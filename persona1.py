#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y
# “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos.

class Persona:

    # creamos la primera funcion
    # para inicializar el atributo nombre, edad, dni
    def set_nombre(self,nom):
        self.nombre=nom
    def set_edad(self,anios):
        self.edad = anios
    def set_dni(self,doc):
        self.dni = doc
 
    # creamos el segundo metodo
    # para mostrar el nombre, edad, dni
    def get_nombre(self):
        print("Nombre: ",self.nombre)
    def get_edad(self):
        print("Edad: ", self.edad)
    def get_dni(self):
        print("DNI: ", self.dni)
 
#bloque principal
# creamos una instancia de la clase persona
persona1=Persona()
persona1.set_nombre("Pedro")
persona1.get_nombre()

persona1.set_edad(40)
persona1.get_edad()

persona1.set_dni(27123456)
persona1.get_dni()

# creamos un objeto de la clase persona
persona2=Persona()
persona2.set_nombre("Clara")
persona2.get_nombre()

persona2.set_edad(25)
persona2.get_edad()

persona2.set_dni(29098765)
persona2.get_dni()
