import cv2
import sys
import subprocess
from pathlib import Path
import json
import numpy


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
    frame_count = 0
    (grabbed, frame) = camera.read()
    while grabbed:
        frame_count = frame_count + 1
        if frame_count < 10:
            (grabbed, frame) = camera.read()
        else:
            break
    # allows the user to create a specfied bounding box
    # around the object of their choice
    bbox = cv2.selectROI(frame, False)

    x_axis = list()
    y_axis = list()
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
            x_axis.append(p1[0])
            y_axis.append(p1[1])
            

        #this is what plays the video
        cv2.imshow("New", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    
    cv2.destroyWindow("New")
    str_x = json.dumps(x_axis)
    str_y = json.dumps(y_axis)

    s2_out = subprocess.call("python3 graphing.py " + str_x + " " + str_y, shell=True)

    
"""
 Main of the program
"""
if __name__ == '__main__':
    filename = get_filename()
    track(filename)

