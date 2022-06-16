#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------
# En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
# El banco requiere también al final del día calcular la cantidad de dinero 
# que se ha depositado.
#1.Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente
# tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
#2.La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar
# y deposito_total.
#
# creamos la clase banco
class Banco:
	                     # inicializamos
	def __init__(self):
		self.cliente1 = Cliente("Ivan")
		self.cliente2 = Cliente("Marcos")
		self.cliente3 = Cliente("Juan")
		self.cliente4 = Cliente(input("Ingrese nombre del cliente: "))
		self.cliente5 = Cliente(input("Ingrese nombre del cliente2: "))
		self.cliente6 = Cliente(input("Ingrese nombre del cliente3: "))
	                     # función para operar
	def operacion(self):
		self.cliente1.depositar(1000)
		self.cliente2.depositar(300)
		self.cliente3.depositar(43)
		self.cliente4.depositar(int(input("Ingrese cantidad a depositar4: ")))
		self.cliente5.depositar(int(input("Ingrese cantidad a depositar5: ")))
		self.cliente6.depositar(int(input("Ingrese cantidad a depositar6: ")))
		self.cliente1.extraer(400)
		self.elegir = int(input("""
		¿Que operación desea realizar?
		0 - Depósito
		1 - Extracción
		"""))
		if self.elegir == 0:
			self.cliente5.depositar(int(input("Ingrese cantidad a depositar5: ")))
		else:
			self.cliente5.extraer(int(input("Ingrese cantidad a extraer: ")))
	                     # función para obtener los depósitos totales
	def depositos(self):
		total = self.cliente1.devolver_cantidad() + self.cliente2.devolver_cantidad() + self.cliente3.devolver_cantidad() + self.cliente4.devolver_cantidad() + self.cliente5.devolver_cantidad() + self.cliente6.devolver_cantidad()
		print("El total de dinero del banco es: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()
		self.cliente4.imprimir()
		self.cliente5.imprimir()
		self.cliente6.imprimir()
# creamos la clase Cliente
class Cliente:
	                     # inicializamos
	def __init__(self,nombre):
		self.nombre = nombre
		self.cantidad = 0
	                     # función para depositar dinero
	def depositar(self,cantidad):
		self.cantidad = self.cantidad + cantidad
	                     # función para extraer dinero
	def extraer(self,cantidad):
		self.cantidad = self.cantidad - cantidad
	                     # función para obtener el total de dinero
	def devolver_cantidad(self):
		return self.cantidad
	                     # función para imprimir los datos del cliente
	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)
#
# bloque principal
banco1 = Banco()
banco1.operacion()
banco1.depositos()
