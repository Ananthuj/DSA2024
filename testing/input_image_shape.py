import cv2


def check_image_shape(image_path, input_shape):
    """
    Check if the shape of the image matches the given input shape.


    Parameters:
    image_path (str): The path to the image file.
    input_shape (tuple): The expected shape (height, width, channels).

    Returns:
    bool: True if the image shape matches the input shape, False otherwise.

    """
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was successfully read
    if image is None:
        print(f"Error: Unable to open image at '{image_path}'")
        return False

    # Get the shape of the image
    image_shape = image.shape

    # Check if the image shape matches the input shape
    if image_shape == input_shape:
        print(f"Image shape matches the input shape: {image_shape}")
        return True
    else:
        print(f"Image shape {image_shape} does not match the input shape {input_shape}")
        return False


# Example usage
image_path = r"C:\Users\midhuna m s\Desktop\Developer\DSA2024\testing\images\meera.jpg"
expected_shape = (260, 194, 3)  # Example expected shape (height, width, channels)

check_image_shape(image_path, expected_shape)
