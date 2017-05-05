import numpy as np
import imutils
import cv2
from pathlib import Path

filename = "./videos/green_screen.mp4"
filecheck = Path(filename)

if not filecheck.is_file:
    filename = input("Please enter the path of the video: ")
    filecheck = Path(filename)
    while not filecheck.is_file():
        print ("Sorry, that file doesn't exist.\n")
        filename = input("Please enter a valid path: ")
        filecheck = Path(filename)

tracker = cv2.Tracker_create("MIL")

camera = cv2.VideoCapture(filename)
# grab the color green
green_lower = (50, 110, 50)
green_upper = (255, 140, 255)


(grabbed, frame) = camera.read()

bbox = cv2.selectROI(frame, False)

grabbed = tracker.init(frame, bbox)
while True:
    (grabbed, frame) = camera.read()

    #print (frame[10, 10])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame, green_lower, green_upper)

    #this creates a border around and removes most of the background!
    frame = cv2.bitwise_and(frame, frame, mask= mask)

    grabbed, bbox = tracker.update(frame)

    if grabbed:
        p1 = (int(bbox[0])) , int(bbox[1])
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0,0,255))

    cv2.imshow("New", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    
