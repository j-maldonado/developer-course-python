#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------- Herencia Simple ---------------------------------------------
class Estudiante(object):             #Creamos la clase padre, usamos el parámetro Object que esta definido por defecto en Python
    def __init__(self, edad, nombre): # Definimos los parámetros edad y nombre
        self.edad = edad              #Declaramos que el atributo edad es igual al argumento edad
        self.nombre = nombre          #Declaramos que el atributo nombre es igual al argumento nombre

class Ingenieria(Estudiante):         #Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
                                      #Lo que la convierte a INGENIERIA en una clase hija o secundaria
    def presentarse(self):            #Creamos el método presentarse
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio Ingenieria") #Se presenta llamando los atributos

Clara = Ingenieria(23, 'Clara Fraser') #Indicamos argumentos edad y nombre, instanciamos obj de Ingen. y hereda de Estudiante
Clara.presentarse()                  # Llamamos al método y Clara se presenta

# -------- Herencia Múltiple ------------------------------------------

class Estudiante(object):             #Creamos la clase padre
    def __init__(self, edad, nombre): # Definimos los parámetros edad y nombre
        self.edad = edad              #Declaramos que el atributo edad es igual al argumento edad
        self.nombre = nombre          #Declaramos que el atributo nombre es igual al argumento nombre
class Instituto(object):
    def presentarinstituto (self):
        print("Estudio en el Instituto de Formación Técnica Superior N° 3")
class Ingenieria(Estudiante, Instituto): #Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
                                     #Lo que la convierte a INGENIERIA en una clase hija o secundaria
    def presentarse(self):           #Creamos el método presentarse
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio Ingenieria") #Se presenta llamando los atributos
       
Clara = Ingenieria(26, 'Clara Fraser') #Indicamos argumentos edad y nombre, creamos obj instanciando la clase Ingenieria y hereda de estudiante e instituto
Clara.presentarse()                 # Llamamos al método y Clara se presenta
Clara.presentarinstituto()

