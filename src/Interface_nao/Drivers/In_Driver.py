#!/usr/bin/env python2

import numpy as np
import os
import cv2


class Interface_entree:

    def __init__(self):
        pass
    # Take a screenshot of the game
    def Prendre_Photo(self) :
        os.system('import -window root ../../Images/img.jpg')

    def Attente_Bumper(self,text,Event):
        key = raw_input(text + ' : ' )
        
    def Attente_senseur(self, Texte):
        # #on attend la reponse du senseur sur le crane

        # if(Texte != "") :#si on a du texte on le dis
        #     #Interface_sortie.Interface_sortie(Texte, "")#on dis notre texte 
        #     print Texte
        # self.ANSWER = 0     
        # self.NB_TENTATIVE = 5 #nombre de tentative avant l'arret de l'attente        
        # self.compteur_tentative = 0
        # try:     
        #     myBrocker = ALBroker("myBrocker", "0.0.0.0",0, "localhost", 9559)
        # except:
        #     print("Impossible de connecter le broker")

        # ReactToTouch = ReactToTouchModule.ReactToTouchModule("ReactToTouch")
               
        # print ReactToTouch.getIsTouched()

        # #on attend que le pied gauche du robot soit toucher
        # try:        
        #     while (not ReactToTouch.getIsTouched() and self.compteur_tentative != self.NB_TENTATIVE):
        #         time.sleep(1)        
        #         self.compteur_tentative += 1 #on incremente notre compteur de tentative
        # except KeyboardInterrupt:
        #     myBrocker.shutdown()
        #     sys.exit(0)
        
        # print ReactToTouch.getIsTouched()
        # #fin du while
        # #on verifie si le while c'est fini a cause du compteur
        # if(self.compteur_tentative != self.NB_TENTATIVE):
        #     self.ANSWER = 1

        # myBrocker.shutdown()
        # return self.ANSWER
        pass
        
if __name__ == "__main__":
    test = Interface_entree()
    test.Attente_Bumper("Test", "iuguyf")
