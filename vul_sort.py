import pandas as pd

# Load the CSV file
file_path = "your_csv_file.csv"  # Update with your actual file path
df = pd.read_csv(file_path, dtype=str)  # Read all values as strings to handle formatting issues

# Ensure required columns exist
required_columns = ["namespace", "vulnerabilityID", "updateTimestamp"]
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Missing required columns: {', '.join(set(required_columns) - set(df.columns))}")

# Convert updateTimestamp to datetime, handling errors and missing values
df["updateTimestamp"] = pd.to_datetime(df["updateTimestamp"], errors="coerce")

# Drop rows where namespace or vulnerabilityID are missing
df.dropna(subset=["namespace", "vulnerabilityID"], inplace=True)

# Sort by updateTimestamp to get the latest entries
df.sort_values(by=["namespace", "vulnerabilityID", "updateTimestamp"], ascending=[True, True, False], inplace=True)

# Drop duplicates, keeping only the latest timestamp entry for each namespace-vulnerability pair
df = df.drop_duplicates(subset=["namespace", "vulnerabilityID"], keep="first")

# Save the cleaned data to a new CSV file
output_path = "cleaned_csv_file.csv"
df.to_csv(output_path, index=False)

print(f"Processed file saved as: {output_path}")
