import cv2
from datetime import datetime
import os


def check_timestamp(input_string):
    timestamp_format = "%Y-%m-%d %H:%M:%S"

    try:
        datetime.strptime(input_string, timestamp_format)
        status = True
    except ValueError:
        status = False

    return status


def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_image(image, directory="temp", filename="temp.jpg"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, filename)

    cv2.imwrite(filepath, image)
    print(f"Image saved at '{filepath}'.")

    return filepath


def capture_image():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Webcam - Press s to capture, q to quit', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            current_timestamp = get_current_timestamp()

            if check_timestamp(current_timestamp):
                print(f"Valid timestamp: {current_timestamp}")
            else:
                print("Invalid timestamp.")

            cap.release()
            cv2.destroyAllWindows()
            return original_frame

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None


def main():
    image = capture_image()

    if image is not None:
        save_image(image, directory="temp", filename="temp.jpg")


if __name__ == "__main__":
    main()
