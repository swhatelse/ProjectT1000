#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import cv2

""" Sert à définir une plage de couleur en HSV """
class Color(object):
    def __init__(self, low, high):
        self.lowHSV = low
        self.highHSV = high
    def __init__(self, lowH, lowS, lowV, highH, highS, highV):
        self.lowHSV = np.array([lowH, lowS, lowV], dtype=np.uint8)
        self.highHSV = np.array([highH, highS, highV], dtype=np.uint8)

def detectColor(img, color, ksize = None, weight = None):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
    if ksize and weight:
        blur = cv2.GaussianBlur(binary,(ksize,ksize), weight)
    else:
        blur = cv2.GaussianBlur(binary,(25,25), 25)
    return blur

# Constantes
BLUE = Color(104,75,46,151,255,255)
# BLUE = Color(91,138,157,130,255,255)
YELLOW = Color(20,182,183,40,255,255)
RED1 = Color(0,168,100,6,255,255)
RED2 = Color(123,168,97,179,255,255)
