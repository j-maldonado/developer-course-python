while True:
    try:
        Nota1= int(input("Ingrese la Nota 1: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        Nota2= int(input("Ingrese la Nota 2: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        Nota3= int(input("Ingrese la Nota 3: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        Nota4= int(input("Ingrese la Nota 4: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        Nota5= int(input("Ingrese la Nota 5: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        Nota6= int(input("Ingrese la Nota 6: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        Nota7= int(input("Ingrese la Nota 7: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

Promedio = ((Nota1 + Nota2 + Nota3 + Nota4 + Nota5 + Nota6 + Nota7 ) / 7 )
print ('El Promedio de los Datos Ingresados es:', Promedio)