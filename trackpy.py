import numpy as np
import imutils
import cv2

camera = cv2.VideoCapture('videos/green_screen.mp4')
cv2

while True:
    (grabbed, frame) = camera.read()

    # this is what grabs the next frame of the video
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    