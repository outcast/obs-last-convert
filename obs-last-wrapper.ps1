$StartLocation = Get-Location
$ScriptLocation = "E:\Users\James\Stream\Scripts"
Set-Location -Path $ScriptLocation
try {
    . (".\virt-env\Scripts\activate.ps1")
}
catch {
    Write-Host "Error while loading supporting PowerShell Scripts"
}

python .\obs-last-convert.py $ScriptLocation mp4
