import os
import cv2
from datetime import datetime
import joblib
import numpy as np
import sys
import time
from sklearn import svm

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.expanduser("~"), "Desktop", "developer", "DSA2024")
    )
)

from utils.helper import is_valid_timestamp, save_image


def download_folder(folder_id, destination_folder):
    print(f"Downloading folder with ID: {folder_id} to {destination_folder}...")


def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def capture_image():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return None

    print("The camera is detecting faces. Press 'q' to quit.")

    original_frame = None
    face_detected = False
    face_detection_time = None

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

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            if not face_detected:
                face_detected = True
                face_detection_time = time.time()

        cv2.imshow("Webcam - Detecting Faces", frame)

        if face_detected and (time.time() - face_detection_time >= 1):
            current_timestamp = get_current_timestamp()

            if is_valid_timestamp(current_timestamp):
                print(
                    f"Face detected!! Capturing image with timestamp: {current_timestamp}"
                )
            else:
                print("Invalid timestamp.")

            cap.release()
            cv2.destroyAllWindows()
            return original_frame

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None


def train_model():
    X = [[0], [1], [2], [3]]
    y = [0, 1, 1, 0]

    model = svm.SVC(probability=True)
    model.fit(X, y)

    model_directory = os.path.join(
        os.path.expanduser("~"), "Desktop", "developer", "DSA2024", "model"
    )
    if not os.path.exists(model_directory):
        os.makedirs(model_directory)

    model_path = os.path.join(model_directory, "face_recognition_model.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved at '{model_path}'.")


def infer_model(model, input_data):
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)
    return prediction, probabilities


def main():
    destination_folder = os.path.join(
        os.path.expanduser("~"), "Desktop", "developer", "DSA2024"
    )

    folder_id = "1z1nFcsu_fcq44_qMOkK58qF2U5mPSC7H"
    download_folder(folder_id, destination_folder)

    train_model()

    model_directory = os.path.join(
        os.path.expanduser("~"), "Desktop", "developer", "DSA2024", "model"
    )
    model_path = os.path.join(model_directory, "face_recognition_model.pkl")
    model = joblib.load(model_path)

    image = capture_image()

    if image is not None:
        save_image(image, directory="temp", filename="temp.jpg")

        input_data = np.array([[1]])

        prediction, probabilities = infer_model(model, input_data)

        print(f"Prediction: {prediction}")
        print(f"Probabilities: {probabilities}")


if __name__ == "__main__":
    main()
