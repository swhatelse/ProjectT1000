#!/usr/bin/env python2

import socket
import sys

from network import NetUtils

class TestUtilsSrv(object):
    def __init__(self):
        self.IP = "127.0.0.1"
        self.port = 6669
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.IP, self.port))
            self.sock.listen(1)
        except:
            sys.exit("Impossible d'initialiser le server")

    def testRecv(self):
        cnx, addr = self.sock.accept()
        msgType, data = NetUtils.receive(cnx)
        print('received')

if __name__ == "__main__":
    test = TestUtilsSrv()
    test.testRecv()
