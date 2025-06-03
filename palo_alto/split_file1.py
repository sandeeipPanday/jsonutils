import pandas as pd
import os

# Configuration
input_file = "file1.csv"  # Large CSV file
output_folder = "split_chunks"  # Folder to store split files
chunk_size_mb = 100  # Target chunk size in MB

# Create output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Estimate rows per chunk based on file size
file_size = os.path.getsize(input_file) / (1024 * 1024)  # Convert bytes to MB
df_sample = pd.read_csv(input_file, nrows=1000)  # Read sample rows
row_size = df_sample.memory_usage(deep=True).sum() / 1000  # Approximate row size in KB
rows_per_chunk = int((chunk_size_mb * 1024) / row_size)  # Calculate rows per chunk

# Read and split the CSV file
for i, chunk in enumerate(pd.read_csv(input_file, chunksize=rows_per_chunk)):
    chunk_file = os.path.join(output_folder, f"chunk_{i}.csv")
    chunk.to_csv(chunk_file, index=False)
    print(f"Saved chunk {i+1}: {chunk_file}")

print("Splitting complete!")
