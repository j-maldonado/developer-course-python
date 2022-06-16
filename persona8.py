#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------- Declaramos Variables de Clase --------------------------------

class Perros(object):
    'Clase para los perros'           #Descripción
    Collar = True                     #Variable de clase Estática
    def __init__(self, salud, hambre):
        self.salud = salud            #Variable de Instancia
        self.hambre = hambre          #Variable de Instancia
print("El perro tiene collar: ", Perros.Collar) #podemos accederla sin crear un objeto(sin instanciar)

# -------------- Accedemos a variables de Instancia ---------------------------

# print (Perros.hambre) #-> ASI NO PODES!, porque hambre es una variable de instancia
#Debes instanciar:
Pequines = Perros(100, 5)
print("¿Cuanto kilos come un Pequines?: ", Pequines.hambre)
