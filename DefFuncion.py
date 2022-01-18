
""" Serie fibonacci INPUT
while True:
    try:
        numLimite = int(input('Ingrese limite para la serie Fibonacci: '))
    except ValueError:
        print ('Debes escribir un numero')
    
    if numLimite < 0:
        print('El valor debe ser mayor a 0')
    else:
        break



def fibo (numLimite) : # 'def' define una funcion y luego el nombre y entre () el parametro que utiliza
    serie=[0,1]
    uno= 0
    dos= 1
    tres= 0 
    while tres < numLimite:
        tres = uno + dos
        if tres < numLimite:
            serie.append(tres)
            uno = dos
            dos = tres
    print(serie)

fibo(numLimite)"""

##Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse“.


cadena = input('Ingrese la cadena que desea invertir: ')


def invertir_cadena(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

print (invertir_cadena(cadena))


