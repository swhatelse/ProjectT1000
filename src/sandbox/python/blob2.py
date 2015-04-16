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

    def run(self, img, color):
        binary = self.detectColor(img, color)
            
        # Detect blobs.
        keypoints = self.detector.detect(~binary)

        print(len(keypoints))
        
        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        # Show keypoints
        # cv2.imshow("image", im_with_keypoints)
        # cv2.imshow("binary", binary)
        for kp in keypoints:
            print(kp.pt)
            
        return im_with_keypoints
    
if __name__ == '__main__':
    blob = Blob()
    blob.run()
