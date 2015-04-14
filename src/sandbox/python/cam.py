#!/usr/bin/env python2

import cv2
import numpy as np
import time

lowH = 16
lowS = 168
lowV = 165
highH = 30
highS = 255
highV = 255

blur = 100
d = 0
rangeL = 0
rangeH = 0
k = 3
trackInited = False

class Color:
    def __init__(self, low, high):
        self.lowHSV = low
        self.highHSV = high
    def __init__(self, lowH, lowS, lowV, highH, highS, highV):
        self.lowHSV = np.array([lowH, lowS, lowV], dtype=np.uint8)
        self.highHSV = np.array([highH, highS, highV], dtype=np.uint8)

def nothing(x):
    pass

def detectColor(img, color):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv,(k,k),blur);
    hsv = cv2.medianBlur(hsv,k); 
    binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
    kernel = np.ones((5,5),np.uint8)
    binary = cv2.dilate(binary,kernel,iterations = 1)
    return binary

# Needs a binary image
def distance(binary):
    # dist = cv2.distanceTransform(binary, cv2.cv.CV_DIST_C, cv2.cv.CV_DIST_MASK_PRECISE)
    dist = cv2.distanceTransform(binary, cv2.cv.CV_DIST_L2, 5)
    dist = cv2.normalize(dist, 0.0, 1.0, cv2.NORM_MINMAX);
    return dist

def getValues():
    global blur,d,rangeL,rangeH,k,d,lowH,lowS,lowV,highH,highS,highV
    lowH = cv2.getTrackbarPos('lowH','track')
    lowS = cv2.getTrackbarPos('lowS','track')
    lowV = cv2.getTrackbarPos('lowV','track')
    highH = cv2.getTrackbarPos('highH','track')
    highS = cv2.getTrackbarPos('highS','track')
    highV = cv2.getTrackbarPos('highV','track')
    blur = cv2.getTrackbarPos('blur','track')
    d = cv2.getTrackbarPos('d','track')
    rangeL = cv2.getTrackbarPos('rangeL','track')
    rangeH = cv2.getTrackbarPos('rangeH','track')
    k = cv2.getTrackbarPos('k','track')
    if( k % 2 == 0):
        k = k + 1
    if( d % 2 == 0):
        d = d + 1
    

def trackInit(img, mask):
    hist = cv2.calcHist([img],[0],mask,[180],[0,180])
    cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)
    return hist

def track(img,mask):
    if(not trackInited):
        trackInit(img,mask)

def selectROI(event, x, y, flags, param):
    # grab the reference to the current frame, list of ROI
    # points and whether or not it is ROI selection mode
    # global frame, roiPts, inputMode
 
    # if we are in ROI selection mode, the mouse was clicked,
    # and we do not already have four points, then update the
    # list of ROI points with the (x, y) location of the click
    # and draw the circle
    if event == cv2.EVENT_LBUTTONDOWN:
        # roiPts.append((x, y))
        cv2.circle(img, (x, y), 4, (0, 255, 0), 2)
        # cv2.imshow("image", img)
        print(x)


cv2.namedWindow('track')
cv2.createTrackbar('lowH','track',0,179,nothing)
cv2.createTrackbar('lowS','track',0,255,nothing)
cv2.createTrackbar('lowV','track',0,255,nothing)
cv2.createTrackbar('highH','track',179,179,nothing)
cv2.createTrackbar('highS','track',255,255,nothing)
cv2.createTrackbar('highV','track',255,255,nothing)
cv2.createTrackbar('blur','track',0,255,nothing)
cv2.createTrackbar('k','track',3,255,nothing)
cv2.createTrackbar('d','track',0,255,nothing)
cv2.createTrackbar('rangeL','track',0,255,nothing)
cv2.createTrackbar('rangeH','track',0,255,nothing)

cap = cv2.VideoCapture(0)
# img = cv2.imread('../cam/img/Puissance4_01.svg.png',1)
# noise = cv2.imread('../cam/img/Puissance4_01.svg.png',1)
# img = cv2.imread('P4_nao.jpg',1)
# noise = cv2.imread('P4_nao.jpg',1)
# cv2.randn(noise, 1,(256,256,256));
# noise = img + noise

ret, img = cap.read()
cv2.namedWindow('image')
cv2.setMouseCallback("image", selectROI,img)

jaune = Color(16, 168, 165, 30, 255, 255)
rouge = Color(0, 230, 218, 17, 255, 255)
blue = Color(111, 124, 145, 118, 255, 255)

r,h,c,w = 250,90,400,125
track_window = (c,r,w,h)
finish = False

while (finish != True):
    ret, img = cap.read()
    getValues()
    col = Color(lowH, lowS, lowV, highH, highS, highV)
    
    binary = detectColor(img, col)
    track(img,binary)
    # dist = distance(binary)
    # ret, plateau = cv2.threshold(dist, .5, 1., cv2.cv.CV_THRESH_BINARY);
    cv2.imshow('image',img)
    cv2.imshow('binary',binary)
    # cv2.imshow('distance',dist)
    # cv2.imshow('form',plateau)

    key = cv2.waitKey(30);
    if (key == ord('q')):
        finish = True
        # cv2.imwrite('nao_bin.png', binary)
    elif(key == ord('b')):
        trackInit(img,binary)
cv2.destroyAllWindows()
