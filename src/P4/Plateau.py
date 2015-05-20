"""classe gerant le plateau de jeu

*   Classe representant le plateau de jeu d'un puissance 4
*
*   Nous allons accepter uniquement les valeurs suivantes :
*       J[0] pour les cases vides
*       J[1] pour les cases prises par le joueur 1
*       j[2] pour les cases prises par le joueur 2
*"""
# -*- encoding: UTF-8 -*-

import random

"""
-vide 0
-rouge 1
-jaune 2
"""
J=[0,1,2]
class Plateau:

    def __init__(self,erreur) :
        self._J=[0,1,2]
        self.NB_LIGNE = 6
        self.NB_COLONNE = 7
        self.plateau = [[self._J[0] for x in range(0, self.NB_COLONNE)] for x in range(0, self.NB_LIGNE)]
        self.erreur=erreur
        self._premier=1
    def _joueur_exist(self,joueur):
        b = False
        for i in self._J:
            b= b or (joueur==i)
        return b;
    
    def colonne_remplie(self,c):
        
        return c<0 or c>=self.NB_COLONNE or self.plateau[0][c]!=self._J[0]
    
    def _set_case_plateau(self, colonne, ligne, joueur) :
        if not self._joueur_exist(joueur):
            self.erreur("erreur, mauvaise valeur pour le joueur: "+str(joueur))
            exit
        else :
            if self._en_dehors(ligne,colonne):
                self.erreur("en dehors du tableau!")
                exit
        self.plateau[ligne][colonne] = joueur;
    
    def _en_dehors(self,ligne,colonne):
        b=False
        if ligne >=self.NB_LIGNE or ligne <0 or colonne<0 or colonne>=self.NB_COLONNE:
            b=True
        return b
        
    def addColonne(self,colonne,joueur): 
        #~ print "le joueur " + str(self.whois(joueur))+" joue en colonne "+str(colonne)
        
       
        if not self._joueur_exist(joueur):
            self.erreur("erreur, mauvaise valeur pour le joueur :"+ str(joueur))
            return
        if self._en_dehors(0,colonne):
            self.erreur("en dehors du tableau!")
            exit
        i=self.NB_LIGNE-1
        while(i>=0 and self.plateau[i][colonne]!=self._J[0]):
            i-=1
        if self._en_dehors(i,colonne) :
            self.erreur("colonne pleine")
            return
        self.plateau[i][colonne]=joueur
    
    def removeColonne(self,colonne):
        
        #~ print "suppression en colonne "+str(colonne)
        i=0
        while(i<self.NB_LIGNE and self.plateau[i][colonne]==self._J[0]):
            i+=1
        if(i!=self.NB_LIGNE):
            self.plateau[i][colonne]=self._J[0]
    
    def get_case_plateau(self, colonne, ligne) :
        if self._en_dehors(ligne,colonne):
            self.erreur("en dehors du tableau")
            exit
        return self.plateau[colonne][ligne]

    def init_plateau(self) :
        for i in range (0, self.NB_LIGNE) :
            for j in range (0, self.NB_COLONNE) :
                self.plateau[i][j] = self._J[0]

    def affichePlateau(self) : 
        print self.toString()
    
    def toString(self):
        res=""
        for i in range(0, self.NB_LIGNE) :
            res+="|"
            for j in range (0, self.NB_COLONNE) :
                if (self.plateau[i][j]== self._J[1]) :
                    res+= "X"
                elif (self.plateau[i][j]== self._J[2]) :
                    res+= "O"
                elif (self.plateau[i][j]== self._J[0]) :
                    res+= "_"
                else:
                    res+=str(self.plateau[i][j])
                res+= "|"
            res+= "\n"
        return res
    
    
    def whois(self,joueur):
        value=0
        for i,j in enumerate(self._J):
            if(joueur==j):  
                #~ print "je pense "+str(joueur)+"= "+str(j)+ " en "+str(i)
                value=i
        return value
    
    def tour(self):
        joueur=[0,0,0]
        for l in range(0,self.NB_LIGNE):
            for c in range(0,self.NB_COLONNE):
                joueur[self.whois(self.plateau[l][c])]+=1
        premier = self.whois(self._J[1])
        second = self.whois(self._J[2])
        if self._premier!=self.whois(self._J[1]) :
            premier+=second
            second=premier-second
            premier-=second
        at=premier
        if(joueur[second]<joueur[premier]):
            at=second
        self._tour=at
        
    def winner(self):
        b= False
        whithJ0=False
        winner=self._J[0]
        l=0
        while(l<self.NB_LIGNE and not b):
            c=0
            while(c<self.NB_COLONNE and not b):
                if(self.plateau[l][c]!=self._J[0]):
                    joueur=self.plateau[l][c]
                    compteur=1
                    d=1
                    #~ haut-gauche 
                    while(min(l-d,c-d)>=0 and compteur<4 and self.plateau[l-d][c-d]==joueur):
                        d+=1
                        compteur+=1
                    d=1
                    #~ bas-droite 
                    while(l+d<self.NB_LIGNE and c+d<self.NB_COLONNE and compteur<4 and self.plateau[l+d][c+d]==joueur):
                        d+=1
                        compteur+=1
                    b = b or compteur==4 
                    
                    compteur=1
                    d=1
                    #~ Haut-droite 
                    while(l-d>=0 and c+d<self.NB_COLONNE and compteur<4 and self.plateau[l-d][c+d]==joueur):
                        d+=1
                        compteur+=1
                    d=1
                    #~ bas-gauche 
                    while(l+d<self.NB_LIGNE and c-d>=0 and compteur<4 and self.plateau[l+d][c-d]==joueur):
                        d+=1
                        compteur+=1
                    b = b or compteur==4
                    
                    compteur=1
                    lp=1
                    while(l-lp>=0 and compteur<4 and self.plateau[l-lp][c]==joueur):
                        lp+=1
                        compteur+=1
                    lp=1
                    while(l+lp<self.NB_LIGNE and compteur<4 and self.plateau[l+lp][c]==joueur):
                        lp+=1
                        compteur+=1
                    b = b or compteur==4
                    
                    compteur=1
                    cp=1
                    while(c-cp>=0 and compteur<4 and self.plateau[l][c-cp]==joueur):
                        cp+=1
                        compteur+=1
                    cp=1
                    while(c+cp<self.NB_COLONNE and compteur<4 and self.plateau[l][c+cp]==joueur):
                        cp+=1
                        compteur+=1
                    b = b or compteur==4
                    
                    if(b):
                        #~ print joueur
                        winner=joueur
                else:
                    whithJ0=True
                c+=1
            l+=1
        return winner
        
    def end(self):
        return self.winner()!=self._J[0]
        
    def isNext(self, p):
        diff=0
        for colonne in range(0, self.NB_COLONNE):
            lastIsEmpty=False
            for ligne in range(self.NB_LIGNE, 0):
                if(lastIsEmpty and p.plateau[ligne][colonne]!=self._J[0]):
                    print("Jeton en vol")
                    return False
                lastIsEmpty = p.plateau[ligne][colonne] == self._J[0]
                if(self.plateau[ligne][colonne]!=p.plateau[ligne][colonne]):
                    diff+=1
                    if(diff>1):
                        print("2 coups de differences")
                        return False
        return True;
					
    def coherence(self):
        result=True
        for colonne in range(0,self.NB_COLONNE):
            ligne=self.NB_LIGNE
            flag=0
            while(ligne>0 and result):
                ligne-=1
                if(flag==0 and self.plateau[ligne][colonne]==self._J[0]):
                    flag=1
                elif(flag==1 and self.plateau[ligne][colonne]!=self._J[0]):
                    #~ self.affichePlateau()
                    result=False
        return result

