#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Herencia Multiple y Atributos no sirve Super(), hay que usar los constructores
# de las clases especificándolas por su nombre. Y si cambiamos el nombre u orden de
# la clase debemos especificarlo.

class Padre(object):                 #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
class Madre(object):                 #Creamos la clase Padre llamada Madre
    def __init__(self, brazos, piernas): #Definimos los Atributos
        self.brazos = brazos
        self.piernas = piernas
        
class Hijo(Padre, Madre):            #Creamos clase hija que hereda de Padre y luego de Madre
    def __init__(self, ojos, cejas, cara, brazos, piernas): #creamos el constructor de la clase especificando atributos
        Madre.__init__(self, brazos, piernas)
        Padre.__init__(self, ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara
        
Tomas = Hijo('Marrones', 'Negras', 'Redonda', 2, 2)
print(Tomas.ojos, Tomas.cejas, Tomas.cara, Tomas.piernas, Tomas.brazos)
print("Los ojos de Tomas son ", Tomas.ojos, ", sus cejas son ", Tomas.cejas, " y su cara ", Tomas.cara, ", tiene ", Tomas.piernas, " piernas y ", Tomas.brazos, " brazos.")
