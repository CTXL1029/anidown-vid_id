from colorama import Fore, Style, init
import full_series_download, multiple_series_download, subprocess, shutil, msvcrt, time, os

init()
class line:
    BOLD = Style.BRIGHT
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    LIGHT_ORANGE = "\033[38;5;214m"
    ORANGE = "\033[38;5;208m"
    RESET = Style.RESET_ALL

def countdown():
    for i in range(3, 0, -1):
        print(f"{line.RED}Tự động đóng cửa sổ sau: {i}...")
        time.sleep(1)
    exit()

def retry(is_advanced_download):
    if is_advanced_download == True:
        print(f"{line.BOLD}{line.GREEN}Tiếp tục tải? (Y/F/M/N)\n")
        while True:
            key = msvcrt.getch().decode('latin-1').lower()
            if key == "y":
                main()
                break
            elif key == "f":
                os.system('cls')
                full_series_download.start()
                break
            elif key == "m":
                os.system('cls')
                multiple_series_download.start()
                break            
            elif key == "n":
                countdown()
                break
    else:
        print(f"{line.BOLD}{line.GREEN}Tiếp tục tải? (Y/N)\n")
        while True:
            key = msvcrt.getch().decode('latin-1').lower()
            if key == "y":
                main()
                break
            elif key == "n":
                countdown()
                break        

def rename(download_dir, vid_id, new_name):
    if download_dir == "":
        try:
            os.rename(os.path.expanduser('~') + f"\\Downloads\\{vid_id}.mp4", os.path.expanduser('~') + f"\\Downloads\\{new_name}.mp4")
        except FileNotFoundError:
            print(f"\n{line.RED}{line.BOLD}Lỗi: Không tìm thấy file '{vid_id}.mp4'. ")
        except FileExistsError:
            print(f"\n{line.RED}{line.BOLD}Lỗi: File '{new_name}.mp4' đã tồn tại.")
        except Exception as e:
            print(f"\n{line.RED}{line.BOLD}Đã xảy ra lỗi: {e}")
    else:
        try:
            os.rename(f"{os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4", f"{os.path.expanduser('~') + "\\Downloads\\"}{new_name}.mp4")
            shutil.move(f"{os.path.expanduser('~') + "\\Downloads\\"}{new_name}.mp4", f"{download_dir}\\{new_name}.mp4")
        except FileNotFoundError:
            print(f"\n{line.RED}{line.BOLD}Lỗi: Không tìm thấy file '{vid_id}.mp4'. ")
        except FileExistsError:
            print(f"\n{line.RED}{line.BOLD}Lỗi: File '{new_name}.mp4' đã tồn tại.")
        except Exception as e:
            print(f"\n{line.RED}{line.BOLD}Đã xảy ra lỗi: {e}")

def authenticate(vid_id):
    if vid_id == "f":
        os.system('cls')
        full_series_download.start()
        retry(is_advanced_download = True)
    elif vid_id == "m":
        os.system('cls')
        multiple_series_download.start()
        retry(is_advanced_download = True)

def main():
    name = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập tên của bộ anime cần tải: {line.RESET}"))
    authenticate(name)
    ep = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập số tập của bộ anime cần tải: {line.RESET}"))
    vid_id = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập vid_id của tập anime: {line.RESET}"))
    download_dir = input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập đường dẫn tải anime về (Để trống khi tải vào thư mục Downloads): {line.RESET}").replace('"','')
    if "Movie" in ep:
        file_name = f"{ep} - {name}"
    else: file_name = f"Tập {ep} - {name}"

    if download_dir == "":
        print(f"{line.BOLD}{line.YELLOW}Đang tiến hành tải vào thư mục Downloads...{line.RESET}")
        subprocess.run(f'java -jar abyss-dl.jar {vid_id} h -o {os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4' , text=True, check=False)
        rename(download_dir, vid_id, file_name)
    else:
        print(f"{line.BOLD}{line.YELLOW}Đang tiến hành tải vào thư mục {download_dir}...{line.RESET}")
        subprocess.run(f'java -jar abyss-dl.jar {vid_id} h -o {os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4' , text=True, check=False)  
        rename(download_dir, vid_id, file_name)     
    retry(is_advanced_download = False)
    

if __name__ == "__main__":
    os.system('cls')
    print(f"{line.BOLD}{line.CYAN}Trình Tải Anime Từ Server Abyss / HydraX")
    try:
        main()
    except Exception as e:
        print(f"{line.RED}{line.BOLD}Đã có lỗi xảy ra: \n{e}")
        input("Nhấn Enter để đóng cửa sổ")