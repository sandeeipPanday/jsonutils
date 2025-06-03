import pandas as pd

# Load both CSV files with specified data types and optimized memory handling
file1 = "file1.csv"  # First CSV file with 'Cluster' and 'Account ID' columns
file2 = "file2.csv"  # Second CSV file where 'Cluster' is named 'clusters'

df1 = pd.read_csv(file1, dtype={'Cluster': str, 'Account ID': str}, low_memory=False)
df2 = pd.read_csv(file2, dtype={'clusters': str}, low_memory=False)

# Merge based on 'clusters' column in file2 and 'Cluster' column in file1
df2 = df2.merge(df1.rename(columns={'Cluster': 'clusters'})[['clusters', 'Account ID']], 
                on='clusters', how='left')

# Save the updated file
df2.to_csv("updated_file.csv", index=False)

print("Account ID values copied successfully!")
