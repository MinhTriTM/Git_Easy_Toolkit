#!/bin/bash

# Di chuyển vị trí làm việc hiện tại vào thư mục chứa file script này
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Kiểm tra Python 3 có tồn tại không
if ! command -v python3 &> /dev/null
then
    echo "❌ Lỗi: Máy Mac của bạn chưa cài Python3!"
    echo "Vui lòng mở Terminal và chạy lệnh: xcode-select --install"
    read -p "Nhấn Enter để thoát..."
    exit
fi

clear
python3 git_toolkit.py "$@"
