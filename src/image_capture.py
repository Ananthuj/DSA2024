import os
import cv2
import joblib
import numpy as np


def save_image(image, directory="temp", filename="temp.jpg"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, filename)

    cv2.imwrite(filepath, image)
    print(f"Image saved at '{filepath}'.")

    return filepath


def capture_image():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return None

    print("Press 's' to capture the image and 'q' to quit.")

    original_frame = None

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

        cv2.imshow("Webcam - Press s to capture, q to quit", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):
            current_timestamp = get_current_timestamp()

            if check_timestamp(current_timestamp):
                print(f"Valid timestamp: {current_timestamp}")
            else:
                print("Invalid timestamp.")

            cap.release()
            cv2.destroyAllWindows()
            return original_frame

        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None


def infer_model(model, input_data):
    """Infers the model output and probabilities for the input data."""
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
