#!/usr/bin/env python2

import cv2
import numpy as np
# from matplotlib import pyplot as plt

class Detector(object):
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.surf = cv2.SURF(400)
        self.img = None
        self.imObject = None
        
    def run(self):
        self.img = cv2.imread('../cam/img/280px-Puissance4_01.svg.png',1)
        self.imObject = cv2.imread('jaune.png',1)
        
        imGray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        imObjectGray = cv2.cvtColor(self.imObject,cv2.COLOR_BGR2GRAY)
        kp2, desc2 = self.surf.detectAndCompute(self.imObject,None,False)
        kp1, desc1 = self.surf.detectAndCompute(self.img,None, False)

        # # create BFMatcher object
        # bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # # Match descriptors.
        # matches = bf.match(desc2,desc1)

        # # Sort them in the order of their distance.
        # matches = sorted(matches, key = lambda x:x.distance)

        # Draw first 10 matches.
        # img3 = cv2.drawMatches(self.imObject,kp2,self.img,kp1,matches[:10], flags=2)

        # plt.imshow(img3),plt.show()
        # cv2.imshow(img3)
        

        while True:
            for k in kp1:
                x, y = k.pt
                # cv2.circle(self.img, (int(x),int(y)), 4, (0, 255, 0), 1) 

            print(len(kp2))
            self.img = cv2.drawKeypoints(self.img,kp1,None,(0,255,0),4)
                
            cv2.imshow('image', self.img)

            if cv2.waitKey(30) ==  ord('q'):
                break
        cv2.destroyAllWindows()
        self.cam.release()

if __name__ == '__main__':
    detector = Detector()
    detector.run()

