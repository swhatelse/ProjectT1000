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
    

def track():
    

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

jaune = Color(16, 168, 165, 30, 255, 255)
rouge = Color(0, 230, 218, 17, 255, 255)
blue = Color(111, 124, 145, 118, 255, 255)

r,h,c,w = 250,90,400,125
track_window = (c,r,w,h)

while True:
    ret, img = cap.read()
    getValues()
    col = Color(lowH, lowS, lowV, highH, highS, highV)
    
    binary = detectColor(img, col)
    # dist = distance(binary)
    # ret, plateau = cv2.threshold(dist, .5, 1., cv2.cv.CV_THRESH_BINARY);
    cv2.imshow('image',img)
    cv2.imshow('binary',binary)
    # cv2.imshow('distance',dist)
    # cv2.imshow('form',plateau)
    
    if ( cv2.waitKey(30) == ord('q') ):
        break
        # cv2.imwrite('nao_bin.png', binary)
cv2.destroyAllWindows()
