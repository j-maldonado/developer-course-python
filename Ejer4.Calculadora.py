#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Realizar un programa en el cual se declaren dos valores enteros por 
# teclado utilizando el método __init__. Calcular después la suma, resta, 
# multiplicación y división. Utilizar un método para cada una e imprimir
# los resultados obtenidos. Llamar a la clase Calculadora.
# creamos la clase
class Calculadora:
# iniciamos con el método __init__
	def __init__(self):
		self.valor1=int(input("Ingrese el primer valor: "))
		self.valor2=int(input("Ingrese el segundo valor: "))
# función para sumar
	def suma(self):
		suma=self.valor1+self.valor2
		print("El resultado de la suma de los valores es: ",suma)
# función para restar
	def resta(self):
		resta=self.valor1-self.valor2
		print("El resultado de la resta de los valores es: ",resta)
# función para calcular el producto
	def multiplicacion(self):
		pro=self.valor1*self.valor2
		print("El resultado de la multiplicación de los valores es: ",pro)
# función para dividir
	def division(self):
		div=self.valor1/self.valor2
		print("El resultado de la división de los valores es: ",div)
# función para imprimir
	def imprimir(self):
		print("Los valores son: ")
		print("Valor 1: ",self.valor1)
		print("Valor 2: ",self.valor2)

# bloque principal
calcular=Calculadora()
calcular.imprimir()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.division()

"""
# ---------- otra opcion hecha por Alejandra --------------------
class Calculadora:
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2

    def get_suma(self):
        Suma = self.Num1 + self.Num2
        print(f'El resultado de la suma de {self.Num1} + {self.Num2} = {Suma}')

    def get_resta(self):
        Resta = self.Num1 - self.Num2
        print(f'El resultado de la resta de {self.Num1} - {self.Num2} = {Resta}')
    def get_multiplicacion(self):
        Multiplicacion = self.Num1 * self.Num2
        print(f'El resultado de la multiplicacion de {self.Num1} * {self.Num2} = {Multiplicacion}')

    def get_division(self):
        while True:
            try:
                Division = self.Num1 / self.Num2

            except ZeroDivisionError:
                print(f'No se puede existe la division por 0, debera volver a elegir')
                num2 = float(input('Ingrese el nuevo divisor distinto de 0: ')
    Otro = True

while Otro:
    Numero1 = float(input('Ingreso el primer numero: '))
    Numero2 = float(input('Ingrese el segundo numero: '))

    Calculo = Calculadora(Numero1,Numero2)

    Operacion = input('Que operacion desea hacer? S=Suma, R=Resta, M=Multiplicacion, D=Division: ' )

    if Operacion.upper() == 'S':
        Calculo.get_suma()
    elif Operacion.upper() == 'R':
        Calculo.get_resta()
    elif Operacion.upper() == 'M':
        Calculo.get_multiplicacion()
    elif Operacion
    Otro = input('Desea Realizar una nueva operacion? S/N ')

    if Otro.upper() == 'S':
        Otro = True
    else:
        Otro = False
# ----- otra opcion hecha por Juan ----------------------
class calculadora:
    def __init__(self, x,y):
        self.value1=x
        self.value2=y

    #Operaciones

    def suma(self):
        res = self.value1 + self.value2
        return(res)
    
    def resta(self):
        res= self.value1 - self.value2
        return(res)
    
    def mult(self):
        res= self.value1 * self.value2
        return(res)

    def div(self):
        res= (self.value1)/(self.value2)
        return(res)
part1=True
prendida = True
operacion=""
res=0
valor1=0
valor2=1
part2=True
while prendida:
    
    while part1:
        try:
            valor1= int(input("Valor nº1: "))
            part1=False
        except ValueError:
            print("Ingrese valor entero")
    part1=True
    res=valor1
    
    part2=True
    while part2:
        print("Seleccione operacion:
                     +. Suma
                     -. Resta
                     /. División
                     *. Multipicación
                     C. Clear
                     AC. Off")
"""
