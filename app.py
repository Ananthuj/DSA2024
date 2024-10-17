import os
import cv2
from datetime import datetime
import joblib
import numpy as np
import sys
from sklearn import svm

# Add project path to sys.path for helper functions
sys.path.append(r'c:\\Users\\imaks\\Desktop\\developer\\DSA2024')

from utils.helper import is_valid_timestamp, save_image  # Assuming these functions are implemented in helper.py


def download_folder(folder_id, destination_folder):
    print(f"Downloading folder with ID: {folder_id} to {destination_folder}...")


def get_current_timestamp():
    """Returns the current timestamp in the format YYYY-MM-DD HH:MM:SS."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def capture_image():
    """Automatically captures an image when a face rectangle is detected."""
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return None

    print("Detecting face... The image will be captured once the face rectangle appears.")

    original_frame = None
    face_detected = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        original_frame = frame.copy()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            # Draw rectangle around detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_detected = True

        cv2.imshow("Webcam - Detecting Face", frame)

        if face_detected:
            print("Face detected and rectangle drawn. Capturing image...")
            current_timestamp = get_current_timestamp()

            if is_valid_timestamp(current_timestamp):
                print(f"Image captured with valid timestamp: {current_timestamp}")
            else:
                print("Invalid timestamp.")

            # Release the webcam and close the windows
            cap.release()
            cv2.destroyAllWindows()

            # Return the captured frame
            return original_frame

        # Allow user to exit manually
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None


def train_model():
    """Trains a simple SVM model and saves it."""
    X = [[0], [1], [2], [3]]  # Example features
    y = [0, 1, 1, 0]  # Example labels

    model = svm.SVC(probability=True)
    model.fit(X, y)

    model_directory = os.path.join(os.path.expanduser("~"), "Desktop", "developer", "DSA2024", "model")
    if not os.path.exists(model_directory):
        os.makedirs(model_directory)

    model_path = os.path.join(model_directory, "face_recognition_model.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved at '{model_path}'.")


def infer_model(model, input_data):
    """Infers the model output and probabilities for the input data."""
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)
    return prediction, probabilities


def main():
    # Downloading folder from Google Drive (dummy function)
    destination_folder = os.path.join(
        os.path.expanduser("~"), "Desktop", "developer", "DSA2024"
    )

    folder_id = "1z1nFcsu_fcq44_qMOkK58qF2U5mPSC7H"
    download_folder(folder_id, destination_folder)

    # Train and save model
    train_model()

    # Load the model for inference
    model_directory = os.path.join(
        os.path.expanduser("~"), "Desktop", "developer", "DSA2024", "model"
    )
    model_path = os.path.join(model_directory, "face_recognition_model.pkl")
    model = joblib.load(model_path)

    # Capture an image automatically when a face is detected
    image = capture_image()

    if image is not None:
        save_image(image, directory="temp", filename="temp.jpg")  # Saving captured image

        # Example input data for the model
        input_data = np.array([[1]])  # Adjust input_data to your actual feature set

        # Perform inference
        prediction, probabilities = infer_model(model, input_data)

        print(f"Prediction: {prediction}")
        print(f"Probabilities: {probabilities}")


if __name__ == "__main__":
    main()
