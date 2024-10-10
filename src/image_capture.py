import cv2
import os


def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return

    print("Press 's' to save the image and 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow('Webcam - Press s to save, q to quit', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            save_image(frame, 'temp')
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def save_image(image, path):
    if not os.path.exists(path):
        os.makedirs(path)

    save_path = os.path.join(path, 'temp.jpg')
    cv2.imwrite(save_path, image)
    print(f"Image saved at: {save_path}")


capture_image()
