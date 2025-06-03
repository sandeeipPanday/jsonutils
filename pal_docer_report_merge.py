import pandas as pd

# File paths
file1 = "file1.csv"  # Large CSV with 'Cluster' and 'Account ID'
file2 = "file2.csv"  # Small CSV with 'clusters'
output_file = "processed_file.csv"

# Load small file fully into memory
df2 = pd.read_csv(file2, dtype={'clusters': str}, low_memory=False)

# Create empty list to store processed chunks
chunk_size = 100000  # Adjust chunk size based on available memory
processed_chunks = []

# Process large file in chunks
for chunk in pd.read_csv(file1, dtype={'Cluster': str, 'Account ID': str}, low_memory=False, chunksize=chunk_size):
    chunk.rename(columns={'Cluster': 'clusters'}, inplace=True)  # Ensure matching column names
    chunk = chunk.merge(df2, on='clusters', how='left')  # Merge chunk with small file
    processed_chunks.append(chunk)

# Combine all processed chunks into a final dataframe
final_df = pd.concat(processed_chunks)

# Save the processed file
final_df.to_csv(output_file, index=False)

print(f"Processing complete! Mapped data saved in {output_file}")
