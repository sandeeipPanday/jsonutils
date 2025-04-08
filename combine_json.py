import json
import os

def combine_json_files(input_directory, output_file):
    combined_data = {}
    
    # Loop through all files in the directory
    for file_name in os.listdir(input_directory):
        if file_name.endswith('.json'):  # Process only JSON files
            file_path = os.path.join(input_directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    combined_data.update(data)  # Merge data
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON file: {file_name}")
    
    # Write the combined data to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(combined_data, output, indent=4)
    print(f"Combined JSON saved to {output_file}")

# Example usage
input_directory = 'path_to_directory_containing_json_files'
output_file = 'combined.json'
combine_json_files(input_directory, output_file)