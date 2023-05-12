from principal import *
from configuracion import *
from funcionesSeparador import *

import pygame
import random
import math

def lectura(archivo, lista):

    #Lee el archivo linea por linea
    lines = archivo.readlines()

    # Y las agrega a una lista que elegí
    for line in lines:
        # Para agregar la palabra sin "\n" y sabiendo que se encuentra al final de cada palabra selecciono todo menos eso último
        lista.append(line[:-1])


def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):

    # Voy llenando la lista silabasEnPantalla
    generada=nuevaSilaba(listaDeSilabas)
    silabasEnPantalla.append(generada)

    # Al mismo tiempo genero una lista de coordenadas correspondiente a cada silaba
    # Dentro de un rango que evite que salgan fuera de la pantalla y que quede centrado
    x=random.randrange(50,ANCHO-50)
    y=-20
    pos=[x,y]
    posiciones.append(pos)


    # Recorro todas las coordenadas para revisar si están fuera de la pantalla
    i=0
    while i<len(posiciones):

        # Si es así, remuevo la silaba y su correspondiente posicion
        if posiciones[i][1]>=ALTO-100:
            silabasEnPantalla.pop(i)
            posiciones.pop(i)


        # Sino voy moviendo la silaba, en un espacio mayor que la altura de las letras para que no se superpongan
        else:
            posiciones[i][1] = posiciones [i][1] + 25
            i+=1



def nuevaSilaba(silabas):

    # Selecciona una sílaba al azar de la lista que ingresa
    silaba = random.choice(silabas)
    return silaba


def quitar(candidata, silabasEnPantalla, posiciones):

    # Separa el ingreso del usuario en silabas
    silabas=dameSilabas(candidata)

    # Busca la posición de la coincidencia del ingreso en silabasEnPantalla
    for sila in silabas:
        if sila in silabasEnPantalla:
            i = silabasEnPantalla.index(sila)
            silabasEnPantalla.pop(i)
            posiciones.pop(i)


def dameSilabas(candidata):

     # Obtiene las silabas de la palabra ingresada separada por un guión
    separadas=separador(candidata)

     # Arma una lista de las silabas sin el guión
    lista=separadas.split("-")
    return lista


def esValida(candidata, silabasEnPantalla, lemario):

    # Separo el ingreso en sílabas para ver si coincide con silabasEnPantalla
    # Además de estar esa palabra en el lemario
    # Para saber si es válida

    silabasCandidata=dameSilabas(candidata)
    coincidencia=0
    for i in range(len(silabasCandidata)):
        if silabasCandidata[i] in silabasEnPantalla:
            coincidencia+=1
            if coincidencia==len(silabasCandidata) and candidata in lemario:
                return True

    else:

        return False



def Puntos(candidata):

    # Un acumulador de puntos en funcion de las letras que tenga la palabra ingresada
    # Mientras mas rara la letra, más puntos da
    puntos=0

    for letra in candidata:
        if letra == "a" or "e" or "i" or "o" or "u":
            puntos=puntos+1
        if letra == "j" or "k" or "q" or "w" or "x" or "y" or "z" :
            puntos=puntos+5
        else:
            puntos=puntos+2

    return puntos


def procesar(candidata, silabasEnPantalla, posiciones, lemario):

    # Si es valida la quito de la pantalla y devuelvo los puntos que gane para sumarlos
    if esValida(candidata, silabasEnPantalla, lemario ):
        quitar(candidata,silabasEnPantalla,posiciones)
        success()
        puntos=Puntos(candidata)
        if puntos>100:
            super()
        return puntos
    else:
        crash()
        return 0


def super():
    super_sound = pygame.mixer.Sound("super.wav")
    pygame.mixer.Sound.play(super_sound)
    pygame.mixer.music.stop()

def success():
     success_sound = pygame.mixer.Sound("success.wav")
     pygame.mixer.Sound.play(success_sound)
     pygame.mixer.music.stop()


def crash():
     crash_sound = pygame.mixer.Sound("crash.wav")
     pygame.mixer.Sound.play(crash_sound)
     pygame.mixer.music.stop()
