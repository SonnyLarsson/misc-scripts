$date = Get-Date
$path = ($pwd).path

$location = Get-ChildItem -Path $path | Sort-Object
foreach ($file in $location)
{

    $file.CreationTime = $date
    $file.LastAccessTime = $date
    $file.LastWriteTime = $date
    $date = $date.AddMinutes(1)
    
    '=' * 20
    $CurrentFileInfo = Get-Item -LiteralPath $file.FullName
    $CurrentFileInfo.FullName
    $CurrentFileInfo.CreationTime
    $CurrentFileInfo.LastWriteTime
    $CurrentFileInfo.LastAccessTime 
}
$location

Read-Host -Prompt "Press Enter to exit"