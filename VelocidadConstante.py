#Calcular la distancia recorrida a velocidad constante dad la velocidad en km/h
while True:
    try:
        Velocidad = int(input("Ingrese la Velocidad Constante en Km/h: "))
        break
    except ValueError:
        print("Ingrese un Numero")

while True:
    try:
        Tiempo = int(input('Ingrese el Tiempo en minutos que se mantuvo la velocidad colocada anteriormente: '))
        break
    except ValueError:
        print("Ingrese un Numero")

Distancia = Velocidad*(Tiempo/60)
print('La Distancia recorrida durante', Tiempo, 'minutos a', Velocidad, 'Km/h es de ', Distancia, 'Kilometros')