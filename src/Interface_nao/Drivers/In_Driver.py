#!/usr/bin/env python2

import numpy as np
import os
import cv2
import time

from Global import const

class Interface_entree:

    def __init__(self):
        pass
    # Take a screenshot of the game
    def Prendre_Photo(self) :
        os.system('import -window root ' + const.ROOT_PATH + '/Images/img.jpg')

    def Attente_Bumper(self,text,Event):
        # key = raw_input(text + ' : ' )
        time.sleep(1)
        return True
        
    def Attente_senseur(self, Texte):
        pass
        
if __name__ == "__main__":
    test = Interface_entree()
    test.Attente_Bumper("Test", "iuguyf")
