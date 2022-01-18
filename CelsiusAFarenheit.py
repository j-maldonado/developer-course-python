while True:
    try
        Celsius = int(input("Ingrese cantidad de Grados Celsius a convertir: "))
        break
    except ValueError:
        print("Ingrese un Valor Numerico")

Farenheit = Celsius*1.8+32
print(Celsius, 'Grados Celsius es igual a ', Farenheit, ' Grados Farenheit')