#!/usr/bin/env python2

import cv2
import numpy as np

class Detector(object):
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.surf = cv2.SURF()
        self.img = None
        self.imObject = None
        
    def run(self):
        self.img = cv2.imread('../cam/img/280px-Puissance4_01.svg.png',1)
        self.imObject = cv2.imread('jaune.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
        keyPoints, descriptors = self.surf.detect(self.imObject)
        
        while True:
            cv2.imshow('image', self.img)
            if cv2.waitKey(30) ==  ord('q'):
                break
        cv2.destroyAllWindows()
        self.cam.release()

if __name__ == '__main__':
    detector = Detector()
    detector.run()

