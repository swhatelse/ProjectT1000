from naoqi import ALProxy
import sys
import time
import Interface_sortie
""" Cette classe permet de realiser les mouvements que nous avons enregistrer dans choregraphe
"""

class Interface_mouvement :

        def __init__(self) :
		#on defini la liste des mouvements possibles		
		self.Liste_mouvement= ["P4_Position_Debut_Jeu", "P4_Position_Think", "P4_Position_Think_End", "P4_Position_Prise_Jeton", "P4_Position_Lacher_Jeton", "SitDown"]

	

	def Faire(self, Choix_Mouvement) :
		#on commence par ce connecter au proxy
		try:
			postureProxy = ALProxy("ALBehaviorManager", "localhost", 9559)
			postureProxy.getInstalledBehaviors()
		except:
			Interface_sortie.Interface_sortie("Module 'ALBehaviorManager' not found.")

		#on met le robot dans la posture demande
		if(postureProxy.isBehaviorInstalled(self.Liste_mouvement[Choix_Mouvement])):
			if(not postureProxy.isBehaviorRunning(self.Liste_mouvement[Choix_Mouvement])):
				postureProxy.post.runBehavior(self.Liste_mouvement[Choix_Mouvement])
				time.sleep(1.5)
			else:
				Interface_sortie.Interface_sortie("Cette posture est en cours d'utilisation")
		else :
			Interface_sortie.Interface_sortie("Cette posture n'existe pas")
	
