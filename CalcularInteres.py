# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión
while True:
    try:
        pesos = float(input('Capital inicial: '))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        interes = float(input('Interes anual: '))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

while True:
    try:
        anios = int(input('Cantidad de anios: '))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")


 
capObt = (pesos * (1 + interes/100) ** anios)
 
print('El capita total al cabo de ', anios, 'anios sera de ', capObt)