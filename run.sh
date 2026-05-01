#!/bin/bash
# Script để chạy Git Tool trên macOS/Linux
echo "Đang khởi chạy Git Auto Toolkit..."
if command -v python3 &>/dev/null; then
    python3 git_tool.py
elif command -v python &>/dev/null; then
    python git_tool.py
else
    echo "[LỖI] Không tìm thấy Python! Vui lòng cài đặt Python để sử dụng tool đa nền tảng này."
    read -p "Nhấn Enter để thoát..."
fi
