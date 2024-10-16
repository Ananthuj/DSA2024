import os


def check_image_exists(image_path):
    """
    This function checks if an image file exists at the given path.

    Parameters:
    image_path (str): The full path to the image file.

    Returns:
    bool: True if the image exists, False otherwise.
    """
    # Check if the file exists and is a file (not a directory)
    if os.path.isfile(image_path):
        print(f"The image file '{image_path}' exists.")
        return True
    else:
        print(f"The image file '{image_path}' does not exist.")
        return False


# Example usage
image_path = r"C:\Users\midhuna m s\Desktop\Developer\DSA2024\testing\images\meera.jpg"  # Replace with your actual image path

# Store the result of the first check
image_exists = check_image_exists(image_path)

if image_exists:
    print("Proceeding with image processing...")
else:
    print("Image file not found, exiting program.")
