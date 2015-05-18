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

def erreur(s):
    print s

# Classe d'encapsulation du jeu. 
class Game(object):
    def __init__(self, doubleIA = False):
        try:
            self.p = Plateau.Plateau(erreur)
            # self.ia1=IA.IA(self.p)
            # self.player = 1
            # self.doubleIA = doubleIA
            # # UI
            # pygame.init ()
            # self.image = pygame.image.load ("Grille.png")
            # sizeim = self.image.get_size ()
            # size = (sizeim[0]*1, sizeim[1])
            # self.screen = pygame.display.set_mode (size)
            # self.pionjaune = pygame.image.load ("PionJaune.png")
            # self.pionrouge = pygame.image.load ("PionRouge.png")
            # self.font = pygame.font.Font ("freesansbold.ttf", 15)

            self.tracker = Tr.Tracker()
            self.detector = Dr.Detector()
            
        except:
            sys.exit("Impossible d'initialiser le jeu")

    def display(self):
        matrice = self.p.plateau
        screen.fill((0,0,0))
        screen.blit(image,(0,0))
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j]==Plateau.J[1]:
                    screen.blit(pionrouge,(16+97*j,13+97.5*i))
                    pygame.display.flip()
                if self.matrice[i][j]==Plateau.J[2]:
                    screen.blit(pionjaune,(16+97*j,13+97.5*i))
                    pygame.display.flip()
            
    # def nextMove(self,path):
    #     img = cv2.imread(path)
    #     plateau = getPlateau(img)        
    #     move = self.ia1.choix_colonne(1,6),Plateau.J[1]
    #     plateau.addColonne(move)
    #     return move

    def nextMove(self,path):
        frame = cv2.imread(path)
        tracker = tr.Tracker(True)
        detector = bl.Detector(True)
        img, binary = tracker.detect(frame,Color.BLUE)

        blKp = detector.getAll(img2)
        ylKp = detector.getYellows(img2)
        rdKp = detector.getReds(img2)

        Plateau.createTable(rdKp, ylKp, blKp)

        if doubleIA:
            move = self.ia1.choix_colonne(1,6),Plateau.J[self.player]
            self.player = self.player % 2 + 1
        else:
            move = self.ia1.choix_colonne(1,6),Plateau.J[1]
        plateau.addColonne(move)
        return move

    
    def isEnd(self):
        return self.p.end()

if __name__ == "__main__":
    game = Game()
    game.nextMove()
