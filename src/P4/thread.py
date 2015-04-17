# -*- encoding: UTF-8 -*-

import threading as thread
from threading import Thread as th
import time

lock=thread.Lock()
truc=0
def whenYouWant(s):
    print s
class Afficheur(th):
    def __init__(self,phrase,function):
        th.__init__(self)
        self.phrase=phrase
        self.function=function

    def run(self):
        i=0
        while(i<20):
            lock.acquire()
            self.function(self.phrase+" "+str(i))
            lock.release()
            time.sleep(0.006)
            i+=1


a=Afficheur("premier mais pas le second parce que c'est le premier",whenYouWant)
b=Afficheur("second qui viens après le premier mais pas toujours ça peut être \
mélangé mais je tiens a préciser que c'est le second",whenYouWant)
c=Afficheur("thibaud est une ...",whenYouWant)
a.start()
b.start()   
c.start()
a.join()
b.join()
c.join()
print "fin"

