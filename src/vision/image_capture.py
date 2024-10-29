import cv2
import os
from datetime import datetime

def download_folder(folder_id, destination_folder):
    print(f"Downloading folder with ID: {folder_id} to {destination_folder}...")

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def capture_image(output_path):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow("Face Detection", frame)

            if len(faces) > 0:
                cv2.imwrite(output_path, frame)
                print(f"Image saved at {output_path}")
                break

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    temp_image_path = os.path.join(main_dir, "src", "vision", ".temp", "temp.jpg")

    os.makedirs(os.path.dirname(temp_image_path), exist_ok=True)

    capture_image(temp_image_path)
