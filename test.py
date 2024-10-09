from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# load model
model = keras.models.load_model("model.keras")
# Path to your new image
image_path = "/content/finger_count_2_48.png"

# Load and preprocess the image
img = image.load_img(
    image_path, target_size=(150, 150)
)  # Resize to match the input shape (150x150)
img_array = image.img_to_array(img)  # Convert image to array
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension (1, 150, 150, 3)
img_array /= 255.0  # Rescale by 1./255 to match training preprocessing

# Make the prediction
predictions = model.predict(img_array)

# Get the class with the highest probability
predicted_class_index = np.argmax(
    predictions[0]
)  # Index of the highest predicted probability

# Retrieve class labels from the training generator (train_generator.class_indices)
class_labels = {
    v: k for k, v in train_generator.class_indices.items()
}  # Reverse the dictionary to map index to class name
predicted_class_label = class_labels[predicted_class_index]

# Print prediction result
print(f"Predicted class: {predicted_class_label}")

# Plot the image with the predicted label
plt.imshow(img)
plt.title(f"Predicted: {predicted_class_label}")
plt.axis("off")
plt.show()
