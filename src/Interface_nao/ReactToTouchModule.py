from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker
import Interface_sortie
import Interface_entree
import sys
import time

class ReactToTouchModule(ALModule):

    def __init__(self, name):
              
        ALModule.__init__(self, name)
        self.Touched = False
        try :
            global Memoire_proxy
            self.Memoire_proxy = ALProxy("ALMemory")
        except:
            Interface_sortie.Interface_sortie("Le module 'ALSensors' n'a pas etait trouve", "")  
        
        self.Memoire_proxy.subscribeToEvent("LeftBumperPressed", name, "IsTouched")               
        
    def getIsTouched(self):
        return self.Touched

    def setIsTouched(self, touch):
        self.Touched = touch    

    def IsTouched(self, *_args):
        
        print value
        print key    
        print "on me touche!!!"
        
        #on recupere l'etat de nos capteur          
        #self.Memoire_proxy.unsubscribeToEvent("LeftBumperPressed","ReactToTouch")
        print self.getIsTouched()
        self.setItTouched(True)
        print self.getIsTouched()
        #self.Memoire_proxy.subscribeToEvent("LeftBumperPressed","ReactToTouch","IsTouched")
        pass
  

    
