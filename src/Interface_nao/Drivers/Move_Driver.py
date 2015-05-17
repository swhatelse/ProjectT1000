#!/usr/bin/env python2

class Interface_mouvement :
    def __init__(self) :
        self.Liste_mouvement= ["Debut_Jeu", "Think", "Think_End", "Prise_Jeton", "Lacher_Jeton", "SitDown", "Fin_Jeu", "StandUp"]

    def Faire(self, Choix_Mouvement, Timer) :
        print('Nao moves : ' + self.Liste_mouvement[Choix_Mouvement])
       
if __name__ == "__main__":
    test = Interface_mouvement()
    test.Faire(7,10)
        
	
