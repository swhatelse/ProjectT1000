# -*- encoding: UTF-8 -*-

import Plateau
import random
import IA
import pygame
import sys
import Detector as bl
import createTable
import tracker as tr
import cv2
import Color

def choisir_colonne(x,y):
# Cette fonction retourne la colonne demandee au joueur1
# Tant que la valeur n'est pas acceptable, on demande la colonne a jouer
    col=x-16
    col=col/97
    return col
 
def erreur(s):
    print s
    
def affichage(plateau):
    #~ p.affichePlateau()
    matrice=plateau.plateau
    screen.fill((0,0,0))
    screen.blit(image,(0,0))
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            #~ print str(i)+" "+str(j)+" "+str(97.5*i)
            if matrice[i][j]==Plateau.J[1]:
                screen.blit(pionrouge,(16+97*j,13+97.5*i))
                pygame.display.flip()
            if matrice[i][j]==Plateau.J[2]:
                screen.blit(pionjaune,(16+97*j,13+97.5*i))
                pygame.display.flip()


def getTableau(imgroot):              
    tracker = tr.Tracker()
    detector = bl.Detector()
    frame = cv2.imread(imgroot,1)
    #~ clic=cv2.VideoCapture(0)
    #~ value,frame=clic.read()
    
    img, binary = tracker.detect(frame,Color.BLUE)
    #~ cv2.imshow("truc",img)
    cv2.imshow('truc', frame)
    red=detector.getReds(img)
    yel=detector.getYellows(img)
    al=detector.getAll(img)
    table=createTable.createTable(red,yel,al)
    
    return table

if __name__ == '__main__':
    ##################"
    #~ 
    #~ pygame.init ()
    #~ image = pygame.image.load ("Grille.png")
    #~ sizeim = image.get_size ()
    #~ size = (sizeim[0]*1, sizeim[1])
    #~ screen = pygame.display.set_mode (size)
    #~ screen.blit (image, (0,0))
    #~ pygame.display.flip ()
    #~ 
    #~ 
    #~ pionjaune = pygame.image.load ("PionJaune.png")
    #~ pionrouge = pygame.image.load ("PionRouge.png")
    #~ font = pygame.font.Font ("freesansbold.ttf", 15)
    ###################
    
    p=Plateau.Plateau(erreur)
    ia1=IA.IA(p)
    
    ########################################
    
    import time
     #~ 
    while(True):
        table=getTableau('../Images/P4_Lointain.jpg')
        print table.toString()
    #~ clic=False
    #~ while(not clic):
        #~ time.sleep (0.1)
        #~ pygame.display.flip ()
        #~ 
        #~ for event in pygame.event.get():
            #~ if event.type == pygame.MOUSEBUTTONUP :
                #~ x,y = pygame.mouse.get_pos()
                #~ colonne = choisir_colonne(x,y)
                #~ if(not p.colonne_remplie(colonne)):
                    #~ p.addColonne(colonne,Plateau.J[2])
                    #~ clic=True
    #~ print p.toString()

    ########################################
