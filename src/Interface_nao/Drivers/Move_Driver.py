#!/usr/bin/env python2
# -*- coding: utf-8 -*-

Debut_Jeu = 0
Think = 1
Think_End = 2
Prise_Jeton = 3
Lacher_Jeton = 4
SitDown = 5
Fin_Jeu = 6
StandUp = 7


class Interface_mouvement :
    def __init__(self) :
        self.Liste_mouvement= ["Debut_Jeu", "Think", "Think_End", "Prise_Jeton", "Lacher_Jeton", "SitDown", "Fin_Jeu", "StandUp"]

    def Faire(self, Choix_Mouvement, Timer) :
        print('Nao moves : ' + self.Liste_mouvement[Choix_Mouvement])
       
if __name__ == "__main__":
    test = Interface_mouvement()
    test.Faire(7,10)
        
	
