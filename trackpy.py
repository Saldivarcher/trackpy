import numpy as np
import imutils
import cv2
from pathlib import Path

filename = input("Please enter the path of the video: ")
filecheck = Path(filename)

while not filecheck.is_file():
	print ("Sorry, that file doesn't exist.\n")
	filename = input("Please enter a valid path: ")
	filecheck = Path(filename)

camera = cv2.VideoCapture(filename)
# grab the color green
green_lower = (50, 110, 50)
green_upper = (255, 140, 255)
while True:
    (grabbed, frame) = camera.read()
    #print (frame[10, 10])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame, green_lower, green_upper)
    new = cv2.bitwise_and(frame, frame, mask= mask)
    # this is what grabs the next frame of the video
    cv2.imshow("Frame", frame)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Mask", mask)
    #cv2.imshow("Mask", mask)
    cv2.imshow("New", new)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    
