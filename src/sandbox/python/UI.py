#!/usr/bin/env python2

import cv2
import Color
import tracker2 as tr
import blob2 as bl
import numpy as np

def nothing(x):
    pass

class UI(object):
    def __init__(self):
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.selection = None
        self.pressed = None
        self.releasedCoords = None

        self.lowH = 0
        self.lowS = 177
        self.lowV = 255
        self.highH = 91
        self.highS = 255
        self.highV = 255
        
        cv2.namedWindow('track')
        # cv2.setMouseCallback('image', self.onmouse)
        cv2.createTrackbar('lowH','track',self.lowH,255,nothing)
        cv2.createTrackbar('lowS','track',self.lowS,255,nothing)
        cv2.createTrackbar('lowV','track',self.lowV,255,nothing)
        cv2.createTrackbar('highH','track',self.highH,255,nothing)
        cv2.createTrackbar('highS','track',self.highS,255,nothing)
        cv2.createTrackbar('highV','track',self.highV,255,nothing)

    # def onmouse(self, event, x, y, flags, param):
    #     if event == cv2.EVENT_LBUTTONDOWN:
    #         self.pressed = True
    #         self.x0,self.y0 = x,y

    #     elif event == cv2.EVENT_LBUTTONUP:
    #         self.pressed = False
    #         self.drag = False
    #         self.tracking_state = True
    #         self.x1,self.y1 = x,y
    #         self.selection = (self.x0, self.y0, x, y)
    #         cv2.rectangle(self.frame,(self.x0,self.y0),(x,y),(0,255,0),2)
    #         cv2.imshow('image', self.frame)

    #     elif event == cv2.EVENT_MOUSEMOVE:
    #         if self.pressed:
    #             self.drag = True
    #             cv2.rectangle(self.frame,(self.x0,self.y0),(x,y),(0,255,0),2)
    #             cv2.imshow('image', self.frame)

    def calibrate(self):
        self.lowH = cv2.getTrackbarPos('lowH','track')
        self.lowS = cv2.getTrackbarPos('lowS','track')
        self.lowV = cv2.getTrackbarPos('lowV','track')
        self.highH = cv2.getTrackbarPos('highH','track')
        self.highS = cv2.getTrackbarPos('highS','track')
        self.highV = cv2.getTrackbarPos('highV','track')
        color = Color.Color(self.lowH,self.lowS,self.lowV,self.highH,self.highS,self.highV)
        return color

    def detectColor(self, img, color):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # hsv = cv2.GaussianBlur(hsv,(5,5),3);
        # hsv = cv2.medianBlur(hsv,5);
        binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
        return binary

    def run(self):
        tracker = tr.Tracker()
        detector = bl.Blob()

        blue = Color.Color(108,121,106,152,255,255)
        yellow = Color.Color(20,186,218,33,255,255)
        red = Color.Color(132,169,96,179,255,255)
        
        while True:
            # frame = cv2.imread('../../Images/P4_Lointain.jpg',1)
            frame = cv2.imread('../cam/img/280px-Puissance4_01.svg.png',1)

            color = self.calibrate()
            bin = self.detectColor(frame, color)
            cv2.imshow('bin', ~bin)
            
            img, binary = tracker.detect(frame,blue)
            cv2.imshow('image', img)
            # cv2.imshow('binary', ~binary)
            ylKp = detector.run(img, yellow)
            rdKp = detector.run(img, red)
            emptKp = detector.run(img, color, True)
            imKp = cv2.drawKeypoints(img, ylKp, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            imKp = cv2.drawKeypoints(imKp, rdKp, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            imKp = cv2.drawKeypoints(imKp, emptKp, np.array([]), (255,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv2.imshow('yellow', imKp)
            
            if cv2.waitKey(30) ==  ord('q'):
                break

if __name__ == '__main__':
    app = UI()
    app.run()
