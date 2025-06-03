import pandas as pd

# File paths
file1 = "file1.csv"  # Large CSV with 'Cluster' and 'Account ID'
file2 = "file2.csv"  # Small CSV with 'clusters'
output_file = "processed_file.csv"
chunk_size = 100000  # Process the large file in smaller chunks

# Load small file fully into memory
df2 = pd.read_csv(file2, dtype={'clusters': str}, low_memory=False)

# Open output file for writing
with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
    first_chunk = True  # Flag for handling header write

    # Process large file in chunks
    for chunk in pd.read_csv(file1, dtype={'Cluster': str, 'Account ID': str}, low_memory=False, chunksize=chunk_size):
        chunk.rename(columns={'Cluster': 'clusters'}, inplace=True)  # Ensure matching column name
        chunk = chunk.merge(df2, on='clusters', how='left')  # Merge chunk with small file

        # Append chunk to CSV file without loading all chunks into memory
        chunk.to_csv(f_out, index=False, mode='a', header=first_chunk)
        first_chunk = False  # Only write header once

        print(f"Processed chunk with {len(chunk)} rows and appended to {output_file}")

print(f"Processing complete! Mapped data saved in {output_file}")
