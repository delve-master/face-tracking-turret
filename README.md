# Face-tracking turret with OpenCV and a servomotor

This repository contains the source code for controlling the servomotor based on the face detection input from a camera (I used the webcam).

The face detection (and eye detection) is achieved with OpenCV's HaarCascadeClassifier for faces (and eyes). The script will detect the face based on that and draw a square around the face to visualize the result. The locational data of the detected face will be shared with the connected Arduino board to control the servomotor's position to follow the face.

!!! Note
    This project requires an Arduino Uno (or clone), Arduino IDE, Python, and OpenCV library ready on your system.

The `face_tracking_servo_control.py` is the main script. It will throw errors if you try to run it without connecting the Arduino board to your computer and adjust the port number in the code.


## Tests
Inside the `tests` folder, there are two scripts: `face_detection.py` and `video_face_detection.py`. 

- The `face_detection.py` is for testing if the algorithm successfully detects the face for the specified source image (in the `source_img` folder). It should also detect eyes in the face as well.
  

- The `video_face_detection.py` is for testing if the camera (by default, it will be your webcam) can succesfully detect your face in real time.

