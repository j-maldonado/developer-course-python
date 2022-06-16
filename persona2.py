#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Humano:     # creamos la clase humano
	def __init__(self, edad, nombre, dni, ocupacion):  # método constructor
		self.edad = edad           
		self.nombre = nombre
		self.dni = dni
		self.ocupacion = ocupacion
		
	def get_persona(self):
		print( "\n"
		"Nombre: ", self.nombre, "\n" 
		"DNI: ", self.dni, "\n"
		"Edad: ", self.edad, "\n"
		"Ocupación: ", self.ocupacion, "\n"
		)
		mostrar = ("Hola soy {}, tengo {} años, mi DNI es {}, y mi ocupacion {}") # mensaje respuesta
		print(mostrar.format(self.nombre, self.edad, self.dni, self.ocupacion))
# Ahora cambiemos un atributo mediante un método para mantener el encapsulamiento:
	def contratar(self, puesto):  #añadimos un nuevo parámetro en el método
		self.puesto = puesto
		print ("{} ha sido contratado como {}".format(self.nombre, self.puesto))
		self.ocupacion = puesto   #Ahora cambiamos el atributo ocupación
		
#cuerpo principal con ingreso de datos
#nombre = input("Ingrese el nombre de la persona: ")
#edad = int(input("Ingrese la edad de la persona: "))
#dni = int(input("Ingrese el Nro.de Documento: "))
#ocupacion = input("Ingrese ocupación: ")
nombre = "Blanca"
edad = 35
dni = 29123456
ocupacion = "Docente"

persona3 = Humano(edad, nombre, dni, ocupacion)
persona3.get_persona()
persona3.contratar("Secretaria")  # aqui llamamos al método que cambia el atributo ocupacion
persona3.get_persona() # volvemos a mostrar con el cambio de ocupacion
