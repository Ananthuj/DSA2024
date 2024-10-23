import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import cv2
from mtcnn import MTCNN
import time


# Function to detect and return the cropped face part
def get_face_bounding_part(image_path):
    detector = MTCNN()
    try:
        # Load the image
        img = cv2.imread(image_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Detect faces in the image
        faces = detector.detect_faces(img_rgb)

        if len(faces) == 0:
            print("No faces detected in the image.")
            return None

        # Process the first detected face (modify if you want to handle multiple faces)
        face = faces[0]  # Only taking the first face
        x, y, width, height = face["box"]

        # Crop the image to the bounding box
        cropped_img = img_rgb[y : y + height, x : x + width]

        return cropped_img

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None


# Function to load and preprocess the cropped face for model prediction
def load_and_preprocess_image(cropped_face, target_size=(150, 150)):
    try:
        img_resized = cv2.resize(cropped_face, target_size)
        img_array = np.expand_dims(img_resized, axis=0)
        img_array = (
            img_array.astype("float32") / 255.0
        )  # Normalize pixel values to [0, 1]
        return img_array
    except Exception as e:
        print(f"Error in preprocessing image: {e}")
        return None


# Function to make a model prediction on the preprocessed image and print the time taken for the prediction
def make_model_prediction(model, preprocessed_image, class_labels):
    start_time = time.time()
    predictions = model.predict(preprocessed_image)
    end_time = time.time()

    prediction_time = end_time - start_time
    print(f"Prediction time: {prediction_time:.4f} seconds")

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

    # Define the image path
    image_path = os.path.join(main_dir, "captured_images", "captured_1729677895")

    # Step 1: Detect and extract face bounding part
    cropped_face = get_face_bounding_part(image_path)
    if cropped_face is None:
        print("Face not found, unable to proceed with prediction.")
        exit()

    # Step 2: Preprocess the cropped face for model inference
    preprocessed_image = load_and_preprocess_image(cropped_face)
    if preprocessed_image is None:
        print("Error in preprocessing image, exiting.")
        exit()

    # Define class labels (modify as needed for your dataset)
    class_labels = {0: "user1", 1: "user2", 2: "user3", 3: "user4", 4: "user5"}

    # Step 3: Make prediction
    predicted_class_label = make_model_prediction(
        model, preprocessed_image, class_labels
    )

    print(f"Predicted class: {predicted_class_label}")