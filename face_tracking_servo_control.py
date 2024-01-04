""" 
Script's function: face recognition based on video streaming with laptop camera and updating servomotor's position based on the output;

In order for the script to work, you first have to connect the Arduino to your computer.
Adjust the path of CascadeClassifier and the port number of Arduino connection when necessary.
Load the turret_servo_control.ino code to your Arduino then execute this script.
"""
import cv2 as cv
import serial
import time

# cascades for face detection
face_cascade = cv.CascadeClassifier('C:\\Users\\logan\\miniconda3\\envs\\data_science\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

# open the window for video streaming
cv.namedWindow("Face detection")
cam = cv.VideoCapture(0)

# getting python-arduino connection
arduino = serial.Serial("COM5", 9600)
arduino.write(90)
time.sleep(2)
print("Connection to Arduino...")

while True:
    ret, frame = cam.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5, 10)

    for (x, y, w, h) in faces:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 69, 255), 2)
        roi_gray = gray_frame[y:y + h, x:x + w]  # slicing off the face from the image(grayscale)
        roi_color = frame[y:y + h, x:x + w]  # slicing off the face from the image(color)
        xx = int((x + (x + w)) / 2)
        yy = int((y + (y + h)) / 2)  # NOT SUPPORTED FOR MICRO SERVO
        center = (xx, yy)  # NOT SUPPORTED FOR MICRO SERVO
        pos = "X{0:d}".format(xx)
        arduino.write(pos.encode())
        print("Current position: ", xx)

    cv.imshow("Face detection", frame)
    k = cv.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

arduino.close()
cam.release()
cv.destroyAllWindows()
