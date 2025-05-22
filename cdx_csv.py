import json
import pandas as pd

# Load the CycloneDX JSON file
with open("cyclonedx.json", "r") as file:
    data = json.load(file)

# Extract components (modify keys as needed)
components = data.get("components", [])

# Convert to DataFrame
df = pd.DataFrame(components)

# Save to CSV
df.to_csv("cyclonedx.csv", index=False)

print("Conversion completed successfully!")
