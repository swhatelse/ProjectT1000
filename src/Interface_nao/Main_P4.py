import Interface_entree as Reception
import Interface_mouvement as Action
import Interface_sortie as Nao_dit
import IA
import random
import Plateau
import sys
import time

#initialisation des variables
Continue = 0 # a 0 si pas de reponse sinon a 1 pour savoir si on continue a jouer a la fin d'une partie


#on place nao en position de jeu
Position_nao = Action.Interface_mouvement()
Position_nao.Faire(0,40)

#on commence le jeu du puissance 4 : 
#Le joueur 1 est nao
#Le joueur 2 est le joueur adverse

def erreur(s):
    Nao_dit.Interface_sortie(s, "") 

if __name__ == '__main__':
    try:
        while(Continue == 0):
            #initialisation des variables
            Reponse_nao = Reception.Interface_entree()#Pour recuperer les infos sur nao
            Victoire_nao = 0 #Si Nao gagne alors on passe a 1 sinon c'est que c'est l'adversaire qui a gagner
            Compteur_egalite = 0 #compteur pour l'egalite
            Joueur_courant = 0 #defini le joueur en cours de jeu
            Fin_partie = False #on a pas fini notre partie
            #on designe qui doit commencer a jouer
            Joueur_courant = random.randint(1,2) #on choisis entre le joueur 1 ou le joueur 2
            #on signale le joueur qui commence
            if(Joueur_courant == 1):#si c'est nao qui commence
                Nao_dit.Interface_sortie("Je commence a jouer","") 
            else :
                Nao_dit.Interface_sortie("A vous de commencer","")
            #on cree notre plateau de jeu
            plateau = Plateau.Plateau(erreur)
            
            Compteur_egalite = 0 #on reinitialise notre compteur d'egalite
            while(not Fin_partie):#tant que ce n'est pas la fin de la partie
                if(Compteur_egalite == 42):#egalite
                    Nao_dit.Interface_sortie("Match nul","")
                    break #on arrete la boucle a ce moment la
                if(Joueur_courant == 1):#c'est nao qui joue
                    if(Compteur_egalite != 0): # pour eviter la redondance au debut du jeu
                        Nao_dit.Interface_sortie("A moi de jouer","")
                    
                   
                    #on fait jouer l'IA
                    #on met la position de reflection de nao
                    Position_nao.Faire(1,5)
                    #todo IA
                    IA_Nao = IA.IA(plateau)
                    choix_jeu = IA_Nao.choix_colonne(1,3)
                    plateau.addColonne(choix_jeu, 1)
                    #on met la position fin de reflection
                    Position_nao.Faire(2,5)
                    #on dit le coup a jouer
                    Nao_dit.Interface_sortie("Coup a jouer" + str((choix_jeu + 1)),"")
                    #on se met en position pour recevoir le jeton
                    Position_nao.Faire(3,10)
                    ready = 0
                    #on attend que l'on ai presse le pied gauche
                    while(ready == 0):
                        ready = Reponse_nao.Attente_Bumper("", "LeftBumperPressed")
                        time.sleep(1)
                    #fin while ready
                    #on lache le jeton
                    Position_nao.Faire(4,5)
                    Nao_dit.Interface_sortie("J'ai fini de jouer", "")
                    #fin du tour de nao
                else:#c'est au tour de l'humain
                    Nao_dit.Interface_sortie("A votre tour.","")
                    ok = False
                    while(not ok):
                        col = raw_input("Entrez la colonne que l'adversaire a joue :")
                        if(0 >= int(col) and int(col) <= 6):
                            ok = True                   
                    plateau.addColonne(int(col), 2)
                    plateau.affichePlateau()
                    
                    #Methode a utiliser si on a la reco visuelle
                    """
                    #on attend que l'humain est jouer
                    Joueur_humain_fin = 0
                    #on attend que l'on ai presse le pied gauche
                    while(Joueur_humain_fin == 0):
                        Joueur_humain_fin = Reponse_nao.Attente_Bumper("", "LeftBumperPressed")
                        #fin while ready 
                    
                    #Boucle d'aquisition et traitement de l'image
                    #tant que le traitement n'est pas ok on recommence
                   
                    traitement_ok = False
                    while(traitement_ok != True) :              
                        #on prend la photo
                        Reponse_nao.Prendre_Photo()
                        #on traite la photo
                        #debug
                        traitement_ok = True
                    """ 
                #fin du tour
                
                #on regarde le resultat du jeu
                Victoire_nao = plateau.winner()
                if(Victoire_nao == 1):#victoire de nao
                    Position_nao.Victoire("J'ai gagner!")
                    Fin_partie = True
                elif(Victoire_nao == 2):#victoire du joueur humain            
                    Position_nao.Defaite("")
                    Fin_partie = True
                else:
                    #on change de joueur
                    if(Joueur_courant == 1):
                        Joueur_courant = 2
                    else:
                        Joueur_courant = 1
                    #fin changement de joueur
                    Compteur_egalite += 1
            #fin de la partie
            """ On demande si la personne veut refaire une partie
                On va attendre une reponse sur le pied droit de nao ici 
                Si on le presse cela signifie qu'on arrete de jouer
                Si on ne fait rien on continue
            """
            Continue = Reponse_nao.Attente_Bumper("Voulez vous continuer", "RightBumperPressed")
            if(Continue != 0): #on arrete de jouer 
                Nao_dit.Interface_sortie("A bientot","")
            elif(Victoire_nao != 1):#Si c'est l'adversaire qui a gagner
                Nao_dit.Interface_sortie("Je vais prendre ma revanche","")
            else:
                Nao_dit.Interface_sortie("Bonne chance","")
        #fin du while Continue
        Position_nao.Faire(6,20)#on remet nao en position de securite
        
    except KeyboardInterrupt:#si on interromps manuellement l'action
        Position_nao.Faire(6,10)#on remet nao en position de securite
        sys.exit(0) #a utiliser si on veux quitter le programme complet
