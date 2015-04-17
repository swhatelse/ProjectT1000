# -*- encoding: UTF-8 -*-

import Plateau
import random

class IA:
    def __init__(self,plateau):
        self.plateau=plateau
        self.ia=Plateau.J[0]
        self.profondeur=0
        
    def inverserJoueur(self,joueur):
        return Plateau.J[3-self.plateau.whois(joueur)]

    def choix_colonne(self, joueur, profondeur):
        self.ia=joueur
        self.profondeur=profondeur
        valeurMax = -10000
        valeurtmp = 0
        colonneOptimal = 6
        c = 0 
        l = 0
        colonneHasard = 0
     
        if(profondeur == 0 or self.plateau.end()):     # Si profondeur atteinte ou situationFinale (grille remplie, bot joueur gagne, adversaire gagne)
            valeurMax = self.evaluationHeuristique(joueur, profondeur)
            #~ print("valeur max = "+ str(valeurMax)+"\n")
    
        else:
            for c in range(0,self.plateau.NB_COLONNE):    # Pour chaque colonnes
                
                #~ for sp in range(self.profondeur-profondeur):
                    #~ print "-",
                #~ print c,
                if not self.plateau.colonne_remplie(c) :   # Si la colonne n'est pas pleine
                    #~ print "x-"+str(profondeur)
                    #~ print "colonne "+str(c)+" non pleine"
                    self.plateau.addColonne(c,joueur)      # simulation ajout jeton
                    valeurtmp = self.IAmin(profondeur-1, self.inverserJoueur(joueur))
                    if(valeurtmp > valeurMax):     # On veut la plus grande valeur des neuds de profondeur -1
                        valeurMax = valeurtmp
                        colonneOptimal = c
                    self.plateau.removeColonne(c)
         
        if(valeurMax == 0):
            f=True
            colonneHasard=0
            while f or self.plateau.colonne_remplie(colonneHasard):
                f=False
                colonneHasard = random.randrange(0,self.plateau.NB_COLONNE)
            colonneOptimal = colonneHasard
        #~ print "valueMax:"+str(valeurMax)
        #~ print "colonne:"+str(colonneOptimal)
        return colonneOptimal

    def IAmin(self, profondeur, joueur):
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
                        #~ print "tmp-"+str(profondeur)+" :"+str(valeurMin)
                    self.plateau.removeColonne(c)
        #~ print "min-"+str(profondeur)+" :"+str(valeurMin)
        #~ for sp in range(self.profondeur-profondeur):
            #~ print "-",
        #~ print c
        return valeurMin
                           
    def IAmax( self, profondeur, joueur):
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
        
        #~ for sp in range(self.profondeur-profondeur):
            #~ print "+",
        #~ print c
        return valeurMax

    def evaluationHeuristique(self, joueur, profondeur):
        
        valeur = 0
        win=self.plateau.winner()
        #~ print "profondeur:"+str(profondeur)
        if(win==self.ia):  # joeur 2 = bot
            valeur = 200+10*profondeur
        elif(win!=Plateau.J[0]): # joeur 1 = adversaire (une personne)
            valeur = -(100+10*profondeur)
        
        #~ if(self.plateau.end()):
            #~ print " winner in:"+str(valeur)
        return valeur

def erreur(s):
    print s    

if __name__ == '__main__':
    plateau=Plateau.Plateau(erreur)
    ia=IA(plateau)
    choix=ia.choix_colonne(1,1000)
    print choix
    plateau.addColonne(choix,1)
    plateau.affichePlateau()
    
