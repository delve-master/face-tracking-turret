# This script should test if the OpenCV in your system can successfully show an image in grayscale.
import cv2

img = cv2.imread("source_img/WIN_20211027_16_33_29_Pro.jpg", 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()