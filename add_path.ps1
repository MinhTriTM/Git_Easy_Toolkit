$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($currentPath -notmatch "C:\\tools\\git_run") {
    $newPath = $currentPath + ";C:\tools\git_run"
    [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
    Write-Host "Đã thêm C:\tools\git_run vào biến môi trường PATH của User."
} else {
    Write-Host "C:\tools\git_run đã tồn tại trong biến môi trường PATH."
}