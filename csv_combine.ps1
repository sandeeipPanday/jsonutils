# Define the folder containing CSV files
$csvFolder = "C:\Path\To\CSVFiles"

# Define the output file
$outputFile = "C:\Path\To\Combined.csv"

# Get all CSV files in the folder
$csvFiles = Get-ChildItem -Path $csvFolder -Filter "*.csv"

# Read the first file to get headers
$firstFile = $csvFiles[0].FullName
$header = Get-Content -Path $firstFile | Select-Object -First 1

# Create the output file and add headers
Set-Content -Path $outputFile -Value $header

# Loop through all CSV files and append their content (excluding headers)
foreach ($file in $csvFiles) {
    $content = Get-Content -Path $file | Select-Object -Skip 1
    Add-Content -Path $outputFile -Value $content
}

Write-Output "Combined CSV created at $outputFile"
