import pandas as pd
import os

# Configuration
input_folder = "split_chunks"  # Folder containing split CSV files
reference_file = "file2.csv"  # Small CSV file
output_file = "processed_file.csv"

# Load reference file
df_ref = pd.read_csv(reference_file, dtype={'clusters': str}, low_memory=False)

# Open output file for writing
with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
    first_chunk = True  # Flag for handling header write

    # Process each split file
    for file in sorted(os.listdir(input_folder)):
        if file.endswith(".csv"):
            chunk_path = os.path.join(input_folder, file)
            print(f"Processing: {chunk_path}")

            # Load chunk
            chunk = pd.read_csv(chunk_path, dtype={'Cluster': str, 'Account ID': str}, low_memory=False)
            chunk.rename(columns={'Cluster': 'clusters'}, inplace=True)  # Ensure matching column name
            chunk = chunk.merge(df_ref, on='clusters', how='left')  # Merge with reference file

            # Write processed chunk to final output file
            chunk.to_csv(f_out, index=False, mode='a', header=first_chunk)
            first_chunk = False  # Only write header once

            print(f"Processed chunk {file} and appended to {output_file}")

print("Processing complete!")
