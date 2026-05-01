import os
import subprocess
import sys

# Khai báo mã màu ANSI cho Terminal (hoạt động trên Mac, Linux và Windows Terminal)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(f"{Colors.GREEN}{Colors.BOLD}===================================================={Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}       GIT AUTO TOOLKIT (CROSS-PLATFORM)            {Colors.ENDC}")
    print(f"{Colors.GREEN}{Colors.BOLD}===================================================={Colors.ENDC}")
    print()

def run_git_command(command, error_msg):
    try:
        # shell=True giúp chạy được lệnh có chứa khoảng trắng và tham số trên mọi OS
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n{Colors.FAIL}[LỖI] {error_msg}{Colors.ENDC}")
        return False

def get_target_dir():
    while True:
        target_dir = input(f"{Colors.CYAN}>> Nhập đường dẫn thư mục làm việc (VD: D:\\MyProject hoặc /Users/name/project): {Colors.ENDC}").strip()
        
        # Nếu người dùng kéo thả thư mục vào Terminal, có thể nó bị bọc trong dấu nháy kép
        if target_dir.startswith('"') and target_dir.endswith('"'):
            target_dir = target_dir[1:-1]
        elif target_dir.startswith("'") and target_dir.endswith("'"):
            target_dir = target_dir[1:-1]
            
        if os.path.isdir(target_dir):
            return target_dir
        else:
            print(f"{Colors.WARNING}[CẢNH BÁO] Thư mục '{target_dir}' không tồn tại! Vui lòng nhập lại.{Colors.ENDC}")

def menu_loop(target_dir):
    while True:
        print_header()
        print(f"{Colors.BLUE}ĐƯỜNG DẪN HIỆN TẠI: {target_dir}{Colors.ENDC}")
        print(f"{Colors.GREEN}===================================================={Colors.ENDC}")
        print("CHỌN HÀNH ĐỘNG GIT BẠN MUỐN THỰC HIỆN:")
        print("[1] Clone (Tải project mới từ Github về thư mục này)")
        print("[2] Pull  (Cập nhật code mới nhất từ Github về máy)")
        print("[3] Push  (Lưu thay đổi và Đẩy code lên Github)")
        print("[4] Chọn lại thư mục khác")
        print("[5] Thoát chương trình")
        print(f"{Colors.GREEN}===================================================={Colors.ENDC}")
        
        action = input(f"{Colors.CYAN}>> Nhập số (1/2/3/4/5): {Colors.ENDC}").strip()
        
        if action == '1':
            repo_url = input(f"\n{Colors.CYAN}>> Nhập URL của Repository (VD: https://github.com/.../repo.git): {Colors.ENDC}").strip()
            if repo_url:
                print(f"\n{Colors.BLUE}[TIẾN TRÌNH] Đang thực hiện Git Clone...{Colors.ENDC}")
                os.chdir(target_dir)
                if run_git_command(f'git clone "{repo_url}" .', "Clone thất bại. Thư mục có thể không trống hoặc URL sai."):
                    print(f"{Colors.GREEN}[THÀNH CÔNG] Đã tải source code về máy!{Colors.ENDC}")
            input(f"\n{Colors.WARNING}Nhấn Enter để quay lại Menu...{Colors.ENDC}")
            
        elif action == '2':
            branch = input(f"\n{Colors.CYAN}>> Nhập tên nhánh muốn Pull [Mặc định: main]: {Colors.ENDC}").strip()
            if not branch: branch = "main"
            print(f"\n{Colors.BLUE}[TIẾN TRÌNH] Đang thực hiện Git Pull từ nhánh '{branch}'...{Colors.ENDC}")
            os.chdir(target_dir)
            if run_git_command(f'git pull origin "{branch}"', "Pull thất bại. Vui lòng kiểm tra lại kết nối hoặc conflict."):
                print(f"{Colors.GREEN}[THÀNH CÔNG] Đã cập nhật code mới nhất!{Colors.ENDC}")
            input(f"\n{Colors.WARNING}Nhấn Enter để quay lại Menu...{Colors.ENDC}")
            
        elif action == '3':
            commit_msg = input(f"\n{Colors.CYAN}>> Nhập lời nhắn (Commit Message): {Colors.ENDC}").strip()
            if not commit_msg: commit_msg = "Auto commit"
            
            branch = input(f"{Colors.CYAN}>> Nhập tên nhánh muốn Push [Mặc định: main]: {Colors.ENDC}").strip()
            if not branch: branch = "main"
            
            print(f"\n{Colors.BLUE}[TIẾN TRÌNH] Đang thực hiện chuỗi lệnh Push...{Colors.ENDC}")
            os.chdir(target_dir)
            
            print(f"\n{Colors.BOLD}1. Thực hiện: git add .{Colors.ENDC}")
            run_git_command("git add .", "Lỗi khi add file.")
            
            print(f"\n{Colors.BOLD}2. Thực hiện: git commit -m \"{commit_msg}\"{Colors.ENDC}")
            # Lệnh commit có thể trả về lỗi nếu không có gì thay đổi, ta cho qua
            subprocess.run(f'git commit -m "{commit_msg}"', shell=True) 
            
            print(f"\n{Colors.BOLD}3. Thực hiện: git push origin \"{branch}\"{Colors.ENDC}")
            if run_git_command(f'git push origin "{branch}"', "Push thất bại. Bạn có quyền ghi (write access) hoặc cần pull trước không?"):
                print(f"\n{Colors.GREEN}[THÀNH CÔNG] Đã đẩy code lên Github an toàn!{Colors.ENDC}")
                
            input(f"\n{Colors.WARNING}Nhấn Enter để quay lại Menu...{Colors.ENDC}")
            
        elif action == '4':
            return True # Trả về True để quay lại vòng lặp ngoài cùng (chọn thư mục)
            
        elif action == '5':
            print(f"\n{Colors.GREEN}Cảm ơn bạn đã sử dụng Tool. Hẹn gặp lại!{Colors.ENDC}")
            sys.exit(0)
            
        else:
            print(f"\n{Colors.FAIL}[LỖI] Lựa chọn không hợp lệ! Vui lòng nhập số từ 1 đến 5.{Colors.ENDC}")
            input(f"{Colors.WARNING}Nhấn Enter để thử lại...{Colors.ENDC}")

if __name__ == "__main__":
    # Kích hoạt ANSI escape sequence trên Windows (CMD cũ)
    if os.name == 'nt':
        os.system('color')
        
    try:
        while True:
            print_header()
            target_directory = get_target_dir()
            # Nếu menu_loop trả về False hoặc bị thoát ngang, vòng lặp này sẽ chạy lại
            change_dir_request = menu_loop(target_directory)
            if not change_dir_request:
                break
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Đã hủy bởi người dùng (Ctrl+C). Thoát chương trình.{Colors.ENDC}")
        sys.exit(0)
