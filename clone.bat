@echo off
echo.
echo [TIẾN TRÌNH] Đang thực hiện Git Clone...
set TARGET_DIR=%~1
set REPO_URL=%~2

:: Di chuyển đến thư mục đích
cd /d "%TARGET_DIR%"

:: Chạy lệnh clone (clone thẳng vào thư mục hiện tại)
git clone "%REPO_URL%" .

echo [THÀNH CÔNG] Đã tải source code về máy!
