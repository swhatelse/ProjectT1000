#!/usr/bin/env python2

# Standard imports
import cv2
import numpy as np;
import time
import Color

def nothing(x):
    pass

class Blob(object):

    def __init__(self):
        # Set up the detector with default parameters.
        self.detector = cv2.SimpleBlobDetector()
        
    def detectColor(self, img, color):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv,(5,5),3);
        hsv = cv2.medianBlur(hsv,5);
        binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
        return binary

    def run(self, img, color, invert = False):
        binary = self.detectColor(img, color)
        # Detect blobs.
        if not invert:
            keypoints = self.detector.detect(~binary)
        else:
            keypoints = self.detector.detect(binary)

        infos = [ kp.pt for kp in keypoints ]

        # print(infos)
        
        return keypoints, infos
