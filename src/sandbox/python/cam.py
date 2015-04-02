import cv2
import numpy as np
import time

# lowH = 154;
# lowS = 153;
# lowV = 145;
# highH = 180;
# highS = 255;
# highV = 255;

# Jaune
lowH = 16;
lowS = 168;
lowV = 165;
highH = 30;
highS = 255;
highV = 255;

# Rouge
# lowH = 16;
# lowS = 168;
# lowV = 165;
# highH = 30;
# highS = 255;
# highV = 255;

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
    hsv = cv2.medianBlur(hsv,9);
    binary = cv2.inRange(hsv, color.lowHSV, color.highHSV)
    return binary


# Needs a binary image
def distance(binary):
    # dist = cv2.distanceTransform(binary, cv2.cv.CV_DIST_C, cv2.cv.CV_DIST_MASK_PRECISE)
    dist = cv2.distanceTransform(binary, cv2.cv.CV_DIST_L2, 5)
    dist = cv2.normalize(dist, 0, 50, cv2.NORM_MINMAX);
    return dist

cv2.namedWindow('binary')
cv2.createTrackbar('lowH','binary',0,179,nothing)
cv2.createTrackbar('lowS','binary',0,255,nothing)
cv2.createTrackbar('lowV','binary',0,255,nothing)
cv2.createTrackbar('highH','binary',0,179,nothing)
cv2.createTrackbar('highS','binary',0,255,nothing)
cv2.createTrackbar('highV','binary',0,255,nothing)

key = 'a'

cap = cv2.VideoCapture(0)
# img = cv2.imread('../cam/img/280px-Puissance4_01.svg.png',1)
jaune = Color(16, 168, 165, 30, 255, 255)

while(key != ord('q')):
    ret, img = cap.read()
    lowH = cv2.getTrackbarPos('lowH','binary')
    lowS = cv2.getTrackbarPos('lowS','binary')
    lowV = cv2.getTrackbarPos('lowV','binary')
    highH = cv2.getTrackbarPos('highH','binary')
    highS = cv2.getTrackbarPos('highS','binary')
    highV = cv2.getTrackbarPos('highV','binary')

    blanc = Color(lowH, lowS, lowV, highH, highS, highV)
    cv2.imshow('image',img)
    
    binary = detectColor(img, blanc)
    dist = distance(binary)
    ret, plateau = cv2.threshold(dist, 0, 255, cv2.cv.CV_THRESH_BINARY);
    cv2.imshow('binary',binary)
    cv2.imshow('distance',dist)
    cv2.imshow('form',plateau)
    
    key = cv2.waitKey(30)
    
