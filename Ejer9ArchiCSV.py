#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# Crear una clase persona que contenga un método estático “dump_csv” que
# reciba el nombre de un archivo, una lista de personas y genere un 
# archivo CSV separado por comas con los datos de cada persona. 
#-----------------------------------------------------------------------
class ArchiPersona():
	def dump_csv(self):
		nomArchi = input("Ingrese el nombre del archivo: ")
		with open(nomArchi, 'w') as jArchi:
			sigue = True
			while sigue == True:
				nombre = input("Ingrese nombre: ")
				jArchi.write(nombre + ",")
				continua = input("¿Desea seguir ingresando?(S/N): ").lower()
				if continua != "s":
					sigue = False
			jArchi.close()
		return nomArchi
#-----------------------------------------------------------------------
# Al ejercicio anterior agregar un método “load_csv” que reciba el nombre 
# de un archivo y devuelva una lista de objetos Persona.
#-----------------------------------------------------------------------
	def load_csv(self, nombre):
		nomArchi = nombre
		with open(nomArchi, 'r') as lArchi:
			linea = lArchi.readline()
			while linea != "":
				renglon = linea.split(',')
				for cadaNom in renglon:
					print(cadaNom)
				linea = lArchi.readline()
			lArchi.close()
#
# bloque principal
pruebaArchi = ArchiPersona()
nomArchi = pruebaArchi.dump_csv()
pruebaArchi.load_csv(nomArchi)
