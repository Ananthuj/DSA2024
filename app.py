from flask import Flask, render_template, request, session, url_for, redirect, Response
import cv2
import os
import time
app = Flask(__name__)


app.secret_key = "your_secret_key"

users = {"username": "password"}

attendance_data = {
    "2024-10-08": [
        {"id": "EMP001", "name": "Alice", "status": "Present", "in_time": "10:00"},
        {"id": "EMP007", "name": "Bob", "status": "Absent", "in_time": ""},
        {"id": "EMP005", "name": "Charlie", "status": "Present", "in_time": "09:58"},
        {"id": "EMP008", "name": "Ben", "status": "Present", "in_time": "10:00"},
        {"id": "EMP003", "name": "Ann", "status": "Absent", "in_time": ""},
        {"id": "EMP0012", "name": "Maria", "status": "Present", "in_time": "10:02"},
        {
            "id": "EMP009",
            "name": "Jayalekshmi",
            "status": "Present",
            "in_time": "09:58",
        },
        {"id": "EMP002", "name": "Shilpa", "status": "Present", "in_time": "10:20"},
        {"id": "EMP0041", "name": "Aleena", "status": "Absent", "in_time": ""},
        {"id": "EMP0023", "name": "Leena", "status": "Present", "in_time": "10:05"},
    ],
    "2024-10-09": [
        {"id": "EMP001", "name": "Alice", "status": "Absent", "in_time": ""},
        {"id": "EMP007", "name": "Bob", "status": "present", "in_time": "09:58"},
        {"id": "EMP005", "name": "Charlie", "status": "Present", "in_time": "10:00"},
    ],
}
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def generate_frames():
    cap = cv2.VideoCapture(0)

    # Folder to save captured images
    capture_folder = os.path.join(os.getcwd(), "captured_images")
    if not os.path.exists(capture_folder):
        os.makedirs(capture_folder)

    frame_count = 0  # Count frames to control the capture frequency

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            # Draw rectangles around detected faces and capture the face within the bounding box
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Capture an image every 10 frames (to avoid too many captures)
                if frame_count % 10 == 0:  # Capture every 10th frame
                    # Crop the face region from the frame (ROI: Region of Interest)
                    face_roi = frame[y:y+h, x:x+w]  # Extract only the face within the bounding box

                    # Save the cropped face image with a timestamp
                    timestamp = int(time.time())
                    image_filename = os.path.join(capture_folder, f"captured_{timestamp}.jpg")
                    cv2.imwrite(image_filename, face_roi)
                    print(f"Captured face image saved: {image_filename}")

            frame_count += 1  # Increment the frame counter

            # Encode the frame in JPEG format for video streaming
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()

            # Yield the frame for streaming
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")



@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    username = request.form["username"]
    password = request.form["password"]
    if username in users and users[username] == password:
        session["username"] = username
        return redirect(url_for("home"))
    else:
        return render_template("index.html", error="Invalid Login")
    return render_template("index.html")


@app.route("/addusr")

def addusr(max_images=100):
    # Function to get the next available user id
    def get_next_user_id():
        # Ensure the 'user_img' directory exists
        parent_folder = os.path.join(os.getcwd(), 'user_img')
        if not os.path.exists(parent_folder):
            os.makedirs(parent_folder)

        # List all existing user folders inside 'user_img'
        user_folders = [d for d in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, d)) and d.startswith('user')]
        if user_folders:
            user_numbers = [int(folder[4:]) for folder in user_folders]
            return max(user_numbers) + 1
        else:
            return 1

    # Function to create a user folder inside 'user_img'
    def create_user_folder(user_id):
        parent_folder = os.path.join(os.getcwd(), 'user_img')
        folder_name = os.path.join(parent_folder, f'user{user_id}')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        return folder_name

    # Function to capture face images from the webcam and save them
    def capture_images(user_id, max_images):
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        count = 0
        folder_name = create_user_folder(user_id)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error accessing webcam.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # For every detected face, capture and save the face image
            for (x, y, w, h) in faces:
                face_img = frame[y:y+h, x:x+w]  # Crop the face from the frame
                count += 1
                img_path = os.path.join(folder_name, f'user{user_id}_face_{count}.jpg')
                cv2.imwrite(img_path, face_img)
                print(f"Captured {img_path}")

                # Draw a rectangle around the face in the frame
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Stop if max_images has been reached
                if count >= max_images:
                    print(f"Captured {max_images} images for User{user_id}.")
                    break

            # Display the live webcam feed with the face rectangles
            cv2.imshow(f'Capturing faces for User{user_id}', frame)

            # Stop when 'q' is pressed or max_images reached
            if cv2.waitKey(1) & 0xFF == ord('q') or count >= max_images:
                break

        cap.release()
        cv2.destroyAllWindows()

    # Main logic for capturing images and returning to homepage
    user_id = get_next_user_id()
    while True:
        capture_images(user_id, max_images)
        
        # Automatically close after capturing images and redirect to the home page
        print(f"Captured images for User{user_id}. Returning to homepage.")
        
        # Redirect to the homepage
        return redirect(url_for('home'))  # Assuming you have a 'home' route

@app.route("/addemp")
def addemp():
    return render_template("addemp.html")


@app.route("/home")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"])
    return redirect(url_for("index"))


@app.route("/attendance", methods=["GET"])
def attendance():
    selected_date = request.args.get("date")
    employees = attendance_data.get(selected_date, [])

    return render_template("tbl.html", employees=employees, selected_date=selected_date)



if __name__ == "__main__":
    app.run(debug=True)
