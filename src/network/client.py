#!/usr/bin/env python2

import cv2
import socket
import sys
import os

class Client(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        self.path = '../../Images/P4_Lointain.jpg'
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.IP, self.port))
        except:
            sys.exit("Impossible d'initialiser le client")

    def request(self):
        length = bytes(os.path.getsize(self.path))
        for i in range(8-len(length)):
            length = "0"+ length
        self.sock.send(length.encode())

        fd = open(self.path, 'rb')
        img = fd.read()
        self.sock.send(img)
        fd.close()

        return self.sock.recv(1024)

def __exit__(self, type, value, traceback):
    print("exited properly")
    self.sock.close()

if __name__ == "__main__":
    client = Client()
    print( client.request())
    
