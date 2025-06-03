import pandas as pd
import os

# Configurable parameters
input_file = "file2.csv"  # Large CSV file to split
reference_file = "file1.csv"  # CSV file containing 'Cluster' and 'Account ID'
chunk_size = 100000  # Adjust based on memory limitations
output_folder = "split_chunks"
final_output = "processed_file.csv"

# Step 1: Load reference file with mappings
df_ref = pd.read_csv(reference_file, dtype={'Cluster': str, 'Account ID': str}, low_memory=False)
df_ref.rename(columns={'Cluster': 'clusters'}, inplace=True)  # Ensure matching column name

# Step 2: Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 3: Split the large CSV file
chunk_list = []
for i, chunk in enumerate(pd.read_csv(input_file, dtype={'clusters': str}, low_memory=False, chunksize=chunk_size)):
    chunk = chunk.merge(df_ref[['clusters', 'Account ID']], on='clusters', how='left')
    chunk_output_file = os.path.join(output_folder, f"chunk_{i}.csv")
    chunk.to_csv(chunk_output_file, index=False)
    chunk_list.append(chunk_output_file)
    print(f"Processed chunk {i+1}, saved as {chunk_output_file}")

# Step 4: Combine processed chunks into a final CSV file
combined_df = pd.concat([pd.read_csv(f, low_memory=False) for f in chunk_list])
combined_df.to_csv(final_output, index=False)

print(f"Final processed file saved as {final_output}")
