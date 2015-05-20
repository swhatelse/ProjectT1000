#!/usr/bin/env python2

import socket
import sys
import os
import json

from network import NetUtils

class TestUtilsClt(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        self.path = '../../Images/P4_Lointain.jpg'
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.IP, self.port))
        except:
            sys.exit("Impossible d'initialiser le client")


    def testSend(self):
        length = bytes(os.path.getsize(self.path))
        fd = open(self.path, 'rb')
        img = fd.read()
        NetUtils.send(self.sock, 2,length,img)
        print('Sent')
        fd.close()
        
    def testSend2(self):
        NetUtils.send(self.sock, 3, 1, 2)

    def testSendTuple(self):
        data = json.dumps((2,5))
        NetUtils.send(self.sock, NetUtils.MSG_DATA, len(data), data)
    

    def stop(self):
        self.sock.shutdown()
        self.sock.close()
        
if __name__ == "__main__":
    try:
        test = TestUtilsClt()
        test.testSendTuple()
    except KeyboardInterrupt:
        test.stop()
