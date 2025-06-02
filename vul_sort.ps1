# Define the file path
$FilePath = "C:\path\to\your\file.csv"  # Update with the actual path

# Import CSV
$Data = Import-Csv -Path $FilePath

# Convert the timestamp column to datetime format safely
$Data | ForEach-Object { 
    if ($_.updatetimestamp -and $_.updatetimestamp -match "\d{4}-\d{2}-\d{2}") {
        $_.updatetimestamp = [datetime]$_.updatetimestamp 
    } else {
        $_.updatetimestamp = [datetime]"1900-01-01 00:00:00"  # Default fallback for missing values
    }
}

# Remove duplicates and keep the latest timestamp
$FilteredData = $Data | Sort-Object namespace, vulnerabilityid, updatetimestamp -Descending |
                Group-Object namespace, vulnerabilityid |
                ForEach-Object { $_.Group[0] }

# Export the cleaned data back to CSV
$FilteredData | Export-Csv -Path "C:\path\to\cleaned_file.csv" -NoTypeInformation

Write-Output "Duplicates removed, latest timestamps kept! Cleaned file saved."
