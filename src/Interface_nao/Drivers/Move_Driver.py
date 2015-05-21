#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Interface_nao.Drivers import Say_Driver as Nao_dit
# import Interface_sortie as Nao_dit

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
        self.Liste_mouvement= ["P4_Position_Debut_Jeu", "P4_Position_Think", "P4_Position_Think_End", "P4_Position_Prise_Jeton", "P4_Position_Lacher_Jeton", "SitDown", "P4_Position_Fin_Jeu", "StandUp", "P4_Position_Victoire", "P4_Position_Defaite"]


    def Faire(self, Choix_Mouvement, Timer) :
        print('Nao moves : ' + self.Liste_mouvement[Choix_Mouvement])

    """Ici c'est la fonction en cas de victoire de nao
    @text le texte que l'on desire faire dire a nao
    On ne definie pas en option le mouvement, car on le defini en dur dans la methode    
    """
    def Victoire(self, text) :
        if text != "" :
            Nao_dit.Interface_sortie(text, "")

        self.Faire(8,30) #ici on utilise le Behaviors enregistrer pour la victoire de nao        
        
    """Ici c'est la fonction en cas de defaite de nao
    @text le texte que l'on desire faire dire a nao
    """
    def Defaite(self, text) :
        if text != "" :
            Nao_dit.Interface_sortie(text,"")
    
        self.Faire(9,30)#ici on utlise le Behaviors enregister pour la defaite de nao	

        
if __name__ == "__main__":
    test = Interface_mouvement()
    test.Faire(7,10)
        
	
