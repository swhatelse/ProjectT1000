#!/usr/bin/python
# -*- encoding: UTF-8 -*-

#~ pip install enum34
#~ from enum import Enum

def enum(**enums):
    return type('Enum', (), enums)


if __name__ == '__main__':
    '''permet d'avoir un enumerate définissable par son constructeur'''
    number=enum(One=1,
                Two=2,
                Three="three")
                #Enumeration=valeur
    print(number.One)
    print(number.Two)
    print(number.Three)
