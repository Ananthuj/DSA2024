import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image


def load_and_preprocess_image(image_path, target_size=(150, 150)):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")

    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to [0, 1]
    return img_array


def make_model_prediction(model, preprocessed_image, class_labels):
    predictions = model.predict(preprocessed_image)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_label = class_labels.get(predicted_class_index, "Unknown")
    return predicted_class_label


if __name__ == "__main__":
    # Get the path to the main directory (one level up from 'src')
    main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    # Load the model from the main directory
    model_path = os.path.join(main_dir, ".model", "model.keras")
    if not os.path.exists(model_path):
        print(f"Model file not found at {model_path}")
        exit()

    try:
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully.")
    except OSError as e:
        print(f"Error loading model: {e}")
        exit()

    # Load and preprocess the image (assuming it's in the 'temp' folder in the main directory)
    image_path = os.path.join(main_dir, "temp", "temp.jpg")
    try:
        preprocessed_image = load_and_preprocess_image(image_path)
    except FileNotFoundError as e:
        print(e)
        exit()

    # Define class labels (modify as needed for your dataset)
    class_labels = {0: "user1", 1: "user2", 2: "user3", 3: "user4", 4: "user5"}

    # Make prediction
    predicted_class_label = make_model_prediction(
        model, preprocessed_image, class_labels
    )

    print(f"Predicted class: {predicted_class_label}")
