# -*- encoding: UTF-8 -*-

import Plateau
import random

class IA:
    """ Class contenant l'algo de résolution de type minmax """
    def __init__(self,plateau):
        """public: constructeur prenant un plateau en paramètre, qui lui permettra de faire sa résolution """
        #public
        self.plateau=plateau
        
        #private
        self.ia=Plateau.J[0]
        self.profondeur=0
        
    def inverserJoueur(self,joueur):
        """private: définit le joueur suivant"""
        return Plateau.J[3-self.plateau.whois(joueur)]

    def choix_colonne(self, joueur, profondeur):
        """public: minmax de profondeur:"profondeur" et commençant par le joueur:"joueur" """
        self.ia=joueur
        self.profondeur=profondeur
        valeurMax = -10000
        valeurtmp = 0
        colonneOptimal = 6
        c = 0 
        l = 0
        liste=[]
        colonneHasard = 0
        if(profondeur == 0 or self.plateau.end()):#cas ou le jeu est fini ou la profondeur est de 0 de base
            valeurMax = self.evaluationHeuristique(joueur, profondeur)
        else:
            for c in range(0,self.plateau.NB_COLONNE):    # Pour chaque colonnes
                if not self.plateau.colonne_remplie(c) :   # Si la colonne n'est pas pleine
                    self.plateau.addColonne(c,joueur)      # simulation ajout jeton
                    valeurtmp = self.IAmin(profondeur-1, self.inverserJoueur(joueur))
                    if(valeurtmp > valeurMax):     # On veut la plus grande valeur des neuds de profondeur -1
                        valeurMax = valeurtmp
                        liste=[c]
                        colonneOptimal = c
                    elif(valeurtmp == valeurMax):
                        liste.append(c)
                    self.plateau.removeColonne(c)
        if(len(liste)!=1):"""choix au hasard parmis les possiblités d'égales valeurs """
            print "alea"
            f=True
            colonneHasard=0
            while f or self.plateau.colonne_remplie(colonneHasard):
                f=False
                if(len(liste)>1):
                    colonneHasard = liste[random.randrange(0,len(liste))]
                else:
                    colonneHasard = random.randrange(0,self.plateau.NB_COLONNE)
            colonneOptimal = colonneHasard
        return colonneOptimal

    def IAmin(self, profondeur, joueur):
        """private: fonction min du minmax"""
        #~ print "iamin"+str(profondeur)
        valeurMin = 10000
        valeurtmp = 0
        c=0
        if(profondeur==0 or self.plateau.end()): 
            valeurMin = self.evaluationHeuristique(joueur, profondeur)
        else:
            
            for c in range(0,self.plateau.NB_COLONNE): 
                if(not self.plateau.colonne_remplie(c)):
                    self.plateau.addColonne(c,joueur)
                    valeurtmp = self.IAmax(profondeur-1, self.inverserJoueur(joueur))
                    if(valeurtmp<valeurMin):
                        valeurMin = valeurtmp
                    self.plateau.removeColonne(c)
        return valeurMin
                           
    def IAmax( self, profondeur, joueur):
        """private: fonction max du minmax"""
        
        #~ print "iamax:"+str(profondeur)
        valeurMax = -10000
        valeurtmp=0
        c=0
        if(profondeur==0 or self.plateau.end()):
               valeurMax = self.evaluationHeuristique(joueur, profondeur)
        else:
            for c in range(0,self.plateau.NB_COLONNE):
                if(not self.plateau.colonne_remplie(c)):
                    self.plateau.addColonne(c,joueur)
                    valeurtmp = self.IAmin(profondeur-1, self.inverserJoueur(joueur))
                    if(valeurtmp>valeurMax):
                        valeurMax = valeurtmp
                    self.plateau.removeColonne(c)
        return valeurMax

    def evaluationHeuristique(self, joueur, profondeur):
        """private: fonction heuristique du minmax"""
        
        valeur = 0
        win=self.plateau.winner()
        if(win==self.ia): 
            #~ print "win:"+str(win)
            valeur = 101/(self.profondeur-profondeur)
        elif(win!=Plateau.J[0]): 
            #~ print "loose:"+str(win)
            valeur = -100/(self.profondeur-profondeur)
        return valeur

def erreur(s):
    print s

if __name__ == '__main__':
    """fonction main de test de l'ia"""
    plateau=Plateau.Plateau(erreur)
    ia=IA(plateau)
    choix=ia.choix_colonne(1,1000)
    print choix
    plateau.addColonne(choix,1)
    plateau.affichePlateau()
    
