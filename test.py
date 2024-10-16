import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

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
