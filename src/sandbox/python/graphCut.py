#!/usr/bin/env python2

import cv2
import Color
import tracker2 as tr
import blob2 as bl
import numpy as np

def nothing(x):
    pass

class GraphCut(object):
    def __init__(self):
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

    def detectColor(self, img, color):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
        # hsv = cv2.GaussianBlur(hsv,(5,5),3);
        # hsv = cv2.medianBlur(hsv,5);
        binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
        return binary

    def calibrate(self):
        self.lowH = cv2.getTrackbarPos('lowH','track')
        self.lowS = cv2.getTrackbarPos('lowS','track')
        self.lowV = cv2.getTrackbarPos('lowV','track')
        self.highH = cv2.getTrackbarPos('highH','track')
        self.highS = cv2.getTrackbarPos('highS','track')
        self.highV = cv2.getTrackbarPos('highV','track')
        color = Color.Color(self.lowH,self.lowS,self.lowV,self.highH,self.highS,self.highV)
        return color


    def select(self,img):
        red = Color.Color(132,169,96,179,255,255)
        bg =  Color.Color(136,0,0,183,255,255)
        mask = np.zeros(img.shape[:2],dtype = np.uint8)
        bgdmodel = np.zeros((1,65),np.float64)
        fgdmodel = np.zeros((1,65),np.float64)

        while True:
            color = self.calibrate()
            imFg = self.detectColor(img,red);
            imBg = self.detectColor(img,bg);

            img2 = img.copy()
            # cv2.grabCut(img2,mask,(0,0,1,1),imBg,imFg,1,cv2.GC_INIT_WITH_MASK)
            cv2.grabCut(img2,mask,(0,0,1,1),bgdmodel,fgdmodel,1,cv2.GC_INIT_WITH_MASK)
            
            cv2.imshow("fg", imFg)
            cv2.imshow("bg", imBg)
            cv2.imshow("img2", img2)
            if cv2.waitKey(30) ==  ord('q'):
                break

    
if __name__ == '__main__':
    gc = GraphCut()
    frame = cv2.imread('../../Images/P4_Lointain.jpg',1)
    gc.select(frame)

        
