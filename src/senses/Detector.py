#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Standard imports
import cv2
import numpy as np;
import time

import tracker as tr
import Color

def nothing(x):
    pass

""" Le but de cette classe est de trouver la position de pions
    et de case du puissance 4. Il est préféreable de lui envoyer
    une image avec le P4 isolé ou en focus, pour cela, utilisez
    la class tracker """
class Detector(object):

    def __init__(self, debug = False, ksize = 25, weight = 25):
        self.params = cv2.SimpleBlobDetector_Params()
        self.params.minArea = 50
        self.detector = cv2.SimpleBlobDetector(self.params)
        self.tracker = tr.Tracker()
        self.DEBUG = debug
        self.ksize = ksize
        self.weight = weight

    """ Params img: image de la cible """
    """ Params color: utilisé pour le debug """
    def getAll(self, img, color = None):
        if color:
            blBin = Color.detectColor(img,color)
        else:
            blBin = Color.detectColor(img,Color.BLUE)
            
        if self.DEBUG:
            cv2.imshow("blBin", blBin)
            
        blKp = self.detector.detect(blBin)
        return blKp

    """ Params img: image de la cible """
    """ Params color: utilisé pour le debug """
    def getYellows(self, img, color = None):
        if color:
            binary = Color.detectColor(img,color,self.ksize,self.weight)
        else:
            binary = Color.detectColor(img,Color.YELLOW,self.ksize,self.weight)
            
        if self.DEBUG:
            cv2.imshow("ylBin", binary)
            
        kp = self.detector.detect(~binary)
        return kp

    """ Params img: image cible """
    """ Params color1: utilisé pour le debuging """
    """ Params color2: utilisé pour le debuging """
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

        blKp = self.detector.detect(~rdBin)
        return blKp
