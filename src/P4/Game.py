#!/usr/bin/env python2

import pygame
import sys
import cv2
import time

import cv2
import numpy as np

import senses
import IA
import Plateau
from senses import tracker as Tr
from senses import Detector as Dr
from senses import Color
from Global import Const

def erreur(s):
    print s

# Classe d'encapsulation du jeu. 
class Game(object):
    def __init__(self, doubleIA = False):
        self.player = 1
        self.doubleIA = doubleIA
        self.p = Plateau.Plateau(erreur)
        self.ia1=IA.IA(self.p)
        # UI
        pygame.init ()

        self.image = pygame.image.load (Const.ROOT_PATH_SRV + "/Images/Grille.png")
        sizeim = self.image.get_size ()
        size = (sizeim[0]*1, sizeim[1])
        self.screen = pygame.display.set_mode (size)
        self.pionjaune = pygame.image.load (Const.ROOT_PATH_SRV +"/Images/PionJaune.png")
        self.pionrouge = pygame.image.load (Const.ROOT_PATH_SRV +"/Images/PionRouge.png")
        
        self.font = pygame.font.Font ("freesansbold.ttf", 15)
        self.tracker = Tr.Tracker()
        self.detector = Dr.Detector()

    def display(self):
        matrice = self.p.plateau
        self.screen.fill((0,0,0))
        self.screen.blit(self.image,(0,0))
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                if matrice[i][j]==Plateau.J[1]:
                    self.screen.blit(self.pionrouge,(16+97*j,13+97.5*i))
                    # pygame.display.flip()
                if matrice[i][j]==Plateau.J[2]:
                    self.screen.blit(self.pionjaune,(16+97*j,13+97.5*i))
                    # pygame.display.flip()
        pygame.display.flip()
            
    def nextMove(self,path):
        frame = cv2.imread(path)
        tracker = Tr.Tracker()
        detector = Dr.Detector()
        
        img, binary = tracker.detect(frame,Color.BLUE)

        blKp = detector.getAll(img)
        ylKp = detector.getYellows(img)
        rdKp = detector.getReds(img)

        img = cv2.drawKeypoints(img, blKp, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        img = cv2.drawKeypoints(img, ylKp, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        img = cv2.drawKeypoints(img, rdKp, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

		#DEBUG
		#cv2.imshow("img",img)
		#while True:
		#    if cv2.waitKey(30) ==  ord('q'):
		#        break

        try :
            tmp = Plateau.createTable(rdKp, ylKp, blKp)
            if(self.p.isNext(tmp)):
                self.p = tmp
                self.ia1.plateau = tmp
            else :
                print("Erreur de coherence")
                raise Exception("Erreur de coherence")
        except :
            print("Demande d'image")
            return -1,0
            
        if self.doubleIA:
            # move = self.ia1.choix_colonne(1,6),Plateau.J[self.player]
            move = self.ia1.choix_colonne(self.player,6),Plateau.J[self.player]
            self.player = self.player % 2 + 1
        else:
            move = self.ia1.choix_colonne(1,6),Plateau.J[1]
        self.p.addColonne(move[0],move[1])
        return move

    
    def isEnd(self):
        return self.p.end()

if __name__ == "__main__":
    game = Game()
    game.nextMove()
