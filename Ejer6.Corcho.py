#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Botella y Sacacorchos
# a) Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
# b) Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la
# tapa, o None si está destapada.
# c) Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque
# el corcho y se guarde una referencia al corcho sacado. Debe lanzar una excepción en el caso en
# que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.
# d) Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el
# caso en el que no haya un corcho.
#---------------------------------------------------------------------
#
class Corcho(object):
    def __init__ (self, bodega):      # Metodo constructor
        self.bodega=bodega

    def __str__(self):        # muestra nombre de la bodega en el corcho
        print("La Bodega del corcho es:"+str(self.bodega))
#
class Botella(object):
    def __init__(self,corcho): # Metodo constructor
        if Corcho:
            self.corchotapado=Corcho
        else :
            self.corchotapado=None
    def __str__(self):
        if not self.corchotapado:
            return "La botella esta destapada"
        else :
            return "La botella esta tapada y tiene el corcho :"+str(self.corchotapado)
#
class Sacacorchos(Corcho, Botella):
	def __init__(self, bodega, corcho):
		self.bodega = bodega
		if corcho == 1:
			self.corchotapado = "tapado"
		else:
			self.corchotapado = None
	def __str__(self):
		return "Tengo la botella : "+str(self.bodega)+" y el corcho : "+str(self.corchotapado)
	def destapar(self):
		if self.corchotapado != None:
			corchodestapado = self.corchotapado
			self.corchotapado = None
			return self.corchotapado #   corchodestapado
		else:
			raise AttributeError("La botella ya esta destapada")
	def limpiar(self,destapar):
		if destapar != None:
			self.corchotapado = None
		else:
			raise AttributeError("El sacacorchos no tiene corcho")
# Main Program
bodega = input("Ingrese nombre de la Bodega: ")
hayCorcho = int(input("Si la botella tiene el corcho puesto, Ingrese 1, sino 0: "))
nomBodega = Sacacorchos(bodega, hayCorcho)
nomBodega.__init__(bodega, hayCorcho)
print(nomBodega.__str__())
print("Tiene corcho? ", nomBodega.destapar())
