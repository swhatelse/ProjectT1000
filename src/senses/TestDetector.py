#!/usr/bin/env python2

import cv2
import Color
import Detector as bl
import numpy as np
import tracker as tr

def nothing(x):
    pass

class TestDetector(object):
    def __init__(self):
        cv2.namedWindow('track')

        cv2.createTrackbar('lowH','track',0,179,nothing)
        cv2.createTrackbar('lowS','track',0,255,nothing)
        cv2.createTrackbar('lowV','track',0,255,nothing)
        cv2.createTrackbar('highH','track',179,179,nothing)
        cv2.createTrackbar('highS','track',255,255,nothing)
        cv2.createTrackbar('highV','track',255,255,nothing)
        cv2.createTrackbar('ksize','track',0,255,nothing)
        cv2.createTrackbar('weight','track',0,255,nothing)

    def calibrate(self):
        lowH = cv2.getTrackbarPos('lowH','track')
        lowS = cv2.getTrackbarPos('lowS','track')
        lowV = cv2.getTrackbarPos('lowV','track')
        highH = cv2.getTrackbarPos('highH','track')
        highS = cv2.getTrackbarPos('highS','track')
        highV = cv2.getTrackbarPos('highV','track')
        ksize = cv2.getTrackbarPos('ksize','track')
        weight = cv2.getTrackbarPos('weight','track')
        
        color = Color.Color(lowH,lowS,lowV,highH,highS,highV)

        if ksize % 2 == 0:
            ksize = ksize + 1
        
        return color, ksize, weight

    def detectColor(self, img, color):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hsv = cv2.medianBlur(hsv,5)
        binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
        cv2.imshow('bin', binary)
        return binary

    def testFindObject(self):
        detector = bl.Detector(True)
         
        while True:
            frame = cv2.imread('../Images/P4_Lointain.jpg',1)
            # frame = cv2.imread('../Images/test_P4_1.jpg',1)
            # frame = cv2.imread('../cam/img/280px-Puissance4_01.svg.png',1)
            # noise = cv2.imread('../cam/img/Puissance4_01.svg.png',1)

            noise = frame.copy()
            cv2.randn(noise, 1,(256,256,256));
            frame = frame + noise

            # color = self.calibrate()
            # binary = self.detectColor(frame, color)
            # cv2.imshow('image', frame)
            
            blKp, ylKp, rdKp, img  = detector.findObjects(frame)
            img = cv2.drawKeypoints(img, blKp, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            img = cv2.drawKeypoints(img, ylKp, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            img = cv2.drawKeypoints(img, rdKp, np.array([]), (255,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv2.imshow('img', img)
            # sort by position
            blKp = sorted(blKp, key = lambda x:x.pt)
            
            if cv2.waitKey(30) ==  ord('q'):
                break
            
            # for b in blKp: 
            #     print(b.pt)

    def testGetAll(self):
        tracker = tr.Tracker(True)
        detector = bl.Detector(True)
        frame = cv2.imread('../Images/P4_Lointain.jpg',1)
        img, binary = tracker.detect(frame,Color.BLUE)

        while True:
            noise = img.copy()
            cv2.randn(noise, 1,(256,256,256));
            # img2 = img + noise
            img2 = img

            color, detector.ksize, detector.weight = self.calibrate()
            blKp = detector.getAll(img2,color)
            # blKp = detector.getAll(img2)

            img2 = cv2.drawKeypoints(img2, blKp, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv2.imshow("noise",img2)
            cv2.imshow("detect",img2)

            if cv2.waitKey(30) ==  ord('q'):
                break

        
if __name__ == '__main__':
    app = TestDetector()
    app.testGetAll()
