from colorama import Fore, Style, init
import subprocess, shutil, os

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

def downloader(name, ep, vid_id, download_dir):
    file_name = f"Tập {ep} - {name}"

    print(f"{line.BOLD}{line.YELLOW}\nĐang tải {file_name}.mp4...")
    subprocess.run(f'java -jar "E:\\Quick Access\\App Python\\Anime Downloader\\abyss-dl.jar" {vid_id} h -o {os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4' , text=True, check=False)
    rename(download_dir, vid_id, file_name)

def start():
    print(f"{line.BOLD}{line.CYAN}Trình Tải Anime Từ Server Abyss / HydraX | Tải Nhiều Bộ Anime")
    series = int(input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập số bộ anime cần tải: {line.RESET}"))
    download_dir = input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập đường dẫn tải anime về (Để trống khi tải vào thư mục Downloads): {line.RESET}").replace('"','')
    print()

    names = []
    eps = []
    vid_ids = []
    for inputs in range(series):
        name = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập tên của bộ anime thứ {inputs + 1} cần tải: {line.RESET}"))
        names.append(name)

        ep = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập số tập của bộ anime thứ {inputs + 1} cần tải: {line.RESET}"))
        eps.append(ep)

        vid_id = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Nhập vid_id của tập anime đó: {line.RESET}"))
        vid_ids.append(vid_id)
        print()
    
    if download_dir == "":
        print(f"{line.BOLD}{line.LIGHT_ORANGE}Đang tiến hành tải vào thư mục: Downloads{line.RESET}{download_dir}...")
    else: print(f"{line.BOLD}{line.LIGHT_ORANGE}Đang tiến hành tải vào thư mục: {line.RESET}{download_dir}...")
    
    for run in range(series):
        downloader(names[run], eps[run], vid_ids[run], download_dir)   
