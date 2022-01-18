#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

palabra1=input('Ingrese la primer palabra: ')
palabra2=input('Ingrese la segunda palabra: ')

if palabra1.isalpha() and palabra2.isalpha():
 
    ultima_tres_p1 = palabra1[-3:] 
    ultima_tres_p2 = palabra2[-3:]
    ultima_dos_p1 = palabra1[-2:]
    ultima_dos_p2 = palabra2[-2:]
 
    if ultima_tres_p1 == ultima_tres_p2:
        print("Las palabras riman")
    elif ultima_dos_p1 == ultima_dos_p2:
        print("Las palabras riman un poco")
    else:
        print("Las palabras no riman")
else:
    print('En algun campo no ingreso letras')
     



