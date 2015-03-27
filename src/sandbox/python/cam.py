import cv2
import numpy as np
import time

lowH = 0;
lowS = 0;
lowV = 0;
highH = 180;
highS = 255;
highV = 255;

def nothing(x):
    pass

def detectColor(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    low = np.array([lowH, lowS, lowV], dtype=np.uint8)
    high = np.array([highH, highS, highV], dtype=np.uint8)
    binary = cv2.inRange(hsv, low, high)
    return binary;

# Needs a binary image
def distance(img):
    dist = cv2.distanceTransform(img,CV_DIST_C,CV_DIST_MASK_PRECISE)
    # dist = cv2.distanceTransform(img,CV_DIST_L2)
    return dist

cv2.namedWindow('binary')
cv2.createTrackbar('lowH','binary',0,180,nothing)
cv2.createTrackbar('lowS','binary',0,255,nothing)
cv2.createTrackbar('lowV','binary',0,255,nothing)
cv2.createTrackbar('highH','binary',0,180,nothing)
cv2.createTrackbar('highS','binary',0,255,nothing)
cv2.createTrackbar('highV','binary',0,255,nothing)

key = 'a'

cap = cv2.VideoCapture(0)
#img = cv2.imread('../cam/img/280px-Puissance4_01.svg.png',1);

while(key != 'q'):
    ret, img = cap.read()
    lowH = cv2.getTrackbarPos('lowH','binary')
    lowS = cv2.getTrackbarPos('lowS','binary')
    lowV = cv2.getTrackbarPos('lowV','binary')
    highH = cv2.getTrackbarPos('highH','binary')
    highS = cv2.getTrackbarPos('highS','binary')
    highV = cv2.getTrackbarPos('highV','binary')

    cv2.imshow('image',img)

    binary = detectColor(img)
    dist = distance(binary)
    cv2.imshow('binary',binary)
    cv2.imshow('distance',dist)
    
    key = cv2.waitKey(20)
    
