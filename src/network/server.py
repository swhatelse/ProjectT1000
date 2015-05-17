#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import socket
import sys
import time
import pygame
from P4 import * 

class MsgType:
    DATA = 1
    INTERACTION = 2

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

    def handle(self, msgType, game, cnx):
        if (msgType == MsgType.DATA):
            self.handleImg(game, cnx)
        elif (msgType == MsgType.INTERACTION):
            self.handleInterraction(game, cnx)

    def handleImg(self, game, cnx):
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
            
            nextMove = game.nextMove("img.jpg")
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

    def run(self):
        while True:
            # waiting for a player
            cnx, addr = self.sock.accept()
            game = Game()
            self.gameContinue = True
            while not game.isEnd() and self.gameContinue:
                msgType = cnx.recv(8)
                self.handle(msgType, game, cnx)
                game.display()

    def shutdown(self):
        self.sock.close()
        
    def __exit__(self, type, value, traceback):
        print("exited properly")
        self.sock.close()

if __name__ == "__main__":
    serveur = Server()
    # serveur.handleIm_test()
