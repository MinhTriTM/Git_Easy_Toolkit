@echo off
echo.
echo [TIẾN TRÌNH] Đang thực hiện Git Pull...
set TARGET_DIR=%~1
set BRANCH=%~2

:: Di chuyển đến thư mục đích
cd /d "%TARGET_DIR%"

:: Chạy lệnh pull
git pull origin "%BRANCH%"

echo [THÀNH CÔNG] Đã cập nhật code mới nhất!
