#Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto. Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    try:
        anio=int(input('Ingrese el anio a evaluar: '))
        break
    except ValueError:
        print('Ingrese un dato numerico, reingrese...')


def es_bisiesto(anio):
    if anio % 4 != 0: #no divisible entre 4
	    print("No es bisiesto")

    elif anio % 4 == 0 and anio % 100 != 0: #divisible entre 4 y no 100 o 400
	    print("Es bisiesto")

    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: #divisible en 4 y 10 y no en 400
	    print("No es Bisiesto")

    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: #divisible entre 4, 100 y 400
	    print("Es Bisiesto")


es_bisiesto(anio)