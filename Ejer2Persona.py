#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos 
# el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los 
# datos e indicar si la persona es mayor de edad o no.
# creamos nuestra clase Persona  

class Persona:
    def inicializar (self, nombre, edad):
        self.nombre= nombre 
        self.edad= edad

    def imprimir (self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        

    def resultado (self):
        if self.edad > 18:
            print("Es Mayor de Edad")
        else:
            print('Es Menor de Edad')



persona1=Persona()

persona1.inicializar(nombre=input('ingrese su nombre: '), edad=('Ingrese su edad: '))

persona1.imprimir()
persona1.resultado()
