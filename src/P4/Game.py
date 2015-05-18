#!/usr/bin/env python2

import pygame
import sys
import cv2
import time

import senses
import IA
import Plateau
from senses import tracker as Tr
from senses import Detector as Dr
from senses import Color

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
        self.image = pygame.image.load ("/home/steven/Programmation/PATIA/NAO/ProjectT1000/src/P4/Grille.png")
        sizeim = self.image.get_size ()
        size = (sizeim[0]*1, sizeim[1])
        self.screen = pygame.display.set_mode (size)
        self.pionjaune = pygame.image.load ("/home/steven/Programmation/PATIA/NAO/ProjectT1000/src/P4/PionJaune.png")
        self.pionrouge = pygame.image.load ("/home/steven/Programmation/PATIA/NAO/ProjectT1000/src/P4/PionRouge.png")
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
                    pygame.display.flip()
                if matrice[i][j]==Plateau.J[2]:
                    self.screen.blit(self.pionjaune,(16+97*j,13+97.5*i))
                    pygame.display.flip()
            
    # def nextMove(self,path):
    #     img = cv2.imread(path)
    #     plateau = getPlateau(img)        
    #     move = self.ia1.choix_colonne(1,6),Plateau.J[1]
    #     plateau.addColonne(move)
    #     return move

    def nextMove(self,path):
        frame = cv2.imread(path)
        tracker = Tr.Tracker(True)
        detector = Dr.Detector(True)
        img, binary = tracker.detect(frame,Color.BLUE)

        blKp = detector.getAll(img)
        ylKp = detector.getYellows(img)
        rdKp = detector.getReds(img)

        self.p = Plateau.createTable(rdKp, ylKp, blKp)

        if doubleIA:
            move = self.ia1.choix_colonne(1,6),Plateau.J[self.player]
            self.player = self.player % 2 + 1
        else:
            move = self.ia1.choix_colonne(1,6),Plateau.J[1]
        self.p.addColonne(move)
        return move

    
    def isEnd(self):
        return self.p.end()

if __name__ == "__main__":
    game = Game()
    game.nextMove()
