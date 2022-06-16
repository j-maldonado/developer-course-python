#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Probando():
	def __init__(self):
		self.var1=2
		self.var2="hola"
		self.var3=input("Ingresa un valor: ")
		
	def get_valores(self):
		print("Var1: ", self.var1)

    #def __init__(self,num1,num2):
	#	self.num1=num1
	#	self.num2=num2

nuevoObj = Probando()
nuevoObj = Probando.__init__
nuevoObj = Probando.get_valores
