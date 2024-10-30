import os


def create_folder_if_not_exists(folder_path):
    """
    This function creates a folder at the given path if it doesn't already exist.

    Parameters:
    folder_path (str): The full path to the folder.

    Returns:
    bool: True if the folder was created or already exists, False otherwise.
    """
    if not os.path.exists(folder_path):
        try:
            os.makedirs(
                folder_path
            )  # Create the folder and any necessary parent directories
            print(f"Folder '{folder_path}' created successfully.")
            return True
        except OSError as error:
            print(f"Error creating folder '{folder_path}': {error}")
            return False
    else:
        print(f"Folder '{folder_path}' already exists.")
        return True


# Example usage
folder_name = r"C:\Users\midhuna m s\Desktop\image testing"  # Replace with your desired folder path
create_folder_if_not_exists(folder_name)
