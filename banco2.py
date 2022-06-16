#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------
# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
# Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener 
# el importe del interés (cantidad*interés/100) y otro método para mostrar la información, 
# datos del titular, plazo, interés y total de interés. 
# Crear al menos un objeto de cada subclase.
#-------------------------------------------------------------------------------------------
# creamos la clase Cuenta
class Cuenta:
	def __init__(self,titular,cantidad): # inicializamos los atributos de la clase
		self.titular=titular
		self.cantidad=cantidad
	def imprimir(self):                  # imprimimos los datos
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)
#
# creamos la clase CajaAhorro
# esta clase hereda atributos de la clase Cuenta
class CajaAhorro(Cuenta):
	def __init__(self,titular,cantidad): # iniciamos los atributos de la clase
		super().__init__(titular,cantidad)
	def imprimir(self):                  # imprimimos los datos de la cuenta
		print("Cuenta de caja de ahorros")
		super().imprimir()
#
# creamos la clase PlazoFijo
# esta clase también hereda atributos de la clase Cuenta
class PlazoFijo(Cuenta):
	def __init__(self,titular,cantidad,plazo,interes): # inicializamos los atributos de la clase
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes
	def ganancia(self):                  # calculamos la ganancia
		interesA = self.plazo * self.interes / 365
		ganancia = self.cantidad * interesA / 100
		# ganancia = self.cantidad * self.interes/100
		print("El importe de interés es: ", round(ganancia,2))   # imprimimos los resultados
		print("Nuevo monto en caja de ahorro: ", round(self.cantidad+ganancia,2))
	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()
#
# bloque principal
cliente = input("Ingrese el nombre del cliente: ")
monto = float(input("Ingrese monto inicial Caja de Ahorro: "))
caja1=CajaAhorro(cliente,monto)
caja1.imprimir()
#
cliente = input("Ingrese el nombre del cliente: ")
monto = float(input("Ingrese monto inicial Plazo Fijo: "))
plazo = int(input("Ingrese el plazo expresado en días: "))
interes = 47
plazo1=PlazoFijo(cliente,monto,plazo,interes)
plazo1.imprimir()
