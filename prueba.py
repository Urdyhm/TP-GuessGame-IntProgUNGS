#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sebastian
#
# Created:     19/06/2021
# Copyright:   (c) Sebastian 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random


class char():
    def __init__(self):
        pass

class char_line():
    def __init__(self, word):
        self.word = word
        self.char_line = [(char, self.char_type(char)) for char in word]
        self.type_line = ''.join(chartype for char, chartype in self.char_line)

    def char_type(self, char):
        if char in set(['a', 'Ã¡', 'e', 'Ã©','o', 'Ã³', 'u', 'Ãº']):
            return 'V' #strong vowel
        if char in set(['i', 'u']):
            return 'v' #week vowel
        if char=='x':
            return 'x'
        if char=='s':
            return 's'
        else:
            return 'c'

    def find(self, finder):
        return self.type_line.find(finder)

    def split(self, pos, where):
        return char_line(self.word[0:pos+where]), char_line(self.word[pos+where:])

    def split_by(self, finder, where):
        split_point = self.find(finder)
        if split_point!=-1:
            chl1, chl2 = self.split(split_point, where)
            return chl1, chl2
        return self, False

    def __str__(self):
        return '<'+self.word+':'+self.type_line+'>'

    def __repr__(self):
        return '<'+repr(self.word)+':'+self.type_line+'>'

class silabizer():
    def __init__(self):
        self.grammar = []

    def split(self, chars):
        rules  = [('VV',1), ('cccc',2), ('xcc',1), ('ccx',2), ('csc',2), ('xc',1), ('cc',1), ('vcc',2), ('Vcc',2), ('sc',1), ('cs',1),('Vc',1), ('vc',1), ('Vs',1), ('vs',1), ('vxv',1), ('VxV',1), ('vxV',1), ('Vxv',1)]
        for split_rule, where in rules:
            first, second = chars.split_by(split_rule,where)
            if second:
                if first.type_line in set(['c','s','x','cs']) or second.type_line in set(['c','s','x','cs']):
                    #print 'skip1', first.word, second.word, split_rule, chars.type_line
                    continue
                if first.type_line[-1]=='c' and second.word[0] in set(['l','r']):
                    continue
                if first.word[-1]=='l' and second.word[-1]=='l':
                    continue
                if first.word[-1]=='r' and second.word[-1]=='r':
                    continue
                if first.word[-1]=='c' and second.word[-1]=='h':
                    continue
                return self.split(first)+self.split(second)
        return [chars]

    def __call__(self, word):
        return self.split(char_line(word))



def separador(palabra):
    s = silabizer()
    si=s(palabra)
    nueva=""
    for elem in si:
        encontre=False
        elem=str(elem)
        for e in elem:
            if e!="<" and e!=":" and not encontre:
                nueva=nueva+e
            if e==":":
                nueva=nueva+"-"
                encontre=True
    return nueva[:-1]

def nuevaSilaba(silabas): #YA ANDA
    azar=random.randrange(0,len(silabas))
    nueva=silabas[azar]
    return nueva.lower()


def dameSilabas(candidata): #YA ANDA
    separadas=separador(candidata)
    lista=separadas.split("-")
    return lista

##def lectura(archivo, lista): #YA ANDA
##    lines = archivo.readlines()
##    for line in lines:
##        lista.append(line[:-1])
####
##def Puntos(candidata): #YA ANDA
##    puntos=0
##
##    for letra in candidata:
##        if letra == "a" or "e"or"i" or "o" or "u":
##                puntos=puntos+1
##        if letra == "j" or "k" or "q" or "w" or "x" or "y" or "z" :
##            puntos=puntos+5
##        else:
##            puntos=puntos+2
##
##    return puntos
##

def dondeAparece(lis,blanco,negro):

    salida=[]

    for i in range(len(lis)):
        if lis[i] == blanco:
            salida.append(i)
        elif lis[i] == negro:
            salida.append(i)


    return salida


def esValida(candidata, silabasEnPantalla, lemario):

    # Separo el ingreso en sílabas para ver si coincide con silabasEnPantalla
    # Además de estar esa palabra en el lemario
    # Para saber si es válida

##    if candidata in silabasEnPantalla and candidata in lemario:
##         return True
    silabasCandidata=dameSilabas(candidata)
    coincidencia=0
    for i in range(len(silabasCandidata)):
        if silabasCandidata[i] in silabasEnPantalla:
            coincidencia+=1
            if coincidencia==len(silabasCandidata) and candidata in lemario:
                return True


##    if dameSilabas(candidata) in silabasEnPantalla and candidata in lemario:
##            return True

    else:

        return False


##def quitar(candidata, silabasEnPantalla, posiciones): #YA ANDA
##    silabas=dameSilabas(candidata)
##
##    for sila in silabas:
##
##        i = silabasEnPantalla.index(sila)
##
##        silabasEnPantalla.pop(i)
##        posiciones.pop(i)
##
##def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
##
##    #Para silabas nuevas
##
##    generada=nuevaSilaba(listaDeSilabas)
##    silabasEnPantalla.append(generada)
##    x=random.randrange(0,800-20)
##    y=0
##    pos=[x,y]
##    posiciones.append(pos)
##
##
##    # Actualizar la posicion en pantalla y quitarlas antes del final
##    i=0
##    while i<len(posiciones):
##        if posiciones[i][1]>=600-100:
##            silabasEnPantalla.pop(i)
##            posiciones.pop(i)
##        else:
##            posiciones[i][1] = posiciones [i][1] + 10
##            i+=1


##def procesar(candidata, silabasEnPantalla, posiciones, lemario):
##
##    # Si es valida la quito de la pantalla y devuelvo los puntos que gane para sumarlos
##    if esValida(candidata, silabasEnPantalla, lemario ):
##        quitar(candidata,silabasEnPantalla,posiciones)
##        success_sound = pygame.mixer.Sound("success.wav")
##        pygame.mixer.Sound.play(success_sound)
##        pygame.mixer.music.stop()
##        return Puntos(candidata)
##    else:
##        crash_sound = pygame.mixer.Sound("crash.wav")
##        pygame.mixer.Sound.play(crash_sound)
##        pygame.mixer.music.stop()
##        return 0

##listaDeSilabas=[]
##archivo= open("silabas.txt","r")
##lectura(archivo, listaDeSilabas)
##print (listaDeSilabas)
##lemario=["ca","ba","llo","pe","rro"]
lemario2=["caballo"]
##archivo2= open("lemario.txt","r", encoding='latin1')
##lectura(archivo2, lemario)
##posiciones = []
siPant1=["ca","ba","llo"]
##siPant=["ca","pe"]
##silabList=["ca","ba","llo","pe","rro"]
can1="caba"
##can2="rro"

##print("Este es el resultado de posiciones", posiciones, actualizar(siPant,posiciones,silabList))
##print("Este es el resultado de quitar", quitar(can2,siPant,posiciones), posiciones)
print("Este es el resultado de esValida", esValida(can1,siPant1,lemario2))

##print("Esto es el resultado de Puntos", Puntos(can))
####
##print("Esto es el resultado de la funcion separador", separador(can1))
##print ("Esto es el resultado de la funcion dameSilabas", dameSilabas(can1))
