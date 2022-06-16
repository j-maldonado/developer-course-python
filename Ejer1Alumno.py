#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si 
# ha aprobado o no.

class Alumno:
	def inicializar (self, nombre, nota):
		self.nombre = nombre
		self.nota = nota

	def imprimir (self):
		print('Alumno: ', self.nombre)
		print('Nota: ', self.nota)
	
	def resultado(self):
		if self.nota > 4:
			print('Aprobado')
		else:
			print('Desaprobado')

alumno1=Alumno()

alumno1.inicializar('joan', 9)

alumno1.imprimir()
alumno1.resultado()