# 🚀 Git Easy Toolkit Pro

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()

**Một công cụ dòng lệnh (CLI) Đa nền tảng giúp đơn giản hóa mọi thao tác Git phức tạp thành các menu lựa chọn trực quan. Thích hợp cho cả người mới bắt đầu và dân chuyên nghiệp.**

[Tính năng](#-tính-năng-nổi-bật) • [Cài đặt](#-hướng-dẫn-cài-đặt) • [Sử dụng](#-hướng-dẫn-sử-dụng) • [Đóng góp](#-đóng-góp)

</div>

---

## 🌟 Tính Năng Nổi Bật

- **💻 Đa Nền Tảng:** Hoạt động hoàn hảo trên Windows, macOS và Linux.
- **🖥️ Giao diện Dashboard (TUI):** Hiển thị chi tiết trạng thái thư mục, nhánh hiện tại, các file thay đổi và thông tin tài khoản Git.
- **📂 Chọn thư mục thông minh:** 
  - Hỗ trợ **Kéo & Thả (Drag & Drop)** thư mục trực tiếp vào file thực thi.
  - Hỗ trợ **Duyệt Cửa sổ (GUI Dialog)** để chọn thư mục bằng chuột.
  - **Ghi nhớ lịch sử** (Lưu lại 5 thư mục gần nhất để thao tác nhanh).
- **🛡️ Cứu hộ & Xử lý lỗi:**
  - Nút **Undo** (Hoàn tác) giúp khôi phục code an toàn.
  - Tự động phát hiện **Conflict** (Xung đột) và đưa ra gợi ý giải quyết bằng tiếng Việt thay vì báo lỗi đỏ.
- **🤖 Tự động hóa:** Tự động nhận diện project (NodeJS, Python...) để sinh file `.gitignore` chuẩn.
- **🔥 Tích hợp lệnh "Master":** Hỗ trợ đầy đủ từ `fetch`, `rebase`, `cherry-pick`, `tag` đến `git gc` (Dọn rác).

---

## 📦 Hướng Dẫn Cài Đặt

### Yêu cầu hệ thống
- Đã cài đặt **[Git](https://git-scm.com/downloads)**.
- Đã cài đặt **[Python 3.x](https://www.python.org/downloads/)** (Không cần cài thêm bất kỳ thư viện ngoài nào).

### Các bước cài đặt
1. **Clone dự án về máy:**
   ```bash
   git clone https://github.com/your-username/git-easy-toolkit.git
   cd git-easy-toolkit/git_run
   ```

2. **(Tùy chọn) Cài đặt lệnh `gitt` toàn cầu trên Windows:**
   - Copy file `gitt.bat` ở thư mục gốc.
   - Dán vào `C:\Windows`. 
   - Từ giờ, ở bất kỳ thư mục nào mở CMD, bạn chỉ cần gõ `gitt` là công cụ sẽ khởi chạy!

---

## 🚀 Hướng Dẫn Sử Dụng

Bạn không cần mở Terminal và gõ lệnh Python phức tạp. Công cụ đã chuẩn bị sẵn các file khởi chạy (Launcher) cho từng hệ điều hành:

### 🪟 Windows
- Click đúp vào file `Run_Windows.bat`.
- **Mẹo:** Kéo thả trực tiếp một thư mục dự án bất kỳ đè lên file `Run_Windows.bat` để khởi chạy tool ngay tại thư mục đó.

### 🍎 macOS
- Mở Terminal tại thư mục chứa tool, cấp quyền chạy lần đầu:
  ```bash
  chmod +x Run_Mac.command
  ```
- Click đúp vào file `Run_Mac.command` để chạy.

### 🐧 Linux
- Mở Terminal và chạy lệnh:
  ```bash
  chmod +x Run_Linux.sh
  ./Run_Linux.sh
  ```

---

## 📚 Cấu Trúc Menu Lệnh

Hệ thống cung cấp 6 danh mục lệnh được sắp xếp khoa học:

1. **⚙️ Khởi tạo & Cấu hình:** `init`, `clone`, `remote`, `config`.
2. **🔄 Quy trình làm việc:** `pull`, `fetch`, `status`, `push` (add + commit tự động).
3. **🌿 Quản lý nhánh:** `branch`, `checkout`, `merge`, `branch -d`, `branch -m`.
4. **🔍 Lịch sử & Kiểm tra:** `log --graph`, `diff`, `show`, `blame`.
5. **↩️ Sửa lỗi & Hoàn tác:** `restore`, `stash`, `amend`, `reset --soft/hard`, `revert`, `rm --cached`.
6. **🚀 Nâng cao:** `tag`, `cherry-pick`, `rebase`, `git gc`.

---

## 🤝 Đóng Góp (Contributing)

Mọi đóng góp nhằm làm công cụ trở nên thông minh hơn đều được chào đón!
1. Fork dự án này.
2. Tạo nhánh tính năng của bạn: `git checkout -b feature/AmazingFeature`
3. Commit thay đổi: `git commit -m 'Thêm tính năng AmazingFeature'`
4. Push lên nhánh: `git push origin feature/AmazingFeature`
5. Mở một Pull Request.

Vui lòng xem file [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm chi tiết.

---

## 📄 Giấy phép (License)

Dự án này được phân phối dưới giấy phép MIT. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---
*Được phát triển với ❤️ nhằm mang lại trải nghiệm Git thân thiện nhất cho mọi người.*
