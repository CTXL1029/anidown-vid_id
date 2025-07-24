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
        print(f"{line.RED}Auto close window after: {i}...")
        time.sleep(1)
    exit()

def retry(is_advanced_download):
    if is_advanced_download == True:
        print(f"{line.BOLD}{line.GREEN}Continue download? (Y/F/M/N)\n")
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
        print(f"{line.BOLD}{line.GREEN}Continue download?  (Y/N)\n")
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
    name = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the name of anime series you want to download: {line.RESET}"))
    authenticate(name)
    ep = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter the number of episode: {line.RESET}"))
    vid_id = str(input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter vid_id of anime episode: {line.RESET}"))
    download_dir = input(f"{line.BOLD}{line.LIGHT_ORANGE}Enter download directory (Press Enter to download the file to the Downloads folder): {line.RESET}").replace('"','')
    if "Movie" in ep:
        file_name = f"{ep} - {name}"
    else: file_name = f"Ep {ep} - {name}"

    if download_dir == "":
        print(f"{line.BOLD}{line.YELLOW}Downloading to Downloads folder...{line.RESET}")
        subprocess.run(f'java -jar abyss-dl.jar {vid_id} h -o {os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4' , text=True, check=False)
        rename(download_dir, vid_id, file_name)
    else:
        print(f"{line.BOLD}{line.YELLOW}Downloading to {line.RESET}{download_dir} {line.BOLD}{line.YELLOW}folder...")
        subprocess.run(f'java -jar abyss-dl.jar {vid_id} h -o {os.path.expanduser('~') + "\\Downloads\\"}{vid_id}.mp4' , text=True, check=False)  
        rename(download_dir, vid_id, file_name)     
    retry(is_advanced_download = False)
    

if __name__ == "__main__":
    os.system('cls')
    print(f"{line.BOLD}{line.CYAN}Anime Downloader From Abyss / HydraX Server")
    try:
        main()
    except Exception as e:
        print(f"{line.RED}{line.BOLD}Something went wrong: \n{e}")
        input("Press Enter to close window")