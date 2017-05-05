import numpy as np
import imutils
import cv2
import sys
from pathlib import Path


"""
 get_filename parses the command line arguments and will use it as a path to open 
 a video, else will open the basic given file
"""
def get_filename():
    filename = ""

    if len(sys.argv) <= 1:
        filename = "./videos/green_screen.mp4"
        filecheck = Path(filename)

    else:
        filename = sys.argv[1]
        filecheck = Path(filename)
        while not filecheck.is_file():
                print ("Sorry, that file doesn't exist.\n")
                filename = input("Please enter a valid path: ")
                filecheck = Path(filename)
    return filename



def track(filename):
    # uses the MIL tracking algorithm
    tracker = cv2.Tracker_create("MIL")

    camera = cv2.VideoCapture(filename)

    # grab the color green
    green_lower = (50, 110, 50)
    green_upper = (255, 140, 255)


    (grabbed, frame) = camera.read()

    # allows the user to create a specfied bounding box
    # around the object of their choice
    bbox = cv2.selectROI(frame, False)

    # inits the tracker algo to start
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

        #this is what plays the video
        cv2.imshow("New", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


"""
 Main of the program
"""
if __name__ == '__main__':
    filename = get_filename()
    track(filename)

