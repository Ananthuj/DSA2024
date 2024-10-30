import utils

# Specify the path to the image (Make sure this is a valid image file, e.g., .jpg, .png)
image_path = r"C:\Users\midhuna m s\Desktop\Developer\DSA2024\images\example_image.jpg"  # Change to your actual image file

# Get the shape of the image
shape = utils.get_image_shape(image_path)
if shape:
    print(f"The shape of the image is: {shape}")
else:
    print("Could not retrieve the image shape.")

# Check if the image shape matches the expected input shape
expected_shape = (300, 300, 3)  # Example: height=300, width=300, channels=3 (RGB)
if utils.check_image_shape(image_path, expected_shape):
    print("The image shape matches the expected shape.")
else:
    print("The image shape does not match the expected shape.")
