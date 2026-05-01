## 1. Câu hỏi của người dùng
@..\..\Windows\gitt.bat  chưa hoạt động PS D:\Du_An_Mini\Media_Downloader_System> gitt
gitt: The term 'gitt' is not recognized as a name of a cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.

## 2. Suy nghĩ (Thinking) của Agent
- Người dùng đang gặp lỗi không nhận diện lệnh `gitt` trong PowerShell từ thư mục dự án trên ổ D.
- Người dùng có nhắc đến `..\..\Windows\gitt.bat` từ vị trí ổ D, tức là file `gitt.bat` có thể đang nằm ở `D:\Windows\gitt.bat` thay vì `C:\Windows`, do đó hệ thống không tìm thấy file vì thư mục này không nằm trong PATH.
- Kiểm tra nội dung file gốc `C:\tools\git_run\gitt.bat`, phát hiện lỗi logic trong mã lệnh: `call "%~dp0git_run\Run_Windows.bat" %*`. Vì file này đã nằm trong thư mục `git_run` nên đường dẫn này sẽ trỏ sai đến `git_run\git_run\Run_Windows.bat`.
- Thao tác thực hiện:
  1. Tôi đã sửa nội dung file `C:\tools\git_run\gitt.bat` thành đường dẫn tuyệt đối `call "C:\tools\git_run\Run_Windows.bat" %*` để đảm bảo chạy đúng bất kể file `.bat` nằm ở đâu.
  2. Việc chạy lệnh shell từ công cụ của tôi bị từ chối do lỗi môi trường "File not found" của `powershell.exe`, vì vậy tôi không thể tự động cấu hình PATH.
  3. Tôi cần hướng dẫn người dùng tự copy file `gitt.bat` vào đúng thư mục `C:\Windows` hoặc thêm đường dẫn `C:\tools\git_run` vào biến môi trường PATH để lệnh được nhận diện toàn cục.

## 3. Câu trả lời cuối cùng
Lỗi này xảy ra vì 2 lý do:
1. Bạn đang đứng ở ổ `D:\...` và dùng đường dẫn tương đối `..\..\Windows\gitt.bat` (điều này có thể khiến file được lưu vào `D:\Windows` thay vì `C:\Windows`). Hệ thống chỉ nhận diện các lệnh nằm trong `C:\Windows` hoặc thư mục đã được cấu hình trong biến môi trường PATH.
2. Nội dung file `gitt.bat` gốc bị sai đường dẫn gọi file script.

**Tôi đã thực hiện:**
- Sửa lại nội dung file `C:\tools\git_run\gitt.bat` sử dụng đường dẫn tuyệt đối chuẩn xác:
  ```bat
  @echo off
  call "C:\tools\git_run\Run_Windows.bat" %*
  ```

**Cách khắc phục cho bạn (chọn 1 trong 2 cách):**

**Cách 1 (Nhanh nhất):** Copy lại file `gitt.bat` vào thẳng `C:\Windows`.
Bạn hãy mở PowerShell dưới quyền Admin và chạy lệnh sau:
```powershell
Copy-Item -Path "C:\tools\git_run\gitt.bat" -Destination "C:\Windows\gitt.bat" -Force
```

**Cách 2 (Khuyên dùng):** Thêm thư mục công cụ vào biến môi trường PATH.
1. Nhấn phím `Windows` trên bàn phím, gõ **Environment Variables** và chọn *Edit the system environment variables*.
2. Nhấn nút **Environment Variables...** ở góc dưới.
3. Trong bảng phía trên (User variables), tìm và click đúp vào dòng **Path**.
4. Nhấn **New** và dán đường dẫn này vào: `C:\tools\git_run`
5. Nhấn OK để lưu. Sau đó **khởi động lại PowerShell** và gõ `gitt` để dùng.
