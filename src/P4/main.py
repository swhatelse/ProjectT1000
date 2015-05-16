#!/usr/bin/env python2

import Plateau
import random
import IA
import pygame
import sys

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
                
if __name__ == '__main__':
    ##################"
    
    pygame.init ()
    image = pygame.image.load ("Grille.png")
    sizeim = image.get_size ()
    size = (sizeim[0]*1, sizeim[1])
    screen = pygame.display.set_mode (size)
    screen.blit (image, (0,0))
    pygame.display.flip ()
    
    
    pionjaune = pygame.image.load ("PionJaune.png")
    pionrouge = pygame.image.load ("PionRouge.png")
    font = pygame.font.Font ("freesansbold.ttf", 15)
    ###################
    
    p=Plateau.Plateau(erreur)
    ia1=IA.IA(p)
    
    ########################################
    
    import time
     #~ 
     
    r=random.randrange(0,2)
    while (not p.end()):
    #~ if (not p.end()):
        print r
        if(r==0):
        # Le joueur joue
            p.addColonne(ia1.choix_colonne(1,6),Plateau.J[1])
            affichage(p)
            if p.end():
                break
            affichage(p)
        r=0
        print "humain!"
        clic=False
        while(not clic):
            time.sleep (0.1)
            pygame.display.flip ()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP :
                    x,y = pygame.mouse.get_pos()
                    colonne = choisir_colonne(x,y)
                    if(not p.colonne_remplie(colonne)):
                        p.addColonne(colonne,Plateau.J[2])
                        clic=True
                    
        # On modifie les variables pour tenir compte du jeton depose.
                    affichage(p)
                elif event.type == pygame.QUIT:
                    clic=True
        print "plus humain"
    print "gagnant joueur:"+str(p.winner())
        
        
    print p.toString()

    ########################################
