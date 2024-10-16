import cv2

def get_image_shape(image_path):
    """
    Get the shape of the image (height, width, number of channels).

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    tuple: The shape of the image (height, width, channels).
    """
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was successfully read
    if image is None:
        print(f"Error: Unable to open image at '{image_path}'")
        return None

    # Get the shape of the image
    shape = image.shape
    print(f"The shape of the image is: {shape}")
    return shape

# Example usage
image_path = r"C:\Users\user\Desktop\testing\image.png"  # Replace with your actual image path
get_image_shape(image_path)-