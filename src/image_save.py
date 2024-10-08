import cv2
from PIL import Image
import imageio

capture = cv2.VideoCapture(0)

ret, frame = capture.read()

if ret:
    cv2.imshow("Captured Image", frame)

    cv2.imwrite("opencv_image.jpg", frame)

    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    image.save("pillow_image.png")

    imageio.imwrite("imageio_image.png", frame)

    cv2.waitKey(0)

    capture.release()
    cv2.destroyAllWindows()