#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import socket
import sys
import time
import pygame

from P4 import Game
from network import NetUtils


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

    # def handle(self, msgType, game, cnx):
    #     if (msgType == MsgType.DATA):
    #         self.handleImg(game, cnx)
    #     elif (msgType == MsgType.INTERACTION):
    #         self.handleInterraction(game, cnx)

    def handle(self, game, cnx):
        msgType, data = NetUtils.receive(cnx)
        if msgType == NetUtils.MSG_DATA:
            pass
        elif msgType == NetUtils.MSG_IMG:
            nextMove = game.nextMove("/home/steven/Programmation/PATIA/NAO/ProjectT1000/src/Images/P4_Lointain.jpg")
            NetUtils.send(cnx,MSG_DATA,len(nextMove),nextMove)
        elif msgType == NetUtils.MSG_START:
            pass
        # halt
        elif msgType == -1:
            NetUtils.send(cnx,MSG_HALT)


    def handleImg(self, game, cnx):
        length = cnx.recv(8)
        length = int(length.decode())

        received = 0
        with open("/home/steven/Programmation/PATIA/NAO/ProjectT1000/src/Images/img.jpg", 'wb') as f:
            while received < length:
                print(str(received) + ' < ' + str(length)) 
                data = cnx.recv(1024)
                f.write(data)
                received += len(data)
            f.close()
            
            nextMove = game.nextMove("/home/steven/Programmation/PATIA/NAO/ProjectT1000/src/Images/img.jpg")
            cnx.send(nextMove)

    def handleInterraction(self, game, cnx):
        data = cnx.recv(1024)
        if data == "stop":
            self.gameContinue = False
    
    def handleIm_test(self):
        try:
            print("Server starts")
            cnx, addr = self.sock.accept()
            length = cnx.recv(8)
            length = int(length.decode())
            received = 0
            with open("img.jpg", 'wb') as f:
                while received < length:
                    print(str(received) + ' < ' + str(length)) 
                    data = cnx.recv(1024)
                    f.write(data)
                    received += len(data)
                    
            f.close()
            time.sleep(5)

            cnx.send("Done")
            
            self.sock.close()
            cnx.close()

        except KeyboardInterrupt:
            print("connection closed")
            self.sock.close()
            cnx.close()

    # def run(self):
    #     while True:
    #         # waiting for a player
    #         cnx, addr = self.sock.accept()
    #         game = Game()
    #         self.gameContinue = True
    #         while not game.isEnd() and self.gameContinue:
    #             msgType = cnx.recv(8)
    #             self.handle(msgType, game, cnx)
    #             game.display()
                
    def run(self):
        try:
            print('Démarrage du serveur')
            while True:
                # waiting for a player
                print('En attente de joueur')
                cnx, addr = self.sock.accept()
                msgType, nbAI = NetUtils.receive(cnx)
                nbAI = int(nbAI.decode())
                print(nbAI)
                if nbAI == 2:
                    game = Game.Game(True)
                    print("Machine vs machine")
                else:
                    game = Game.Game(False)
                    print("Man vs machine")
                    
                self.gameContinue = True
                while not game.isEnd() and self.gameContinue:
                    game.display()
                    # self.handle(game, cnx)

                        
        except KeyboardInterrupt:
            print("connection closed")
            self.sock.shutdown()
            self.sock.close()
            cnx.shutdown()
            cnx.close()


    def shutdown(self):
        self.sock.close()
        
    def __exit__(self, type, value, traceback):
        print("exited properly")
        self.sock.close()

if __name__ == "__main__":
    server = Server()
    server.run()
    # serveur.handleIm_test()
