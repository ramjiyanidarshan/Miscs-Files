from importlib.resources import contents
from os import listdir, rename
from os.path import *
from tabulate import tabulate

content_folder: str = ""

def printf(message: str, message_type: str = "normal") -> None:
    supported_message_types: list = ["info", "error"]
    message_type = message_type.lower()

    if message_type not in supported_message_types:
        raise InvalidMessageType(message_type)

    if message_type == "info":
        print(f"[\u001b[34;1mInfo\u001b[0m]\t\t:\t\u001b[34m{message}\u001b[0m")
        return
    
    elif message_type == "error":
        print(
            f"[\u001b[31;1mError\u001b[0m]\t\t:\t\u001b[31m{message}\u001b[0m")
        return

def main():
    content_folder  = expanduser(input("Enter folder path (Do not add '\,/' at the end.)\t:\t"))

    if not isdir(content_folder):
        printf(f"Entered path {content_folder} is not folder.", "error")
        return
    
    content_files = listdir(content_folder)
    printf(f"Total {len(content_files)} file(s) are found in folder: {content_folder}", "info")
    
    new_file_name_prefix:str = input("Enter new file name pattern prefix\t:\t")
    new_names = list()

    zfill_char = len(str(len(content_files)))
    
    for i in range(0, len(content_files)):
        new_names.append(
            f"{new_file_name_prefix}{str.zfill(str(i+1), zfill_char)}{content_files[i][content_files[i].find('.'):]}")
        printf(f"{content_files[i]}\t->\t{new_names[i]}", "info")
    confirmation = input("Confirm changes[Y/n]\t:\t")
    if confirmation == "Y" or confirmation == "y":
        for i in range(0, len(content_files)):
            rename_file(content_folder + "/" +
                        content_files[i], content_folder + "/" + new_names[i])
        else:
            printf("Renaming done.", "info")
    else:
        printf("Renaming task abort.", "error")

def rename_file(file_path: str,     new_filename: str):
    try:
        rename(file_path, new_filename)
    except Exception as e:
        printf(e.args, "error")



if __name__ == "__main__":
    while True:
        main()
        choice = input("Would you like to continue?[Y/n]\t:\t")
        if choice == "y" or choice == "Y":
            continue
        else:
            break
    exit(0)