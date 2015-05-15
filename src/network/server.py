#!/usr/bin/env python2

import cv2
import socket
import sys
import time
import pygame
from P4 import * 

class MsgType(Enum):
    DATA = 1
    INTERACTION = 2

class Server(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.IP, self.port))
            self.sock.listen(1)
        except:
            sys.exit("Impossible d'initialiser le server")

    # Protocole de communication fonctionnant en 3 temps:
    # - envoi du type de message
    # - envoi de la taille
    # - envoi de la donnée
    def handle(self,msgType):
        if (msgType == MsgType.DATA):
            self.handleImg()
        elif (msgType == MsgType.INTERACTION):
            self.handleInterraction()

    def handleImg(self):
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

    def handleInterraction(self):
        pass
    
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
            while not game.isEnd():
                msgType = cnx.recv(8)
                self.handle(msgType)
            break

    def shutdown(self):
        self.sock.close()
        
def __exit__(self, type, value, traceback):
    print("exited properly")
    self.sock.close()

if __name__ == "__main__":
    serveur = Server()
    serveur.handleIm_test()
