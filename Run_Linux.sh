#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

if ! command -v python3 &> /dev/null
then
    echo "❌ Lỗi: Chưa cài đặt Python3!"
    echo "Chạy lệnh: sudo apt install python3 (Ubuntu/Debian)"
    exit
fi

clear
python3 git_toolkit.py "$@"
