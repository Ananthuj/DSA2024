<<<<<<< HEAD
from datetime import datetime


def is_valid_timestamp(timestamp_str):
    try:
        # Define the expected format of the timestamp
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return True  # Return True if valid
    except ValueError:
        return False  # Return False if invalid


# Example usage:
input_str = "2024-10-09 15:30:00"
print(is_valid_timestamp(input_str))  # Output: True

invalid_input_str = "2024-13-40 99:99:99"
print(is_valid_timestamp(invalid_input_str))  # Output: False


from datetime import datetime


def test_timestamp(timestamp_str):
    try:
        # Define the expected format of the timestamp
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        # Format the timestamp to calendar time (e.g., October 9, 2024, 3:30 PM)
        calendar_time = timestamp.strftime("%B %d, %Y, %I:%M %p")
        return True, calendar_time  # Return True and the formatted calendar time
    except ValueError:
        return False, None  # Return False if invalid


# Example usage:
input_str = "2024-10-09 15:30:00"
is_valid, calendar_time = test_timestamp(input_str)
print(f"Is valid: {is_valid}, Calendar Time: {calendar_time}")

invalid_input_str = "2024-13-40 99:99:99"
is_valid, calendar_time = test_timestamp(invalid_input_str)
print(f"Is valid: {is_valid}, Calendar Time: {calendar_time}")
=======
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow as tf

# Directory where the dataset is located
current_dir = os.getcwd()

# Load the model
model = tf.keras.models.load_model("model.keras")

# Path to your new image
image_path = os.path.join(current_dir, ".testdata", "user1.jpg")

# Load and preprocess the image
img = image.load_img(
    image_path, target_size=(150, 150)
)  # Resize to match the input shape
img_array = image.img_to_array(img)  # Convert image to array
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension (1, 150, 150, 3)
img_array /= 255.0  # Rescale by 1./255 to match training preprocessing

# Make the prediction
predictions = model.predict(img_array)

# Get the class with the highest probability
predicted_class_index = np.argmax(
    predictions[0]
)  # Index of the highest predicted probability

# Manually define class labels (if you have 5 classes, for example)
class_labels = {0: "user1", 1: "user2", 2: "user3", 3: "user4", 4: "user5"}

# Get the predicted class label
predicted_class_label = class_labels.get(predicted_class_index, "Unknown")

# Print prediction result
print(f"Predicted class: {predicted_class_label}")

# Plot the image with the predicted label
plt.imshow(image.load_img(image_path))  # Show the image
plt.title(f"Predicted: {predicted_class_label}")
plt.axis("off")
plt.show()
>>>>>>> 6eca79f4483b046b2a64b5795b216b624570a837
