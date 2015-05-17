#!/usr/bin/env python2

import pygame
import sys
import cv2
import time

import senses
import IA
import Plateau

def erreur(s):
    print s

# Classe d'encapsulation du jeu. 
class Game(object):
    def __init__(self):
        try:
            self.p = Plateau.Plateau(erreur)
            self.ia=IA.IA(self.p)
            
            # UI
            pygame.init ()
            self.image = pygame.image.load ("Grille.png")
            sizeim = self.image.get_size ()
            size = (sizeim[0]*1, sizeim[1])
            self.screen = pygame.display.set_mode (size)
            self.pionjaune = pygame.image.load ("PionJaune.png")
            self.pionrouge = pygame.image.load ("PionRouge.png")
            self.font = pygame.font.Font ("freesansbold.ttf", 15)
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
            
    def nextMove(self,path):
        img = cv2.imread(path)
        plateau = getPlateau(img)        
        move = self.ia.choix_colonne(1,6),Plateau.J[1]
        plateau.addColonne(move)
        return move

    def isEnd(self):
        return self.p.end()

if __name__ == "__main__":
    game = Game()
    game.nextMove()
