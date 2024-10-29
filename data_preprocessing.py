import os
import shutil
from utils.helper import create_folders
from utils.helper import download_folder
from utils.helper import extract_and_delete_zip

# Create necessary folders
dirs = [".temp", ".database", ".model", ".data"]
create_folders(dirs)

# File ID extracted from the Google Drive link
file_id = "1sxW1Zqfr7lDQDPMwaTTctS-bNHFYmhCk"
download_folder(file_id, ".data")

# Path to the downloaded zip file
zip_path = os.path.join(".data", "data.zip")

# Extract the zip file and delete it afterward
extract_and_delete_zip(zip_path)


extracted_folder = os.path.join(".data", ".data")

# Check if the nested folder exists and move its contents
if os.path.exists(extracted_folder):
    for item in os.listdir(extracted_folder):
        source = os.path.join(extracted_folder, item)
        destination = os.path.join(".data", item)

        # Move files and directories from the inner folder to the parent folder
        if os.path.isdir(source):
            shutil.move(source, destination)
        else:
            shutil.move(source, destination)

    # Remove the now-empty inner folder
    os.rmdir(extracted_folder)
