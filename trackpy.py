import numpy as np
import imutils
import cv2

camera = cv2.VideoCapture('videos/green_screen.mp4')

# grab the color green
green_lower = (29, 86, 6)
green_upper = (64, 255, 255)

while True:
    (grabbed, frame) = camera.read()


    frame = imutils.resize(frame, width=600)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # this is what grabs the next frame of the video
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    