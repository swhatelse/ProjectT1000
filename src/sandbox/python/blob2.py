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
        self.params = cv2.SimpleBlobDetector_Params()
        self.params.minArea = 50
        self.detector = cv2.SimpleBlobDetector(self.params)
        
    def detectColor(self, img, color):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # hsv = cv2.GaussianBlur(hsv,(5,5),0)
        hsv = cv2.medianBlur(hsv,5)
        binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
        return binary

    def run(self, img, color, invert = False):
        binary = self.detectColor(img, color)

        if not invert:
            keypoints = self.detector.detect(~binary)
        else:
            keypoints = self.detector.detect(binary)

        infos = [ kp.pt for kp in keypoints ]

        print(len(keypoints))
        
        return keypoints, infos

    def findObjects(self,img, color = None):
        # blue = Color.Color(101,117,59,131,255,255)
        blue = Color.Color(104,75,46,151,255,255)
        yellow = Color.Color(20,182,183,40,255,255)
        red1 = Color.Color(0,168,100,6,255,255)
        red2 = Color.Color(123,168,97,179,255,255)

        if color:
            blBin = self.detectColor(img,color);
        else:
            blBin = self.detectColor(img,blue);
        ylBin = self.detectColor(img,yellow);
        rdBin1 = self.detectColor(img,red1);
        rdBin2 = self.detectColor(img,red2);

        rdBin = cv2.bitwise_or(rdBin1, rdBin2);
        # blBin = cv2.absdiff(blBin,rdBin)
        
        blKp = self.detector.detect(blBin);
        ylKp = self.detector.detect(~ylBin);
        rdKp = self.detector.detect(~rdBin);

        return blKp, ylKp, rdKp
    
if __name__ == '__main__':
    blob = Blob()
    blob.run()
