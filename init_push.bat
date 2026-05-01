@echo off
chcp 65001 >nul
echo.
echo --- 1. KHỞI TẠO VÀ PUSH LÊN GITHUB ---
set /p dir_path="Nhập đường dẫn thư mục dự án trên máy (VD: D:\MyProject): "
if not exist "%dir_path%" (
    echo Thư mục không tồn tại! Đang tạo mới...
    mkdir "%dir_path%"
)
cd /d "%dir_path%"

echo Đang khởi tạo git...
git init
git add .

set /p commit_msg="Nhập nội dung cho commit (VD: Initial commit): "
git commit -m "%commit_msg%"
git branch -M main

set /p git_url="Nhập URL repository Github (VD: https://github.com/user/repo.git): "
git remote add origin "%git_url%"

echo Đang push code lên Github...
git push -u origin main
echo.
echo HOÀN THÀNH!
