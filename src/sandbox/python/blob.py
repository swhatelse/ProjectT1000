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
        self.cam = cv2.VideoCapture(0)
        self.lowH = 0
        self.lowS = 177
        self.lowV = 255
        self.highH = 91
        self.highS = 255
        self.highV = 255
        
        # Set up the detector with default parameters.
        self.detector = cv2.SimpleBlobDetector()
        
        cv2.namedWindow('image')
        cv2.namedWindow('track')
        cv2.createTrackbar('lowH','track',self.lowH,179,nothing)
        cv2.createTrackbar('lowS','track',self.lowS,255,nothing)
        cv2.createTrackbar('lowV','track',self.lowV,255,nothing)
        cv2.createTrackbar('highH','track',self.highH,179,nothing)
        cv2.createTrackbar('highS','track',self.highS,255,nothing)
        cv2.createTrackbar('highV','track',self.highV,255,nothing)

    def detectColor(self,color):
        hsv = cv2.cvtColor(self.im,cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv,(5,5),3);
        hsv = cv2.medianBlur(hsv,5);
        binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
        return binary

    def run(self):
        # Read image
        self.im = cv2.imread("../../Images/puissance4.png", 1)
        # self.im = cv2.imread("../../Images/blob_test.jpg", 1)
        # self.imGray = cv2.imread("../../Images/puissance4.png", cv2.IMREAD_GRAYSCALE)
        # noise = cv2.imread('../../Images/puissance4.png',1)
        # self.im = cv2.imread("../../Images/puissance4.jpg",1)
        # tmp = self.im
 
        while True:
            # cv2.randn(noise, 1,(256,256,256));
            # self.im = tmp + noise
            # ret, self.im = self.cam.read()
            
            self.lowH = cv2.getTrackbarPos('lowH','track')
            self.lowS = cv2.getTrackbarPos('lowS','track')
            self.lowV = cv2.getTrackbarPos('lowV','track')
            self.highH = cv2.getTrackbarPos('highH','track')
            self.highS = cv2.getTrackbarPos('highS','track')
            self.highV = cv2.getTrackbarPos('highV','track')
            color = Color.Color(self.lowH,self.lowS,self.lowV,self.highH,self.highS,self.highV)

            binary = self.detectColor(color)
            
            # Detect blobs.
            keypoints = self.detector.detect(~binary)

            print(len(keypoints))
            
            # Draw detected blobs as red circles.
            # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
            im_with_keypoints = cv2.drawKeypoints(self.im, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            
            # Show keypoints
            cv2.imshow("image", im_with_keypoints)
            cv2.imshow("binary", binary)
            # cv2.imshow("noise", noise)
            for kp in keypoints:
                print(kp.pt)
                
            if cv2.waitKey(30) ==  ord('q'):
                break
            
        cv2.destroyAllWindows()

        

if __name__ == '__main__':
    blob = Blob()
    blob.run()
