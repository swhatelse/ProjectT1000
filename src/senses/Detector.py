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
        self.ksize = 0
        self.weight = 0
        
    def getAll(self, img, color = None):
        if color:
            blBin = Color.detectColor(img,color,self.ksize,self.weight)
        else:
            blBin = Color.detectColor(img,Color.BLUE,self.ksize,self.weight)
        if self.DEBUG:
            cv2.imshow("blBin", blBin)
        blKp = self.detector.detect(blBin)
        return blKp

    def getYellows(self, img, color = None):
        if color:
            ylBin = Color.detectColor(img,color,self.ksize,self.weight)
        else:
            ylBin = Color.detectColor(img,Color.YELLOW,self.ksize,self.weight)
        if self.DEBUG:
            cv2.imshow("ylBin", ylBin)
        ylKp = self.detector.detect(ylBin)
        return ylKp

    def getReds(self, img, color1 = None, color2 = None):
        if color1 and color2:
            rdBin1 = Color.detectColor(img,color1,self.ksize,self.weight)
            rdBin2 = Color.detectColor(img,color2,self.ksize,self.weight)
        else:
            rdBin1 = Color.detectColor(img,Color.RED1,self.ksize,self.weight)
            rdBin2 = Color.detectColor(img,Color.RED2,self.ksize,self.weight)

            rdBin = cv2.bitwise_or(rdBin1, rdBin2)
        if self.DEBUG:
            cv2.imshow("rdBin", rdBin)
        blKp = self.detector.detect(rdBin)
        return blKp

    
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
            blBin = self.detectColor(img,color)
        else:
            blBin = self.detectColor(img,blue)
        ylBin = self.detectColor(img,yellow)
        rdBin1 = self.detectColor(img,red1)
        rdBin2 = self.detectColor(img,red2)

        rdBin = cv2.bitwise_or(rdBin1, rdBin2)

        # for blue, we don't need to invert
        blKp = self.detector.detect(blBin)
        ylKp = self.detector.detect(~ylBin)
        rdKp = self.detector.detect(~rdBin)

        if self.DEBUG:
            cv2.imshow("blBin", blBin)
            return blKp, ylKp, rdKp, img
        else:
            return blKp, ylKp, rdKp
    
