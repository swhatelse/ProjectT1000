#!/usr/bin/env python2

import cv2
import numpy as np
import time
import Color

def nothing(x):
    pass

class Tracker(object):

    def __init__(self):
        self.frame = None
        self.trackWin = None
        self.cam = cv2.VideoCapture(0)
        self.drag = False
        self.lowH = 0
        self.lowS = 177
        self.lowV = 255
        self.highH = 91
        self.highS = 255
        self.highV = 255
        self.hist = None
        self.tracking_state = True
        
        cv2.namedWindow('image')
        cv2.namedWindow('track')
        cv2.createTrackbar('lowH','track',self.lowH,179,nothing)
        cv2.createTrackbar('lowS','track',self.lowS,255,nothing)
        cv2.createTrackbar('lowV','track',self.lowV,255,nothing)
        cv2.createTrackbar('highH','track',self.highH,179,nothing)
        cv2.createTrackbar('highS','track',self.highS,255,nothing)
        cv2.createTrackbar('highV','track',self.highV,255,nothing)

    def detectColor(self,color):
        hsv = cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv,(5,5),3);
        hsv = cv2.medianBlur(hsv,5);
        binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
        return binary

    def show_hist(self):
        bin_count = self.hist.shape[0]
        bin_w = 24
        img = np.zeros((256, bin_count*bin_w, 3), np.uint8)
        for i in xrange(bin_count):
            h = int(self.hist[i])
            cv2.rectangle(img, (i*bin_w+2, 255), ((i+1)*bin_w-2, 255-h), (int(180.0*i/bin_count), 255, 255), -1)
            img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
            cv2.imshow('hist', img)


    def detect(self):
        while True:
            self.lowH = cv2.getTrackbarPos('lowH','track')
            self.lowS = cv2.getTrackbarPos('lowS','track')
            self.lowV = cv2.getTrackbarPos('lowV','track')
            self.highH = cv2.getTrackbarPos('highH','track')
            self.highS = cv2.getTrackbarPos('highS','track')
            self.highV = cv2.getTrackbarPos('highV','track')
            color = Color.Color(self.lowH,self.lowS,self.lowV,self.highH,self.highS,self.highV)
            
            # ret, self.frame = self.cam.read()
            self.frame = cv2.imread('../../Images/P4_Lointain.jpg',1)
            height, width, depth = self.frame.shape
            
            self.trackWin = (0, 0, width, height)
            roi = self.frame[0:height, 0:width]
            
            roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(roi,color.lowHSV,color.highHSV)
            hist = cv2.calcHist([roi], [0], mask, [16], [0,180])
            cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
            self.hist = hist.reshape(-1)
            if self.tracking_state:
                prob = cv2.calcBackProject([roi], [0], self.hist, [0,180],1)
                prob &= mask
                term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
                track_box, self.trackWin = cv2.CamShift(prob, self.trackWin, term_crit)
                x,y,w,h = self.trackWin
                try: cv2.rectangle(self.frame, (x,y),(x+w, y+h),(0,255,0),2)
                except: print self.trackWin
            isolated = self.frame[y:y+h, x:x+w]
            cv2.imshow('selection', mask)
            cv2.imshow('backproj', prob)
            # print track_box
            try: cv2.imshow('isolated', isolated)
            except: print self.frame[y:y+h, x:x+w]
            self.show_hist()

            cv2.imshow('image', self.frame)

            if cv2.waitKey(30) ==  ord('q'):
                break
        cv2.destroyAllWindows()
        self.cam.release()

    def __del__(self):
        print('properly stop')
        
if __name__ == '__main__':
    tracker = Tracker()
    tracker.detect()
