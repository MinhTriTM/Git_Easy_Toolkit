@echo off
echo.
echo [TIẾN TRÌNH] Đang thực hiện chuỗi lệnh Push...
set TARGET_DIR=%~1
set COMMIT_MSG=%~2
set BRANCH=%~3

:: Di chuyển đến thư mục đích
cd /d "%TARGET_DIR%"

:: Thực hiện các lệnh Git liên tiếp
echo Bác bước thực hiện:
echo - git add .
git add .

echo - git commit -m "%COMMIT_MSG%"
git commit -m "%COMMIT_MSG%"

echo - git push origin "%BRANCH%"
git push origin "%BRANCH%"

echo [THÀNH CÔNG] Đã đẩy code lên Github an toàn!
