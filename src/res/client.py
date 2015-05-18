#!/usr/bin/python
import socket
import cv2
import numpy
import ResValue

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

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))


TCP_IP_server = 'localhost'
TCP_PORT_server = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP_server, TCP_PORT_server))
s.listen(True)
conn, addr = s.accept()
capture = cv2.VideoCapture(0)
colonne=0
while(colonne!=ResValue.V.Fin):
#~ while(True  ):
    ret, frame = capture.read()
    
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()
    
    sock.send( str(len(stringData)).ljust(16));
    sock.send( stringData );
    #~ 
    decimg=cv2.imdecode(data,1)
    cv2.imshow('CLIENT',decimg)
    
    #~ --
    
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    
    colonne= int(stringData)
    cv2.waitKey(1) 
    
cv2.destroyAllWindows() 
s.close()
sock.close()



