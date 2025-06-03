import pandas as pd

# File paths
file1 = "file1.csv"  # CSV file containing 'Cluster' and 'Account ID'
output_file = "cluster_mapping.xlsx"  # Output Excel file with mapped values

# Load file1.csv with optimized memory settings
df1 = pd.read_csv(file1, dtype={'Cluster': str, 'Account ID': str}, usecols=['Cluster', 'Account ID'], low_memory=False)

# Drop duplicates to keep unique mappings
df1 = df1.drop_duplicates()

# Save extracted mapping to a new Excel file
df1.to_excel(output_file, index=False)

print(f"Mapping extraction complete! Data saved in {output_file}")
