import pandas as pd

# Load the CSV file
file_path = "C:/path/to/your/file.csv"  # Update with the actual path
df = pd.read_csv(file_path)

# Convert column names to lowercase for consistency
df.columns = df.columns.str.lower()

# Rename updateTimestamp to ensure correct processing
df = df.rename(columns={"updatetimestamp": "updateTimestamp"})

# Convert updateTimestamp to datetime safely
df["updateTimestamp"] = pd.to_datetime(df["updateTimestamp"], errors="coerce")

# Remove duplicates, keeping the latest timestamp
df_cleaned = df.sort_values(by="updateTimestamp", ascending=False).drop_duplicates(subset=["namespace", "vulnerabilityid"], keep="first")

# Save the cleaned data to a new CSV file
output_path = "C:/path/to/cleaned_file.csv"
df_cleaned.to_csv(output_path, index=False)

print("Duplicates removed, latest timestamps kept! Cleaned file saved.")
