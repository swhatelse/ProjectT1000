from naoqi import ALProxy
import sys
import time
import Interface_sortie as Nao_dit
""" Cette classe permet de realiser les mouvements que nous avons enregistrer dans choregraphe
   
"""

class Interface_mouvement :


    def __init__(self) :
		#on defini la liste des mouvements possibles. Ils doivent exister dans la liste des behaviors de nao pour pouvoir etre appele		
		self.Liste_mouvement= ["P4_Position_Debut_Jeu", "P4_Position_Think", "P4_Position_Think_End", "P4_Position_Prise_Jeton", "P4_Position_Lacher_Jeton", "SitDown", "P4_Position_Fin_Jeu", "StandUp", "P4_Position_Victoire", "P4_Position_Defaite"]

    """
    @Choix_Mouvement est un numero de la liste initialiser a la creation de notre classe ci-dessus
    @Timer permet de definir un temps de pause apres nos actions.
        Attention pour les action Debut_Jeu et Fin_Jeu il faut prevoir des temps de pause suffisamment grand genre 20 sec minimum
    """
    def Faire(self, Choix_Mouvement, Timer) :
        #on commence par ce connecter au proxy
        try:
            self.postureProxy = ALProxy("ALBehaviorManager", "localhost", 9559)
            self.postureProxy.getInstalledBehaviors()
        except:
            Nao_dit.Interface_sortie("Module 'ALBehaviorManager' not found.", "")

        #on met le robot dans la posture demande
        if(self.postureProxy.isBehaviorInstalled(self.Liste_mouvement[Choix_Mouvement])):
            if(not self.postureProxy.isBehaviorRunning(self.Liste_mouvement[Choix_Mouvement])):
                self.postureProxy.post.runBehavior(self.Liste_mouvement[Choix_Mouvement])
                time.sleep(Timer)
                
            else:
                Nao_dit.Interface_sortie("Cette Action est en cours d'utilisation", "")
        else:
            Nao_dit.Interface_sortie("Cette Action n'existe pas", "")
       

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
       
