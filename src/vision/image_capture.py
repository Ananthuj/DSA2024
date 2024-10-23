import cv2
import os


<<<<<<< HEAD
def download_folder(folder_id, destination_folder):
    print(f"Downloading folder with ID: {folder_id} to {destination_folder}...")
def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def capture_image():
=======
def capture_image(output_path):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    # Load the pre-trained Haar cascade classifier for face detection
>>>>>>> c420ce0aa4c33b3b55da198bd9026c02227635bc
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if ret:
            # Convert frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            # Draw bounding boxes around the detected faces
            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display the frame with bounding boxes
            cv2.imshow("Face Detection", frame)

            # If faces are detected, save the image and exit
            if len(faces) > 0:
                cv2.imwrite(output_path, frame)
                print(f"Image saved at {output_path}")
                break

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Path to save the captured image (modify path as needed)
    main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    temp_image_path = os.path.join(main_dir, "src", "vision", ".temp", "temp.jpg")

    # Ensure .temp directory exists
    os.makedirs(os.path.dirname(temp_image_path), exist_ok=True)

    # Capture and save the image when a face is detected
    capture_image(temp_image_path)
