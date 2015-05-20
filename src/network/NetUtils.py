#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import socket
import sys
import os

from Global import Const

# Type de message
MSG_HALT = 0
MSG_DATA = 1
MSG_IMG = 2
MSG_START = 3

def encode(msg, length):
    msg = bytes(msg)
    for i in range(length-len(msg)):
        msg = "0"+ msg
    return msg

# 3 times protocole
# send type
# send size
# send msg
def send(cnx, msgType, length = 0, msg = None):
    cnx.send(encode(msgType,1))
    # cnx.send(str(msgType).ljust(1))        
    if not msg == None:
        # Encode size on 8 chars
        length = encode(length,8)
        cnx.send(length.encode())

        if not msgType == MSG_IMG:
            cnx.send(encode(msg,1))
        else:
            cnx.send(msg)

def receive(cnx):
    msgType = cnx.recv(1) #int(cnx.recv(1).decode())
    print('Msg type: ' + str(msgType))
    msgType = int(msgType.decode())
    
    if msgType == MSG_HALT:
        data = None
    elif msgType == MSG_DATA:
        length = cnx.recv(8)
        length = int(length.decode())
        data = cnx.recv(length)
    elif msgType == MSG_START:
        length = cnx.recv(8)
        length = int(length.decode())
        data = cnx.recv(length)
    else:
        length = cnx.recv(8)
        length = int(length.decode())
        received = 0
        with open(Const.ROOT_PATH_SRV +"/Images/img.jpg", 'wb') as f:
            while received < length:
                data = cnx.recv(1024)
                f.write(data)
                received += len(data)
            f.close()
        data = None

    return msgType, data    
