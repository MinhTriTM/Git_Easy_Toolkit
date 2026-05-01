@echo off
chcp 65001 >nul
title Git Easy Toolkit
echo Dang kiem tra moi truong Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [LOI] May tinh cua ban chua cai dat Python!
    echo Vui long tai va cai dat Python tai: https://www.python.org/downloads/
    echo Luu y: Nho tick vao o "Add Python to PATH" khi cai dat
    pause
    exit
)

cls
python "%~dp0git_toolkit.py" %*
pause
