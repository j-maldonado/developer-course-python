#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos 
# el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los 
# datos e indicar si la persona es mayor de edad o no.
# creamos nuestra clase Persona  
class Persona:
	def inicializar(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad
	def imprimir(self):
		print("Nombre: ",self.nombre)
		print("Edad: ",self.edad)
	def mayor_edad(self):
		if self.edad >= 18:
			print("Es mayor de edad")
		else:
			print("No es mayor de edad")
# bloque principal
persona1=Persona()
persona1.inicializar("Julieta",17)
persona2=Persona()
persona2.inicializar("Elian",18)
# imprimimos datos y comprobamos si es mayor de edad
persona1.imprimir()
persona1.mayor_edad()
persona2.imprimir()
persona2.mayor_edad() 


#--------------------------------------------
# Resolución Alejandra
#--------------------------------------------
class PersonaE:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def get_mayor(self):
        if self.edad >= 18:
            print(f'{self.nombre} es mayor de edad')
        else:
            print(f'{self.nombre} es menor de edad')
Siguiente = True

while Siguiente == True:
    Nombre = input('Ingrese su Nombre: ')
    Edad = int(input('Ingrese su Edad: '))

    ConsultaPersona = PersonaE(Nombre,Edad)
    ConsultaPersona.get_mayor()

    Otro = input('Desea consultar otro nombre? S/N ')
    if Otro == 'S' or Otro == 's':
        Siguiente = True
    else:
        Siguiente = False
