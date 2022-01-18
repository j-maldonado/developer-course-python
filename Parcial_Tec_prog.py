#Según dos cifras ingresadas determinar los numeros primos entre ambas cifras inclusive y mostrarlos en una lista.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    try:
        N1= int(input("Ingrese el primer numero (EL MENOR): "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        N2= int(input("Ingrese el primer numero (EL MAYOR): "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

Lista= list(range(N1, N2 +1))
ListaNPrimos=[]

def EsPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


for i in Lista:
    if EsPrimo(i) and (i!= 1):
        ListaNPrimos.append(i)
    

print("los números primos son: ", ListaNPrimos )
