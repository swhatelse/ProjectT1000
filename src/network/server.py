#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import socket
import sys
import time
import pygame
import json

from P4 import Game
from network import NetUtils
from P4 import Plateau
from Global import Const

class Server(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        self.gameContinue = False
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.IP, self.port))
            self.sock.listen(1)
        except:
            sys.exit("Impossible d'initialiser le server")

    # Gère la récéption de message
    def handle(self, game, cnx):
        msgType, data = NetUtils.receive(cnx)

        if msgType == NetUtils.MSG_DATA:
            pass
        
        elif msgType == NetUtils.MSG_IMG:
            nextMove = game.nextMove(Const.ROOT_PATH + "/Images/img.png")
            print("Coup : " + str(nextMove))
            if nextMove >= 0:
                tmp = json.dumps(nextMove)
                NetUtils.send(cnx, NetUtils.MSG_DATA, len(tmp), tmp)
            else :
                NetUtils.send(cnx, NetUtils.MSG_FAILURE, 0, None)
                self.handle(game, cnx)
                
        elif msgType == NetUtils.MSG_START:
            pass
        
        elif msgType == NetUtils.MSG_HALT:
            NetUtils.send(cnx,NetUtils.MSG_HALT)

    def run(self):
        try:
            print('Démarrage du serveur')
            while True:
                print('En attente de joueur')
                cnx, addr = self.sock.accept()

                # defini le mode de jeux
                msgType, nbAI = NetUtils.receive(cnx)
                if msgType == NetUtils.MSG_START:
                    nbAI = int(nbAI.decode())
                    print("Nombre d'IA " + str(nbAI))
                    if nbAI == 2:
                        game = Game.Game(True)
                        print("Machine vs machine")
                    else:
                        game = Game.Game(False)
                        print("Man vs machine")

                    # début la partie
                    self.gameContinue = True
                    # self.gameContinue = False
                    
                while not game.isEnd() and self.gameContinue:
                    game.display()
                    self.handle(game, cnx)
                    game.display()
                    img = cv2.imread(Const.ROOT_PATH + "Images/debug.jpg")


                print('Partie terminée')
                        
        except KeyboardInterrupt:
            print("connection closed")
            cnx.shutdown(socket.SHUT_RDWR)
            cnx.close()
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()


    def shutdown(self):
        self.sock.close()
        
    def __exit__(self, type, value, traceback):
        print("exited properly")
        self.sock.close()

if __name__ == "__main__":
    server = Server()
    server.run()
