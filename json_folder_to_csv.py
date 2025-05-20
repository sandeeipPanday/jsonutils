import os
import json
import pandas as pd

input_folder = "path/to/your/json/folder"
output_folder = "path/to/your/new/csv/folder"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        json_file_path = os.path.join(input_folder, filename)

        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Flatten nested JSON if needed
        if isinstance(data, dict): 
            data = [data]  # Convert dict to list

        df = pd.json_normalize(data)  # Normalize nested structures

        csv_filename = filename.replace(".json", ".csv")
        csv_file_path = os.path.join(output_folder, csv_filename)
        df.to_csv(csv_file_path, index=False)

        print(f"Converted: {filename} -> {csv_filename} in {output_folder}")
