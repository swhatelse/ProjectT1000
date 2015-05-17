"""
Cette classe permet de recuperer une photos et de voir lorsque l'on appuis sur le pied de nao

"""
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import Interface_sortie as Nao_dit
import Interface_mouvement
import sys
import time

class Interface_entree:

    def __init__(self):
        self.recordFolder = "/home/nao/P4/"
        self.resolutionMap = {
            '160 x 120': 0,
            '320 x 240': 1,
            '640 x 480': 2,
            '1280 x 960': 3
        }
        self.cameraMap = {
            'Default': -1,
            'Top': 0,
            'Bottom': 1
        }
    """
        Cette methode permet de prendre une photo
        Ici les options sont fige mais il est possible de rajouter des options 
        pour gerer :la resolution,
                    la camera voulu,
                    le format de l'image,
                    ou le nom de l'image.
    """
    def Prendre_Photo(self) :#on prend une photo 
        try:
		    self.photoCapture = ALProxy( "ALPhotoCapture", "localhost", 9559)
        except:
           Nao_dit.Interface_sortie("Module 'ALPhotoCapture' not found.", "")
    
        #on force en dur les options pour les photos de notre projet.
        resolution = self.resolutionMap['1280 x 960']
        cameraID = self.cameraMap['Top']
        fileName = 'nao_pic_test'
        
        
        self.photoCapture.setResolution(resolution)
        self.photoCapture.setCameraID(cameraID)
        self.photoCapture.setPictureFormat("png")
        self.photoCapture.takePicture( self.recordFolder, fileName)


    """
        Cette methode permet d'avoir une attente active et de verifier si
        on presse sur le bumper voulu
        @Bumper doit recevoir soit : LeftBumperPressed ou RightBumperPressed pour fonctionner
        Rajout d'un compteur de tentative pour eviter de boucler a l'infini
        
    """
    def Attente_Bumper(self, Texte, Bumper):
        """
        if(Bumper != "LeftBumperPressed" or "RightBumperPressed"):
            print Bumper
            Nao_dit.Interface_sortie("Erreur d'argument du Bumper", "")            
            sys.exit(0)
        """
        if(Texte != ""):#si on a du texte on le dis
            Nao_dit.Interface_sortie(Texte, "")#on dis notre texte 
            #print Texte #on affiche notre texte dans la console
       
        self.ANSWER = 0  #la reponse finale. Si on a eu une action alors =1. Sinon il reste a 0 
        self.NB_TENTATIVE = 10 #nombre de tentative avant l'arret de l'attente (pour eviter une boucle infini)       
        self.compteur_tentative = 0 #notre compteur qui sera incremente
        self.IsTouched = False    
    
        #on lance notre brocker que l'on doit avoir pour notre evenement  
        try:     
            myBrocker = ALBroker("myBrocker", "0.0.0.0",0, "localhost", 9559)
        except:
            print("Impossible de connecter le broker")

        #on se connecte a la memoire      
        try :
            self.Mem_proxy = ALProxy("ALMemory")
        except:
            Nao_dit.Interface_sortie("Le module 'ALSensors' n'a pas etait trouve", "")     
        
         
        #on attend que le pied gauche du robot soit toucher
        try:        
            while (not self.IsTouched and self.compteur_tentative != self.NB_TENTATIVE):
                time.sleep(1) 
                if(self.Mem_proxy.getData(Bumper) != 0):#si on a toucher le bumper alors on met a 1
                    self.IsTouched = 1

                self.compteur_tentative += 1 #on incremente notre compteur de tentative
        
        except KeyboardInterrupt:#si on interromps manuellement l'action
            myBrocker.shutdown()
            try:
                Position = Interface_mouvement.Interface_mouvement()
                Position.Faire(6,20)
            except:
                Nao_dit.Interface_sortie("Je n'ai pas pu changer de position", "")
            
            sys.exit(0) #a utiliser si on veux quitter le programme complet
        
        #fin du while
        #on verifie si le while c'est fini a cause du compteur
        if(self.IsTouched and self.compteur_tentative != self.NB_TENTATIVE):
            self.ANSWER = 1
        #on ferme notre brocker
        myBrocker.shutdown()

        return self.ANSWER #on retourne notre reponse
   

   	
