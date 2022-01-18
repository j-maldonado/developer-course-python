#!/usr/bin/env python
# -*- coding: utf-8 -*-

nombre = input('Ingrese su NOMBRE: ')
apellido = input ('Ingrese su APELLIDO: ')


while True:
    try:
      sbruto= float(input("Indique el sueldo BRUTO: "))
      break
    except ValueError:
        print("Ingrese un Valor Numerico")


while True:
    try:
      antiguedad= float(input("Indique anios de antiguedad: "))
      break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
      hijos= float(input("Indique cantidad de hijos: "))
      break
    except ValueError:
        print("Ingrese un Valor Numerico")


antiguedadtotal = (sbruto*antiguedad/100)
asigfamil = (hijos*5)*sbruto/100
simponible = sbruto + asigfamil + antiguedadtotal
descuento = simponible*11/100
sneto = simponible - descuento
print('\n sueldo', nombre.upper(), apellido.upper(),'=', 
      '\n - Sueldo Bruto:...............',sbruto, 
      '\n - Asignacion Familiar:........',asigfamil,
      '\n - Bonificacion Antiguedad:....',antiguedadtotal,
      '\n - Descuento de 11%:...........',descuento,
      '\n --------------------------------------',
      '\n SUELDO NETO:..................',sneto, '\n')


