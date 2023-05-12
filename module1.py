#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sebastian
#
# Created:     17/06/2021
# Copyright:   (c) Sebastian 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math
import io

##def lectura(archivo, lista):
##    lineas = archivo.readlines()
##    for linea in lineas:
##        lista.append(linea[:-1])
##with io.open(filename,'r',encoding='utf8') as f:
##    text = f.read()

def lectura(archivo, lista):

    lines = archivo.read().split(' ')

    for line in lines:
        lista.append(line)

archivo=open("lemario.txt","r",encoding='latin1')
lista=[]

lectura(archivo, lista)

print(lista)