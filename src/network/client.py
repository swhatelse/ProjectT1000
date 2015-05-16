#!/usr/bin/env python2

import cv2
import socket
import sys
import os
from Interface_nao import *

class Client(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        self.path = '../../Images/P4_Lointain.jpg'
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.IP, self.port))

            self.entry = Interface_entree()
        except:
            sys.exit("Impossible d'initialiser le client")

    # Interroge le serveur sur le coup à jouer
    def request(self):
        length = bytes(os.path.getsize(self.path))
        # Sert à fixer la taille du message contenant la taille
        # de l'image à envoyer. Comme ça de l'autre côté on sait
        # la quantité d'octets à lire
        for i in range(8-len(length)):
            length = "0"+ length
        self.sock.send(length.encode())

        fd = open(self.path, 'rb')
        img = fd.read()
        self.sock.send(img)
        fd.close()

        # récupération du coup à jouer
        return self.sock.recv(1024)

    def handle(self):
        pass
    
    def run(self):
        # Debut de la partie
        
        while True:
            # Au tour de l'humain
            # Prise de la photo
            self.entry.Prendre_Photo()
            
            # Envoi de la demande au serveur
            move = self.request()
            
            # Indique que faire
        
            # Réaction au events
        pass
    
def __exit__(self, type, value, traceback):
    print("exited properly")
    self.sock.close()

if __name__ == "__main__":
    client = Client()
    print( client.request())
    
