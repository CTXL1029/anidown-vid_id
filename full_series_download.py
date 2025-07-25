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
    try:
        os.rename(f"{os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4", f"{os.path.expanduser('~') + "\\Downloads\\"}{new_name}.mp4")
        shutil.move(f"{os.path.expanduser('~') + "\\Downloads\\"}{new_name}.mp4", f"{download_dir}\\{new_name}.mp4")
    except FileNotFoundError:
        print(f"\n{line.RED}{line.BOLD}Error: '{vid_id}.mp4' not found ")
    except FileExistsError:
        print(f"\n{line.RED}{line.BOLD}Error: File '{new_name}.mp4' has existed.")
    except Exception as e:
        print(f"\n{line.RED}{line.BOLD}Something went wrong: {e}")

def downloader(name, eps, seasons, download_dir, vid_ids):
    for i in range(0, len(eps)):
        if seasons == "":
            file_name = f"Ep {eps[i]} - {name}"
        else: file_name = f"Ep {eps[i]} (Season {seasons}) - {name}"

        print(f"{line.BOLD}{line.YELLOW}\nDownloading {file_name}.mp4...")
        subprocess.run(f'java -jar abyss-dl.jar {vid_ids[i]} h -o {os.path.expanduser('~') + "\\Downloads\\"}{vid_ids[i]}.mp4' , text=True, check=False)
        rename(download_dir, vid_ids[i], file_name)

def lists_vids(ep_start, ep_end):
    eps = []
    for ep in range(ep_start, ep_end + 1):
        if 0 <= ep <= 9:
            eps.append(f"0{ep}")
        else: eps.append(ep)

    vid_ids = []
    print()
    for i in range(0, len(eps)):
        vid_id = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter vid_id of episode {eps[i]}: {line.RESET}"))
        vid_ids.append(vid_id)

    return vid_ids, eps


def start():
    print(f"{line.BOLD}{line.CYAN}Anime Downloader From Abyss / HydraX Server | Download Full Season Anime")
    name = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the name of anime series you want to download: {line.RESET}"))
    ep_start, ep_end = map(int, input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the episode distance of the anime series: {line.RESET}").split(" - "))
    seasons = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the season of the anime (Press Enter to skip): {line.RESET}"))
    download_dir = input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter download directory: {line.RESET}").replace('"','')
    vid_ids, eps = lists_vids(ep_start, ep_end)
    
    print(f"{line.BOLD}{line.LIGHT_ORANGE}Downloading to {line.RESET}{download_dir} {line.BOLD}{line.LIGHT_ORANGE}folder...")
    downloader(name, eps, seasons, download_dir, vid_ids)   
