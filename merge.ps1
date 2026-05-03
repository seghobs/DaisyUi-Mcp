$stepsPath = "C:\Users\user\.gemini\antigravity\brain\be3712f8-1992-486a-b5ac-5cafebb62a54\.system_generated\steps"
$outputFile = "daisyui_all_components.md"

if (Test-Path $outputFile) { Remove-Item $outputFile }

Add-Content -Path $outputFile -Value "# DaisyUI Component Documentation Archive (v5.x)`n"

$files = Get-ChildItem -Path $stepsPath -Recurse -Filter "content.md" | Sort-Object { [int]$_.Directory.Name }

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    if ($lines.Count -lt 110) { continue }

    $title = $lines[0].Substring(7)
    $source = $lines[4].Substring(8)

    $header = "`n## $title`n*Source: $source*`n"
    Add-Content -Path $outputFile -Value $header

    $mainContent = $lines[107..($lines.Count - 1)] -join "`n"
    Add-Content -Path $outputFile -Value $mainContent
    Add-Content -Path $outputFile -Value "`n`n---`n"
    
    Write-Host "Merged: $title"
}
