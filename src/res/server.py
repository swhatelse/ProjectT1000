#!/usr/bin/python
import socket
import cv2
import numpy
<<<<<<< HEAD
=======
from random import *
import ResValue 
>>>>>>> mehdi

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = 'localhost'
TCP_PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
conn, addr = s.accept()

TCP_IP_client = 'localhost'
TCP_PORT_client = 5002

sock = socket.socket()
sock.connect((TCP_IP_client, TCP_PORT_client))
<<<<<<< HEAD

while(True):
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    
    
    decimg=cv2.imdecode(data,1)
    cv2.imshow('SERVER',decimg)
    
    
    #~ --
    
    
    #~ capture = cv2.VideoCapture(0)
    #~ ret, frame = capture.read()
    
    #~ encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    #~ result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    #~ data = numpy.array(imgencode)
    #~ stringData = data.tostring()
    stringData=str(1)
=======
colonne=0;
while(True):
#~ while(colonne!=ResValue.V.Fin):
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
   
     
    
    #~ --
    colonne=int(random()*20 -11)
    stringData=str(colonne)
>>>>>>> mehdi
    
    sock.send( str(len(stringData)).ljust(16));
    print stringData
    sock.send( stringData );
<<<<<<< HEAD
    cv2.imshow('CLIENT',decimg)
=======
    
    decimg=cv2.imdecode(data,1) 
    cv2.imshow('SERVEUR',decimg)
    cv2.waitKey(1)
>>>>>>> mehdi
cv2.destroyAllWindows() 
sock.close()
s.close()
