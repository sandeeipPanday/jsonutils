import pandas as pd

# Load both CSV files
file1 = "file1.csv"  # First CSV file with 'Cluster' and 'Account ID' columns
file2 = "file2.csv"  # Second CSV file where you need to copy 'Account ID' values

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Merge based on 'Cluster' column
df2 = df2.merge(df1[['Cluster', 'Account ID']], on='Cluster', how='left')

# Save updated file
df2.to_csv("updated_file.csv", index=False)

print("Account ID values copied successfully!")
