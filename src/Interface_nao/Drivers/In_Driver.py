#!/usr/bin/env python2

import numpy as np
import os
import cv2
import time

from Global import Const

class Interface_entree:

    def __init__(self):
        pass
    # Take a screenshot of the game
    def Prendre_Photo(self) :
        os.system('import -window root ' + Const.ROOT_PATH + '/Images/img.png')

    def Attente_Bumper(self,text,Event):
        # key = raw_input(text + ' : ' )
        return True
        
    def Attente_senseur(self, Texte):
        pass
        
if __name__ == "__main__":
    test = Interface_entree()
    test.Attente_Bumper("Test", "iuguyf")
