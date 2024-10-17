from flask import Flask, render_template, request, session, url_for, redirect, Response
import cv2

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
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            # Draw rectangle around the faces
            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Encode the frame in JPEG format
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
