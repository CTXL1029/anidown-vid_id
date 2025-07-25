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
            print(f"\n{line.RED}{line.BOLD}Error: '{vid_id}.mp4' not found ")
        except FileExistsError:
            print(f"\n{line.RED}{line.BOLD}Error: File '{new_name}.mp4' has existed.")
        except Exception as e:
            print(f"\n{line.RED}{line.BOLD}Something went wrong: {e}")
    else:
        try:
            os.rename(f"{os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4", f"{os.path.expanduser('~') + "\\Downloads\\"}{new_name}.mp4")
            shutil.move(f"{os.path.expanduser('~') + "\\Downloads\\"}{new_name}.mp4", f"{download_dir}\\{new_name}.mp4")
        except FileNotFoundError:
            print(f"\n{line.RED}{line.BOLD}Error: '{vid_id}.mp4' not found ")
        except FileExistsError:
            print(f"\n{line.RED}{line.BOLD}Error: File '{new_name}.mp4' has existed.")
        except Exception as e:
            print(f"\n{line.RED}{line.BOLD}Something went wrong: {e}")

def downloader(name, ep, vid_id, download_dir):
    file_name = f"Tập {ep} - {name}"

    print(f"{line.BOLD}{line.YELLOW}\nDownloading {file_name}.mp4...")
    subprocess.run(f'java -jar abyss-dl.jar {vid_id} h -o {os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4' , text=True, check=False)
    rename(download_dir, vid_id, file_name)

def start():
    print(f"{line.BOLD}{line.CYAN}Anime Downloader From Abyss / HydraX Server | Download Multiple Anime Series")
    series = int(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the number of anime series to download: {line.RESET}"))
    download_dir = input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter download directory (Press Enter to download the file to the Downloads folder): {line.RESET}").replace('"','')
    print()

    names = []
    eps = []
    vid_ids = []
    for inputs in range(series):
        name = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the name of the anime series - Number {inputs + 1}: {line.RESET}"))
        names.append(name)

        ep = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the episode number of the anime series - Number {inputs + 1}: {line.RESET}"))
        eps.append(ep)

        vid_id = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the vid_id of that anime episode: {line.RESET}"))
        vid_ids.append(vid_id)
        print()
    
    if download_dir == "":
        print(f"{line.BOLD}{line.LIGHT_ORANGE}Downloading anime to: Downloads folder{line.RESET}...")
    else: print(f"{line.BOLD}{line.LIGHT_ORANGE}Downloading anime to: {line.RESET}{download_dir} {line.BOLD}{line.LIGHT_ORANGE}folder...")
    
    for run in range(series):
        downloader(names[run], eps[run], vid_ids[run], download_dir)   
