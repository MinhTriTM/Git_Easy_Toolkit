@echo off
chcp 65001 >nul
color 0A
title Git Auto Toolkit by AI
:START
cls
echo ====================================================
echo             TOOL QUẢN LÝ GIT TỰ ĐỘNG
echo ====================================================
echo.
set /p target_dir=">> Nhập đường dẫn thư mục làm việc (VD: D:\MyProject): "

if not exist "%target_dir%" (
    echo [LỖI] Thư mục không tồn tại! Vui lòng nhập lại.
    pause
    goto START
)

:MENU
cls
echo ====================================================
echo ĐƯỜNG DẪN HIỆN TẠI: %target_dir%
echo ====================================================
echo CHỌN HÀNH ĐỘNG GIT BẠN MUỐN THỰC HIỆN:
echo [1] Clone (Tải project mới từ Github về thư mục này)
echo [2] Pull  (Cập nhật code mới nhất từ Github về máy)
echo [3] Push  (Lưu thay đổi và Đẩy code lên Github)
echo [4] Chọn lại thư mục khác
echo [5] Thoát chương trình
echo ====================================================
set /p action=">> Nhập số (1/2/3/4/5): "

if "%action%"=="1" (
    echo.
    set /p repo_url=">> Nhập URL của Repository (VD: https://github.com/.../repo.git): "
    call clone.bat "%target_dir%" "%repo_url%"
) else if "%action%"=="2" (
    echo.
    set /p branch=">> Nhập tên nhánh muốn Pull (VD: main, master): "
    call pull.bat "%target_dir%" "%branch%"
) else if "%action%"=="3" (
    echo.
    set /p commit_msg=">> Nhập lời nhắn (Commit Message): "
    set /p branch=">> Nhập tên nhánh muốn Push (VD: main, master): "
    call push.bat "%target_dir%" "%commit_msg%" "%branch%"
) else if "%action%"=="4" (
    goto START
) else if "%action%"=="5" (
    exit
) else (
    echo [LỖI] Lựa chọn không hợp lệ!
    pause
    goto MENU
)

echo.
echo ====================================================
echo XONG! NHIỆM VỤ ĐÃ HOÀN TẤT.
echo ====================================================
pause
goto MENU
