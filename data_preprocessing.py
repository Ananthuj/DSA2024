import os
from utils.helper import create_folders
from utils.helper import download_folder
from utils.helper import extract_and_delete_zip

dirs = [".temp", ".database", ".model", ".data"]
create_folders(dirs)

download_folder("1YgEmuOl7qRvg99MzyEWGZLQ4YhoFIiXn", ".data")
extract_and_delete_zip(os.path.join(".data", "data.zip"))
