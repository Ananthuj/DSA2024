import cv2
import os
import zipfile

# Define the number of users and images per user
num_users = 5
images_per_user = 100
output_folder = ".data"

# Create the main data folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize the face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# Function to capture face images for a user
def capture_images(user_id, images_per_user):
    # Create a folder for the user
    user_folder = os.path.join(output_folder, f"user{user_id}")
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    # Start video capture
    cap = cv2.VideoCapture(0)
    count = 0

    while count < images_per_user:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image. Exiting...")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw a bounding box around each face and save the image
        for x, y, w, h in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Crop the face
            face_img = frame[y : y + h, x : x + w]
            # Save the face image
            img_path = os.path.join(user_folder, f"user{user_id}_image{count+1}.jpg")
            cv2.imwrite(img_path, face_img)
            count += 1

            # Display the frame with the bounding box
            cv2.imshow("Face Capture", frame)

            if cv2.waitKey(250) & 0xFF == ord("q"):
                break

        if count >= images_per_user:
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()


# Function to zip the folder
def zip_folder(folder_name, zip_name):
    with zipfile.ZipFile(zip_name, "w") as zip_file:
        for folder, subfolders, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(folder, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_name))


# Capture images for each user
for user_id in range(1, num_users + 1):
    print(f"Capturing images for User {user_id}...")
    capture_images(user_id, images_per_user)

# Zip the data folder
zip_filename = "captured_images.zip"
zip_folder(output_folder, zip_filename)
print(f"Images saved and zipped as {zip_filename}")
