#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import socket
import sys
import os
import random
import time
import json

# from Interface_nao.Drivers import In_Driver as Reception
# from Interface_nao.Drivers import Move_Driver as Action
# from Interface_nao.Drivers import Say_Driver as Nao_dit

from Interface_nao import Interface_entree as Reception
from Interface_nao import Interface_mouvement as Action
from Interface_nao import Interface_sortie as Nao_dit

# from network import NetUtils
# from Global import Const

import NetUtils
import Const


class Client(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        self.path = Const.ROOT_PATH + "/Images/img.png"
        self.inGame = False
        try:
            self.entry = Reception.Interface_entree()
            self.Position_nao = Action.Interface_mouvement()
        except:
            sys.exit("Impossible d'initialiser le client")

    # Interroge le serveur sur le coup à jouer
    def request(self):
        length = os.path.getsize(self.path)
        fd = open(self.path, 'rb')
        img = fd.read()
        print("Envoi de l'image au serveur")
        NetUtils.send(self.sock,NetUtils.MSG_IMG,length,img)
        fd.close()
        # récupération du coup à jouer
        print("Attente de la réponse du serveur")
        msgType, move = NetUtils.receive(self.sock)
        return msgType, move

    def naoPlays(self):
        # DEBUG
        time.sleep(0.1)
        self.entry.Prendre_Photo()
        self.Position_nao.Faire(Action.Think,5)
        
        # Envoi de la demande au serveur
        action, result = self.request()
        result = json.loads(result)
        move = result[0]
        winner = result[1]
        print("Réponse reçu:")
        print("Action :" + str(action))
        print("Move : " + str(move))
        
        self.Position_nao.Faire(Action.Think_End,5)
        
        if action == NetUtils.MSG_DATA:
            if not move == None:
                Nao_dit.Interface_sortie("Coup a jouer en " + str(int(move) + 1),"")
                self.Position_nao.Faire(Action.Prise_Jeton,10)
        
                ready = 0
                #on attend que l'on ai presse le pied gauche
                while(ready == 0):
                    ready = self.entry.Attente_Bumper("", "LeftBumperPressed")
                    time.sleep(0.02)
            
                    self.Position_nao.Faire(Action.Lacher_Jeton,5)
                    Nao_dit.Interface_sortie("J'ai fini de jouer", "")

            if not result[1] == 0:
                self.inGame = False
                if(result[1] == 1):#victoire de nao
                    self.Position_nao.Victoire("J'ai gagner!")
                elif(result[1] == 2):#victoire du joueur humain            
                    self.Position_nao.Defaite("Oh non! Je crois que nous avons un champion!")
                
        elif action == NetUtils.MSG_FAILURE:
            self.naoPlays()
            
    def naoFirstPlays(self):
        Nao_dit.Interface_sortie("Je commence a jouer","")
        self.naoPlays()
        
    def humanPlays(self):
        Nao_dit.Interface_sortie("A votre tour","")
        while(not self.entry.Attente_Bumper("", "LeftBumperPressed") == 1):
            time.sleep(1)
 
    
    def run(self, doubleIA = False):
        # Debut de la partie
        while True:
            while(not self.entry.Attente_Bumper("", "LeftBumperPressed") == 1):
                pass 
            self.inGame = True
            
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except:
                self.Position_nao.Faire(6,20)
                sys.exit("Echec lors de l'ouverture du socket")
            try:
                self.sock.connect((self.IP, self.port))
            except:
                self.Position_nao.Faire(6,20)
                sys.exit("Echec lors de la connexion au serveur")

            # Activation du jeux IA contre IA pour test et débuggage
            if doubleIA:
                print("IA VS IA")
                NetUtils.send(self.sock, NetUtils.MSG_START, 1, 2)
            else:
                print("Humain VS IA")
                NetUtils.send(self.sock, NetUtils.MSG_START, 1, 1)

            # Choix du premier joueur
            Joueur_courant = random.randint(1,2)
            #print("Le joueur " + str(Joueur_courant) + " commence")
            if(Joueur_courant == 1):
                Nao_dit.Interface_sortie("Je commence la partie", "")
            else:
                Nao_dit.Interface_sortie("Vous commencez", "")
            #time.sleep(10)
            #Nao_dit.Interface_sortie("Let's rock baby!","")

            
            while self.inGame:
                if(Joueur_courant == 1):
                    self.naoFirstPlays()
                else :
                    if not doubleIA:
                        self.humanPlays()
                    else:
                        self.naoPlays()
                # Determine le joueur suivant
                Joueur_courant = Joueur_courant % 2 + 1

            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            Nao_dit.Interface_sortie("Partie terminée","")
            break

    def __exit__(self, type, value, traceback):
        print("exited properly")
        self.sock.close()

if __name__ == "__main__":
    client = Client()
    # client.run(True)
    client.run(False)
