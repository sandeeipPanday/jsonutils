# Define the CSV file
$csvFile = "C:\Path\To\File.csv"

# Define the output file
$outputFile = "C:\Path\To\UniqueValues.csv"

# Initialize a hash table to store unique values
$uniqueValues = @{}

# Import CSV file
$csvData = Import-Csv -Path $csvFile

foreach ($row in $csvData) {
    # Add Column G values to the hash table (assuming header "ColumnG")
    $uniqueValues[$row.ColumnG] = $true
}

# Export unique values to CSV
$uniqueValues.Keys | Out-File -FilePath $outputFile

Write-Output "Unique values from Column G saved to $outputFile"
