import cv2
import numpy as np

camera = cv2.VideoCapture('videos/green_screen.mp4')

while True:
    (grabbed, frame) = camera.read()
    