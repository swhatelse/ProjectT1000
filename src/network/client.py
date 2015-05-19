#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import socket
import sys
import os
import random
import time

from Interface_nao import *
from Interface_nao.Drivers import In_Driver as Reception
from Interface_nao.Drivers import Move_Driver as Action
from Interface_nao.Drivers import Say_Driver as Nao_dit
from network import NetUtils
from Global import const

class Client(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        self.path = const.ROOT_PATH + "/Images/img.jpg"
        self.inGame = False
        try:
            # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.entry = Reception.Interface_entree()
            self.Position_nao = Action.Interface_mouvement()
        except:
            sys.exit("Impossible d'initialiser le client")

    # Interroge le serveur sur le coup à jouer
    def request(self):
        length = os.path.getsize(self.path)
        print(length)
        fd = open(self.path, 'rb')
        img = fd.read()
        NetUtils.send(self.sock,NetUtils.MSG_IMG,length,img)
        fd.close()

    def handle(self):
        # récupération du coup à jouer
        msgType, move = NetUtils.receive(self.sock)
        print('img sent')
        return msgType, move


    def naoPlays(self):
        Nao_dit.Interface_sortie("Je commence a jouer","")
        # DEBUG
        time.sleep(1)
        self.entry.Prendre_Photo()
        self.Position_nao.Faire(Action.Think,5)
        
        # Envoi de la demande au serveur
        self.request()
        action, move = self.handle()
        
        self.Position_nao.Faire(Action.Think_End,5)

        if action == NetUtils.MSG_DATA:
            # Nao_dit.Interface_sortie("Coup a jouer" + str((move + 1)),"")
            Nao_dit.Interface_sortie("Coup a jouer" + str(int(move) + 1),"")
            self.Position_nao.Faire(Action.Prise_Jeton,10)
        
            ready = 0
            #on attend que l'on ai presse le pied gauche
            while(ready == 0):
                ready = self.entry.Attente_Bumper("", "LeftBumperPressed")
                time.sleep(1)
            
                self.Position_nao.Faire(Action.Lacher_Jeton,5)
                Nao_dit.Interface_sortie("J'ai fini de jouer", "")
        elif action == NetUtils.MSG_HALT:
            self.inGame = False

    def humanPlays(self):
        Nao_dit.Interface_sortie("A vous de commencer","")
        human_done = False
        while not human_done:
            human_done = self.entry.Attente_Bumper("", "LeftBumperPressed")
            time.sleep(1)
    
    def run(self, doubleIA = False):
        # Debut de la partie
        while True:
            self.inGame = self.entry.Attente_Bumper("", "LeftBumperPressed")
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except:
                sys.exit("Echec lors de l'ouverture du socket")
            try:
                self.sock.connect((self.IP, self.port))
            except:
                sys.exit("Echec lors de la connexion au serveur")

            # Activation du jeux IA contre IA pour test et débuggage
            if doubleIA:
                NetUtils.send(self.sock, NetUtils.MSG_START, 1, 2)
            else:
                NetUtils.send(self.sock, NetUtils.MSG_START, 1, 1)

            # TODO : choix du niveau de difficulté

            # Choix du premier joueur
            Joueur_courant = random.randint(1,2)
            while self.inGame:
                print('Début de la partie')
                if(Joueur_courant == 1):
                    self.naoPlays()
                else :
                    if not doubleIA:
                        self.humanPlays()
                    else:
                        self.naoPlays()
                # Determine le joueur suivant
                Joueur_courant = Joueur_courant % 2 + 1

            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close
            Nao_dit.Interface_sortie("Partie terminée","")

    def __exit__(self, type, value, traceback):
        print("exited properly")
        self.sock.close()

if __name__ == "__main__":
    client = Client()
    client.run(True)
