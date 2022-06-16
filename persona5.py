#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------ SUPER clase padre -------------------------------------------
"""
class Padre(object):                 #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo(Padre):                   #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas) #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara             #Especificamos el nuevo atributo para Hijo

# usando super() quedaría:
class HijoS(Padre):                  #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara             #Especificamos el nuevo atributo para Hijo
        
Tomas = HijoS('Marrones', 'Negras', 'Redonda')
print("Los ojos de Tomas son ", Tomas.ojos, ", sus cejas son ", Tomas.cejas, " y su cara ", Tomas.cara)
"""
# ------------- llamar un metodo de otra clase (list) padre con super() --------------------------------

class Agregarelemento(list):    #Creamos una clase Agregarelemento heredando atributos de clase list (clase incorporada)
    def append(self, alumno):   #Definimos que el método append (de listas) añadirá el elemento alumno
        print (("Añadido el alumno"), (alumno)) #Imprimimos el resultado del método
        super().append(alumno)  #Incorporamos la función super SIN INDICAR LA CLASE ACTUAL, seguida
                                #del método append para la variable alumno
Lista1 = Agregarelemento()      #Definimos la clase de nuestra lista llamada "Lista1"
Lista1.append ('Pablo')         #Añadimos un elemento a la lista como lo haríamos normalmente
Lista1.append ('Juan')
print (Lista1)                  #Imprimimos la lista para corroborar que se añadió el alumno

