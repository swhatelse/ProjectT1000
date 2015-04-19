#!/usr/bin/env python2

# Standard imports
import cv2
import numpy as np;
import time
import tracker as tr
import Color

def nothing(x):
    pass

class Detector(object):

    def __init__(self, debug = False):
        self.params = cv2.SimpleBlobDetector_Params()
        self.params.minArea = 50
        self.detector = cv2.SimpleBlobDetector(self.params)
        self.tracker = tr.Tracker()
        self.DEBUG = debug
        
    def detectColor(self, img, color):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        blur = cv2.medianBlur(hsv,5)
        binary = cv2.inRange(blur, color.lowHSV, color.highHSV)
        return binary

    # Return sets of keypoint for plateau and yellow and red pions
    # it also returns the image in debug mode on which the algo as
    # worked on
    def findObjects(self, img, color = None):        
        blue = Color.Color(104,75,46,151,255,255)
        yellow = Color.Color(20,182,183,40,255,255)
        red1 = Color.Color(0,168,100,6,255,255)
        red2 = Color.Color(123,168,97,179,255,255)

        # isolate plateau
        if self.DEBUG:
            self.tracker = tr.Tracker(True)
        else:
            self.tracker = tr.Tracker()
        img, binary = self.tracker.detect(img,blue)

        if color:
            blBin = self.detectColor(img,color);
        else:
            blBin = self.detectColor(img,blue);
        ylBin = self.detectColor(img,yellow);
        rdBin1 = self.detectColor(img,red1);
        rdBin2 = self.detectColor(img,red2);

        rdBin = cv2.bitwise_or(rdBin1, rdBin2);

        # for blue, we don't need to invert
        blKp = self.detector.detect(blBin);
        ylKp = self.detector.detect(~ylBin);
        rdKp = self.detector.detect(~rdBin);

        if self.DEBUG:
            return blKp, ylKp, rdKp, img
        else:
            return blKp, ylKp, rdKp
    
