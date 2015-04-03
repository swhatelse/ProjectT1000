import Plateau
import Interface_sortie
import Interface_entree
import random

class P4_nao :

    def __init__(self) :

        self.jeu_fini = False # boolean pour arreter le jeu
        self.compteur = 0 # notre compteur de coup pour verifier l'egalite
        self.gagnant = 0
        self.joueur_courant = 0
        self.Plateau = Plateau.Plateau()
        self.nbJetonsByColonne = [0 for x in range (0, 7)] #pour connaitre le nombre de jeton dans chaque colonne
        c = -1 # nbJetonsByColonne qu'on va jouer

        #on definie la difficulte de l'ordinateur
        self.iaOrdinateur = 1 # Niveau de difficulte de l'ordinateur? (1 a 10)
        Interface_sortie.Interface_sortie("Qu'elle difficulte veux tu ?")
        self.iaOrdinateur = Interface_entree.recup_diff();

        #on designe le joueur qui commence la partie
        self.joueur_courant = random.randint(1,2) #on choisis entre le joueur 1 ou le joueur 2
        Interface_sortie.Interface_sortie(str(self.joueur_courant)) #on signale le joueur qui commence


        self.compteur = 0 # compteur de tour de jeu pour connaitre le match nul

        while self.jeu_fini != True : # tant que le jeur n'est pas fini on continue de jouer

            if self.compteur == 42 :  # egalite
                self.jeu_fini = True
                self.gagnant = 0 # on met a 0 le gagnant pour eviter qu'il garde en memoire un joueur.
                Interface_sortie.Interface_sortie("Match nul")
                break #on arrete la boucle a ce moment la

            #fin if egalite
            if self.joueur_courant == 1 :
                Interface_sortie.Interface_sortie("C'est ton tour") #on demande au joueur humain de jouer

            else : #on fait jouer nao

                self.Plateau = Interface_entree.recup_Plateau()#on recupere la matrice du plateau
                Interface_sortie.Interface_sortie("Laisse-moi le temps de reflechir...")

                c3 = [0,6,5,1,2,4,3]   #c3 designe l'ordre de preference, du moins vers le plus.
                r = [0 for x in range(0,7)]
                c = -1       #  nbJetonsByColonne qu'on va jouer

                for j in range (0, 7) : # on regarde d'abord si l'ordi peut gagner en un endroit
                    if (self.nbJetonsByColonne[c3[j]] == 6) :
                        r[c3[j]]=-1;
                    else :
                        r[c3[j]] = self.IA(self.iaOrdinateur, c3[j])
                        if (r[c3[j]]==self.joueur_courant) :
                            c=c3[j]
                            break


                #   on regarde si l'ordi peut ne pas perdre
                if c == -1 :
                    for j in range (0, 7):
                        if r[c3[j]] != -1 :
                            c = c3[j]

                        Interface_sortie.Interface_sortie("Je place mon jeton dans la colonne " + str(c));


            ligne = self.nbJetonsByColonne[c];   #ligne
            self.Plateau.set_case_plateau(c, ligne, self.joueur_courant) #on met le jeton dans notre Plateau
            self.nbJetonsByColonne[c] += 1

            #on verifie si le coup est gagnant
            self.gagnant = self.Is_Victorieux(c, ligne, self.joueur_courant, self.Plateau);
            if self.gagnant != -1 :
                self.jeu_fini = True

            #on change de joueur_courant
            if (self.joueur_courant == 1) :
                self.joueur_courant = 2
            else :
                self.joueur_courant = 1

            self.compteur += 1 #on incremente le nombre de tour
        #fin du while des coups joueur

        #on donne le resultat du jeu
        if self.gagnant == 1 :
            Interface_sortie("Bravo tu m'as battu!") #le joueur 1 est le joueur humain
        elif self.gagnant == 2 :
            Interface_sortie("Perdu ! Nao t'as battu")# le joueur 2 est nao


#fin de la fonction principal
    def IA(self, I, c) :
        I -= 1;        #on descend dans la profondeur du calcul
        s=0;
        if (self.Is_Victorieux(c, self.nbJetonsByColonne[c], self.joueur_courant, self.Plateau) == -1)  :  #si ce que je joue ne me fait pas tout de suite gagner

            if I != 0 :
                r=0,l,g,h;
                l = nbJetonsByColonne[c]   #on joue le nbJetonsByColonne c
                self.Plateau.set_case_Plateau(c, l, self.joueur_courant)
                nbJetonsByColonne[c] += 1
                # changement de joueur
                if (self.joueur_courant == 1) :
                    self.joueur_courant = 2
                else :
                    self.joueur_courant = 1
                for i in range(0., 7) : # on regarde tous les coups possibles
                    if self.nbJetonsByColonne[i] == 6 :
                        r += 1
                    else :
                        g=IA(I,self.joueur_courant,self.Plateau,self.nbJetonsByColonne,i)
                        if g == self.joueur_courant :
                            s = self.joueur_courant
                        else :
                            if g != 0 :
                                r += 1

                self.joueur_courant += 1
                if self.joueur_courant == 3 :
                    self.joueur_courant = 1
                if r == 7 :
                    s = self.joueur_courant #si toutes les solutions menent a perdre...
                self.nbJetonsByColonne[c] -= 1
                self.Plateau.set_case_plateau(c, l, 0)

        else:
            s = J
        I += 1
        return s  # s prend la valeur du joueur qui gagne, 0 si personne ne gagne
    #fin methode IA

    def Is_Victorieux(self, colonne, ligne, Joueur, Plateau) :
        j = [1 for x in range (0,4 )]
        k = [1 for x in range( 0, 3)]

        for i in range(1, 4) :
            if (colonne - i) > -1 :
                if ((Plateau.get_case_plateau(colonne - i, ligne) == Joueur) & (j[0]==i)) :
                    j[0] += 1
                if ((ligne - i > -1) & (j[1]==i)) :
                    if(Plateau.get_case_plateau(colonne - i, ligne - i) == Joueur) :
                        j[1] += 1

                if ((ligne + i < 6) & (j[2]==i)) :
                    if(Plateau.get_case_plateau(colonne - i, ligne + i) == Joueur) :
                        j[2] += 1

            #fin if
            if ((ligne - i > -1) & (j[3]==i)) :
                if(Plateau.get_case_plateau(colonne, ligne - i) == Joueur) :
                    j[3] += 1

        #fin for
        for i in range (1, 4) :

            if (colonne + i < 7) :

                if ((Plateau.get_case_plateau(colonne + i, ligne) == Joueur) & (k[0]==i)) :
                    k[0] += 1
                if ((ligne - i > -1) & (k[2]==i)) :
                    if(Plateau.get_case_plateau(colonne + i, ligne - i) == Joueur) :
                        k[2] += 1
                if ((ligne + i < 6) & (k[1]==i)) :
                    if(Plateau.get_case_plateau(colonne + i, ligne + i) == Joueur) :
                        k[1] += 1

        #fin du for

        if ((k[0]+j[0]>=5) | (k[1]+j[1]>=5) | (k[2]+j[2]>=5) | (j[3]==4)) :
            return Joueur
        else :
            return -1
  #fin is victorieux
