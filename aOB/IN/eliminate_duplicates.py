import json
from pathlib import Path

# -------- configuration --------
input_path  = Path(r"D:\montruth\EM_classification\aOB\IN\250708_072403_neuron_classification.json")   # ← original file
output_path = Path(r"D:\montruth\EM_classification\aOB\IN\250708_072404_neuron_classification.json") # ← file to create
# --------------------------------

def main():

    # 1. load the file -------------------------------------------------------
    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if "-1" not in data:
        raise ValueError('Group "-1" not found in the JSON.')

    base_set = set(data["-1"])            # all IDs that must stay only here

    # 2. iterate over every other group and filter --------------------------
    cleaned = {"-1": data["-1"]}          # start with the untouched -1 list

    for group, values in data.items():
        if group == "-1":
            continue                      # already handled

        # keep only the items NOT in the base set
        cleaned[group] = [v for v in values if v not in base_set]

    # 3. write the result ---------------------------------------------------
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)

    print(f"Finished. Cleaned JSON written to {output_path}")

if __name__ == "__main__":
    main()