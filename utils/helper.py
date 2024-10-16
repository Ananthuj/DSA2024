import os
import gdown
from datetime import datetime


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")


def create_folders(dirs):
    for dir in dirs:
        create_folder_if_not_exists(dir)


def download_folder(folder_id, destination_folder):
    destination_path = os.path.join(destination_folder, "data.zip")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    gdown.download(
        f"https://drive.google.com/uc?id={folder_id}", destination_path, quiet=False
    )
    print(f"Folder downloaded to '{destination_path}'.")


def is_valid_timestamp(timestamp_str):
    """
    2024-10-09 15:30:00 returns true
    2024-13-40 99:99:99 returns false
    """
    try:
        _ = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False


def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
