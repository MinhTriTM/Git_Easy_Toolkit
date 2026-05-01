# Hướng dẫn đóng góp (Contributing Guidelines)

Cảm ơn bạn đã quan tâm đến việc đóng góp cho **Git Easy Toolkit Pro**! Dưới đây là một số nguyên tắc cơ bản để giúp quá trình làm việc nhóm diễn ra suôn sẻ.

## 🐛 Báo cáo lỗi (Bug Reports)
Nếu bạn phát hiện lỗi, vui lòng tạo một Issue trên GitHub và cung cấp các thông tin sau:
- Hệ điều hành đang sử dụng (Windows, macOS, Ubuntu...).
- Phiên bản Python và Git hiện tại.
- Lỗi xuất hiện ở Menu nào.
- Cách tái tạo lỗi (Các bước bạn đã thực hiện trước khi gặp lỗi).

## ✨ Đề xuất tính năng (Feature Requests)
Chúng tôi luôn chào đón các ý tưởng mới! Hãy mở một Issue và mô tả chi tiết:
- Vấn đề mà tính năng mới này sẽ giải quyết.
- Đề xuất giải pháp hoặc cách hoạt động.
- (Tùy chọn) Giao diện UI/UX dự kiến trên Terminal.

## 🛠️ Quy trình gửi Pull Request (PR)
Nếu bạn muốn tự mình sửa lỗi hoặc thêm tính năng, hãy làm theo các bước sau:

1. **Fork** repository này về tài khoản của bạn.
2. Clone repository đã fork về máy:
   ```bash
   git clone https://github.com/your-username/git-easy-toolkit.git
   ```
3. Chuyển sang một nhánh mới với tên mang tính mô tả:
   ```bash
   git checkout -b feature/ten-tinh-nang-cua-ban
   ```
   *(Hoặc `bugfix/sua-loi-abc` nếu bạn fix bug)*
4. Viết code và kiểm tra kỹ trên ít nhất một hệ điều hành. Đảm bảo bạn sử dụng mã màu ANSI chuẩn của project trong `git_toolkit.py`.
5. Đảm bảo thụt lề (Indentation) chuẩn Python (4 spaces).
6. Commit thay đổi với thông điệp rõ ràng.
7. Push nhánh lên GitHub và tạo **Pull Request** vào nhánh `main` của repository gốc.

## 📜 Tiêu chuẩn Code (Coding Standards)
- Project sử dụng Python thuần (không dùng external thư viện `pip install` ngoại trừ các built-in modules như `os`, `sys`, `json`, `subprocess`, `tkinter`) để đảm bảo bất kỳ ai cũng có thể chạy ngay lập tức.
- Giữ vững cấu trúc Menu động, nếu thêm lệnh Git mới, hãy đưa nó vào đúng danh mục logic.

Cảm ơn bạn đã giúp công cụ này trở nên hoàn hảo hơn! 🚀
