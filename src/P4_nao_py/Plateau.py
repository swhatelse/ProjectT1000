import Interface_sortie

"""classe gerant le plateau de jeu

*   Classe representant le plateau de jeu d'un puissance 4
*
*   Nous allons accepter uniquement les valeurs suivantes :
*       0 pour les cases vides
*       1 pour les cases prises par le joueur 1
*       2 pour les cases prises par le joueur 2
*"""


class Plateau:

    def __init__(self) :
        #define NB_LIGNE 6
        #define NB_COLONNE 7

        #define CASE_VIDE 0
        #define JETON_J1 1
        #define JETON_J2 2
        self.NB_LIGNE = 6
        self.NB_COLONNE = 7
        self.plateau_jeu = [[0 for x in range(0, self.NB_LIGNE)] for x in range(0, self.NB_COLONNE)]
        self.init_plateau()

    #getter / setteur de notre plateau
    def set_case_plateau(self, colonne, ligne, valeur) :
        #si on a une valeur superieur a 2 on a une erreur
        if valeur > 2 :
            Interface_sortie.Interface_sortie("erreur, mauvaise valeur!")
        else :
            if ligne > 5 :#si on essaye de placer dans une colonne pleine
                Interface_sortie.Interface_sortie("Cette colonne est deja pleine.")
            self.plateau_jeu[colonne][ligne] = valeur;
        #fin if
    #fin methode set_case_plateau

    def get_case_plateau(self, colonne, ligne) :
        # on renvoi la valeur de la case demande
        return self.plateau_jeu[colonne][ligne]
    #fin methode get_case_plateau

    """ on initialise notre plateau de jeu avec des 0
        pour etre sur de definir les cases vides.
    """
    def init_plateau(self) :

        for i in range (0, self.NB_COLONNE) :
            for j in range (0, self.NB_LIGNE) :
                self.plateau_jeu[i][j] = 0
            #fin for ligne
        #fin for colonne
    #fin methode init_plateau()

    def affichagePlateau(self) :  #affiche le plateau en ligne de commande
        for i in range(5, -1, -1) :
            for j in range (0, 7) :
                if (self.plateau_jeu[j][i]== 0) :
                    print " "
                if (self.plateau_jeu[j][i]== 1) :
                    print "X"
                if (self.plateau_jeu[j][i]== 2) :
                    print "O"
                print " "
            print "\n"
        #fin for
    #fin methode d'affichage du plateau pour le debug

