import os
import json
import pandas as pd

# Define input and output folder paths
input_folder = "path/to/your/json/folder"
output_folder = "path/to/your/new/csv/folder"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each JSON file in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        json_file_path = os.path.join(input_folder, filename)

        # Read JSON file
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Convert JSON data to Pandas DataFrame
        df = pd.DataFrame(data)

        # Save as CSV in the new folder
        csv_filename = filename.replace(".json", ".csv")
        csv_file_path = os.path.join(output_folder, csv_filename)
        df.to_csv(csv_file_path, index=False)

        print(f"Converted: {filename} -> {csv_filename} in {output_folder}")
