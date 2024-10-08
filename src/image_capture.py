import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error occured : Could not access the webcam.")
    exit()

while True:
    ret, frame = capture.read()

    if not ret:
        print("Error occured : Unable to capture image or video.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

