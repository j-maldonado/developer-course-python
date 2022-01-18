#Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película y posterior a ello pide que el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

ListaCat = ['1- Accion ($10)\n', '2- Terror ($8)\n', '3- Suspenso ($5)\n', '4- Comedia ($11)']


while True:
    try:
        print(''.join(ListaCat))
        cate= int(input("\nSeleccione la categoria: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")
    

while True:
    try:
        dias= int(input("Ingrese la cantidad de dias de alquiler: " ))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")


if cate > 0 and cate <=4:
    if cate == 1:
        total= dias*10
        print ('El valor sus', dias, 'dias de alquiler de ACCION es de: $',total)

    elif cate == 2:
        total= dias*8
        print ('El valor sus', dias, 'dias de alquiler de TERROR es de: $',total)


    elif cate == 3:
        total= dias*5
        print ('El valor sus', dias, 'dias de alquiler de SUSPENSO es de: $',total)


    elif cate == 4:
        total= dias*11
        print ('El valor sus', dias, 'dias de alquiler de COMEDIA es de: $',total)

else:
    print('Ingrese una seleccion de categoria de 1 al 4')





