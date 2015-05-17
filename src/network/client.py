#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import socket
import sys
import os
import random

from Interface_nao import *
from Interface_nao.Drivers import In_Driver as Reception
from Interface_nao.Drivers import Move_Driver as Action
from Interface_nao.Drivers import Say_Driver as Nao_dit
from network import NetUtils

class Client(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        self.path = '../../Images/P4_Lointain.jpg'
        self.inGame = False
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.entry = Reception.Interface_entree()
        except:
            sys.exit("Impossible d'initialiser le client")

    # Interroge le serveur sur le coup à jouer
    def request(self):
        # length = bytes(os.path.getsize(self.path))
        # # Sert à fixer la taille du message contenant la taille
        # # de l'image à envoyer. Comme ça de l'autre côté on sait
        # # la quantité d'octets à lire
        # for i in range(8-len(length)):
        #     length = "0"+ length
        # self.sock.send(length.encode())

        # fd = open(self.path, 'rb')
        # img = fd.read()
        # self.sock.send(img)
        # fd.close()

        # # récupération du coup à jouer
        # return self.sock.recv(1024)

        length = os.path.getsize(self.path)
        fd = open(self.path, 'rb')
        img = fd.read()
        NetUtils.send(self.sock,2,length,img)
        fd.close()

        # récupération du coup à jouer
        msgType, move = NetUtils.receive(self.sock)
        return move
        

    def naoPlays(self):
        Nao_dit.Interface_sortie("Je commence a jouer","")
        self.entry.Prendre_Photo()
        Position_nao.Faire(Positions.Think,5)
        
        # Envoi de la demande au serveur
        action = self.request()
        
        Position_nao.Faire(Positions.Think_End,5)
        Nao_dit.Interface_sortie("Coup a jouer" + str((action + 1)),"")
        Position_nao.Faire(Positions.Prise_Jeton,10)
        
        ready = 0
        #on attend que l'on ai presse le pied gauche
        while(ready == 0):
            ready = self.entry.Attente_Bumper("", "LeftBumperPressed")
            time.sleep(1)
            
            Position_nao.Faire(Positions.Lacher_Jeton,5)
            Nao_dit.Interface_sortie("J'ai fini de jouer", "")

    def humanPlays(self):
        Nao_dit.Interface_sortie("A vous de commencer","")
        human_done = False
        while not human_done:
            human_done = self.entry.Attente_Bumper("", "LeftBumperPressed")
            time.sleep(1)
    
    def run(self, doubleIA = False):
        # Debut de la partie
        while True:
            inGame = self.entry.Attente_Bumper("", "LeftBumperPressed")
            self.sock.connect((self.IP, self.port))
            
            if doubleIA:
                NetUtils.send(self.sock, 3, 1, 2)
            else:
                NetUtils.send(self.sock, 3, 1, 1)
                
            Joueur_courant = random.randint(1,2)
            while inGame:
                if(Joueur_courant == 1):
                    self.naoPlays()
                else :
                    if not doubleIA:
                        self.humanPlays()
                    else:
                        self.naoPlays()
                Joueur_courant = Joueur_courant % 2 + 1

            self.sock.shutdown()
    
    def __exit__(self, type, value, traceback):
        print("exited properly")
        self.sock.close()

if __name__ == "__main__":
    client = Client()
    client.run()
