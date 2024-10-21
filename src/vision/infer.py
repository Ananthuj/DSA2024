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
    img_array /= 255.0
    return img_array


def make_model_prediction(model, preprocessed_image, class_labels):
    predictions = model.predict(preprocessed_image)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_label = class_labels.get(predicted_class_index, "Unknown")
    return predicted_class_label


if __name__ == "__main__":
    current_dir = os.getcwd()

    try:
        model = tf.keras.models.load_model(os.path.join(".model", "model.keras"))

        print("Model loaded successfully.")
    except OSError as e:
        print(f"Error loading model: {e}")
        exit()

    image_path = os.path.join("src", "vision", "temp", "temp.jpg")

    try:
        preprocessed_image = load_and_preprocess_image(image_path)
    except FileNotFoundError as e:
        print(e)
        exit()

    # Define class labels (modify as needed for your dataset)
    class_labels = {0: "user1", 1: "user2", 2: "user3", 3: "user4", 4: "user5"}

    predicted_class_label = make_model_prediction(
        model, preprocessed_image, class_labels
    )

    print(f"Predicted class: {predicted_class_label}")
