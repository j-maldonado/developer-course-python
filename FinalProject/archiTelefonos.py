#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa. 
# El programa incorpora funciones para crear el fichero con el listado si no existe, para consultar el teléfono de un cliente, 
# añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listado debe estar guardado en el fichero de 
# texto listado.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea 
# distinta. 
#agenda con nombre, apellido y telefono, en renglones uno debajo del otro
import os
def buscar_entrada(nombre, apellido):
	with open("agenda.txt", "r") as jArchi:
		linea = jArchi.readline()
		while linea != "":
			renglon = linea.split(',')
			if nombre == renglon[1] and apellido == renglon[2]:
				jArchi.close()
				return renglon[3][:-1]
			linea = jArchi.readline()
		jArchi.close()
		return None
def modificar_reg(nombre, apellido, telefono):
	with open("agenda.txt", "r") as rArchi:
		with open("agendacpy.txt", "w") as wArchi:
			linea = rArchi.readline()
			while linea != "":
				renglon = linea.split(',')
				if nombre == renglon[1] or apellido == renglon[2]:
					wArchi.writelines(renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + str(telefono) + "\n")
				else:
					wArchi.write(linea)
				linea = rArchi.readline()
			wArchi.close()
		rArchi.close()
		
	with open("agendacpy.txt", "r") as fcopia:
		with open("agenda.txt", "w") as foriginal:
			for registro in fcopia:
				foriginal.write(registro)
			fcopia.close()
		foriginal.close()
def agrego_entrada(documento, nombre, apellido, telefono):
	with open("agenda.txt", "a") as jArchi:
		jArchi.write(str(documento) + "," + nombre + "," + apellido + "," + str(telefono) + "\n")
		jArchi.close()
def borrar_registro(nombre, apellido):
	with open("agenda.txt", "r") as rArchi:
		with open("agendacpy.txt", "w") as wArchi:
			linea = rArchi.readline()
			while linea != "":
				renglon = linea.split(',')
				if nombre != renglon[1] or apellido != renglon[2]:
					wArchi.write(linea)
				linea = rArchi.readline()
			wArchi.close()
		rArchi.close()
		
	with open("agendacpy.txt", "r") as fcopia:
		with open("agenda.txt", "w") as foriginal:
			for registro in fcopia:
				foriginal.write(registro)
			fcopia.close()
		foriginal.close()
def limpioPantalla():
	sisOper = os.name
	if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
		os.system("clear")
	elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
		os.system("cls")
def consultaAgenda():
	with open("agenda.txt", "r") as kArchi:
		print("***************** AGENDA COMPLETA ***************")
		print("{4}{0:^8}{4} {4}{1:^16}{4} {4}{2:^15}{4} {4}{3:^11}{4}".format("DNI","Nombre", "Apellido", "Telefono", "|"))
		linea = kArchi.readline()
		while linea != "":
			renglon = linea.split(',')
			print("{4}{0:>8}{4} {4}{1:16s}{4} {4}{2:15s}{4} {4}{3:>11}{4}".format(renglon[0], renglon[1], renglon[2], renglon[3][:-1], "|"))
			linea = kArchi.readline()
		print("------------------------------------------------------------")
		kArchi.close()
def muestroMenu():
	print("****************** ABM AGENDA *******************")
	print('''
	0 - Consultar teléfono de un cliente
	1 - Agregar un nuevo cliente
	2 - Eliminar un cliente
	3 - Modificar el teléfono de un cliente
	4 - Consultar toda la agenda
	5 - Limpiar pantalla
	7 - Salir
***************************************************
    ''')

opc = 0
while opc != 7:
	muestroMenu()
	opcion = int(input("Elija la opción deseada:"))
	if opcion == 0:
		print("¿A quien desea buscar en la agenda?")
		nombre = input("Ingrese el Nombre: ")
		apellido = input("Ingrese el Apellido: ")
		print("Su teléfono es: ", buscar_entrada(nombre, apellido))
	elif opcion == 1:
		print("Se agregará un nuevo cliente.")
		documento = int(input("Ingrese el DNI: "))
		nombre = input("Ingrese el Nombre: ")
		apellido = input("Ingrese el Apellido: ")
		telefono = input("Ingrese el Teléfono: ")
		print("Se agregó nuevo cliente.", agrego_entrada(documento, nombre, apellido, telefono))
	elif opcion == 2:
		print("Se eliminará el cliente")
		nombre = input("Ingrese el Nombre: ")
		apellido = input("Ingrese el Apellido: ")
		print("Se ha eliminado el cliente ", nombre, apellido, borrar_registro(nombre, apellido))
	elif opcion == 3:
		print("Se modificará el teléfono del cliente.")
		nombre = input("Ingrese el Nombre: ")
		apellido = input("Ingrese el Apellido: ")
		telefono = input("Ingrese el Teléfono: ")
		print("Se ha modificado el teléfono de ", nombre, apellido, modificar_reg(nombre, apellido, telefono))
	elif opcion == 4:
		limpioPantalla()	
		consultaAgenda()
	elif opcion == 5:
		limpioPantalla()
	else:
		opc = opcion
