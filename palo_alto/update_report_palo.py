import pandas as pd

# File paths
reference_file = "cluster_mapping.xlsx"  # Contains 'Cluster' and 'Account ID'
file2 = "file2.csv"  # Target CSV file where 'Account ID' needs to be inserted
output_file = "updated_file2.csv"  # Final output with mapped 'Account ID'

# Load reference mapping (file1 mapping data)
df_ref = pd.read_excel(reference_file, dtype={'Cluster': str, 'Account ID': str})

# Load file2.csv (target file)
df2 = pd.read_csv(file2, dtype={'clusters': str}, low_memory=False)

# Merge based on 'Cluster' from reference and 'clusters' from file2
df2 = df2.merge(df_ref.rename(columns={'Cluster': 'clusters'})[['clusters', 'Account ID']], 
                on='clusters', how='left')

# Save updated file
df2.to_csv(output_file, index=False)

print(f"Account ID values inserted successfully! Updated file saved as {output_file}")