def erreur(s):
    print s    

def createTable(reds, yellows, emptys):
	
    if(len(emptys)!=42) :
        print("Positions incompletes")
        raise Exception("Positions incompletes")
	
    reds = sorted(reds, key = lambda x:x.pt);
    yellows = sorted(yellows, key = lambda x:x.pt);
    emptys = sorted(emptys, key = lambda x:x.pt);

    plateau = Plateau(erreur);
    
    #~ si il existe des pions
    if(len(reds) > 0 or len(yellows) > 0):
        x = 0;
        y = 0;
        
        if len(reds) > 0 :
            rRed = reds[0].size/2
        if len(yellows) > 0 :
            rYell = yellows[0].size/2
        
        while len(emptys)>0 :
            #~ Retrait des 6 premiers puis tri sur les Y 
            #~ print "---------------------------------"
            tmp=[]
            for i in range (0,plateau.NB_LIGNE):
                if(len(emptys)>0):
                    tmp.append(emptys.pop(0));
            tmp = sorted(tmp, key = lambda x:x.pt[1]);
            x=0
            # Recherche d'un pion correspondant
            for e in tmp :
                num=-1
                red=None
                for i,r in enumerate(reds):
                    if (e.pt[0]-rRed<=r.pt[0] and e.pt[0]+rRed>=r.pt[0] 
                    and e.pt[1]-rRed<=r.pt[1] and e.pt[1]+rRed>=r.pt[1]):
                        num=i
                        red=r
                        break
                if(num>=0):
                    reds.pop(i)
                    plateau.plateau[x][y] = J[1];
                else:
                    num=-1
                    yell=None
                    for i,ye in enumerate(yellows):
                        if (e.pt[0]-rYell<=ye.pt[0] and e.pt[0]+rYell>=ye.pt[0] 
                        and e.pt[1]-rYell<=ye.pt[1] and e.pt[1]+rYell>=ye.pt[1]):
                            num=i
                            yell=ye
                            break
                    if(num>=0):
                        yellows.pop(i)
                        plateau.plateau[x][y] = J[2];
                 
                x += 1;
            y += 1;   
            
    if(len(reds)>0 or len(yellows)>0):
        print("Positions incorrectes")
        raise Exception("Positions incorrectes");
         
    return plateau;

    
if __name__ == '__main__':
    plateau=Plateau(erreur)
    plateau.affichePlateau()
    print plateau.coherence()
    plateau._set_case_plateau(0,plateau.NB_LIGNE-1,plateau._J[1])
    plateau.affichePlateau()
    print plateau.coherence()
    plateau._set_case_plateau(0,plateau.NB_LIGNE-3,plateau._J[1])
    plateau.affichePlateau()
    print plateau.coherence()
    
