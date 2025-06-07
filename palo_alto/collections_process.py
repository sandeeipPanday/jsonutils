import pandas as pd

# Load the CSV file (update the filename accordingly)
df = pd.read_csv("source_file.csv")

# Ensure 'Collections' is treated as a string and split on commas
df['Collections'] = df['Collections'].astype(str).str.split(',')

# Expand rows based on 'Collections' while keeping other columns the same
df_expanded = df.explode('Collections')

# Save the modified data to a new file
df_expanded.to_csv("output_file.csv", index=False)

print("Successfully processed and saved the file!")
