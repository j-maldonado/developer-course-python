#!/usr/bin/env python
#-*- coding: utf-8 -*-

payaso = 11.2
munieca = 7.5

while True:
    try:
        payasoped =int(input('Ingrese la cantidad de Payasos del pedido: '))
        break
    except ValueError:
        print("Ingresar un Valor NUMERICO")
 
while True:
    try:
        muniecaped =int(input('Ahora ingrese la cantidad de Muniecas del pedido: '))
        break
    except ValueError:
        print("Ingresar un Valor NUMERICO")

pedido= (payasoped*payaso)+(muniecaped*munieca)

print('El pesaje total de su pedido es de ', pedido, 'gramos.')