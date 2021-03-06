#!/usr/bin/env python2
# -*- coding: utf-8 -*-

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

""" Gère le jeu """ 
class Game(object):
    def __init__(self, doubleIA = False, difficulty = 3):
        self.player = 1
        self.doubleIA = doubleIA
        self.p = Plateau.Plateau(erreur)
        self.ia1=IA.IA(self.p)
        self.difficulty = difficulty
        # UI
        pygame.init ()

        self.image = pygame.image.load (Const.ROOT_PATH + "/Images/Grille.png")
        sizeim = self.image.get_size ()
        size = (sizeim[0]*1, sizeim[1])
        self.screen = pygame.display.set_mode (size)
        self.pionjaune = pygame.image.load (Const.ROOT_PATH +"/Images/PionJaune.png")
        self.pionrouge = pygame.image.load (Const.ROOT_PATH +"/Images/PionRouge.png")
        
        self.font = pygame.font.Font ("freesansbold.ttf", 15)
        self.tracker = Tr.Tracker()
        self.detector = Dr.Detector()

    """ Affiche le suivi du jeu par un P4 virtuel """
    def display(self):
        matrice = self.p.plateau
        self.screen.fill((0,0,0))
        self.screen.blit(self.image,(0,0))
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                if matrice[i][j]==Plateau.J[1]:
                    self.screen.blit(self.pionrouge,(16+97*j,13+97.5*i))
                if matrice[i][j]==Plateau.J[2]:
                    self.screen.blit(self.pionjaune,(16+97*j,13+97.5*i))
        pygame.display.flip()

    """ Prend en param une image et retourne la colonne a jouer et le numéro du gagnant sinon 0"""
    def nextMove(self,path):
        frame = cv2.imread(path)
        tracker = Tr.Tracker()
        detector = Dr.Detector()
        
        img, binary = tracker.detect(frame,Color.BLUE)

        blKp = detector.getAll(img)
        ylKp = detector.getYellows(img)
        rdKp = detector.getReds(img)

        grey = cv2.cvtColor(img, cv2.cv.CV_HSV2BGR);
        grey = cv2.cvtColor(grey, cv2.cv.CV_BGR2GRAY);
        
        img = cv2.drawKeypoints(img, blKp, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        img = cv2.drawKeypoints(img, ylKp, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        img = cv2.drawKeypoints(img, rdKp, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                
		# DEBUG
        # cv2.imshow("img",img)
        # while True:
        #     if cv2.waitKey(30) ==  ord('q'):
        #         break
        # cv2.imwrite(Const.ROOT_PATH + "/Images/debug.jpg", img)

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

        if self.winner() == 0:
            if self.doubleIA:
                move = self.ia1.choix_colonne(self.player,self.difficulty),Plateau.J[self.player]
                self.player = self.player % 2 + 1
            else:
                move = self.ia1.choix_colonne(1,self.difficulty),Plateau.J[1]
                
            self.p.addColonne(move[0],move[1])
            return [move[0], self.winner()]
        else:
            return [None, self.winner()]

    def winner(self):
        return int(self.p.whois(self.p.winner()))
    
    def isEnd(self):
        return self.p.end()

if __name__ == "__main__":
    game = Game()
    game.nextMove()
