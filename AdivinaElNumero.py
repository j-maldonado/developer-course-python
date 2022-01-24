
import random

# El usuario debe adivinar el número aleatorio generado por la computadora.
def adivina_el_número(x):

    print("============================")
    print("  ¡Bienvenido(a) al Juego!  ")
    print("============================")
    print("Tu meta es adivinar el número")

    número_aleatorio = random.randint(1, x) 

    
    predicción = 0

   
    while predicción != número_aleatorio:
        predicción = int(input(f'Adivina un número entre 1 y {x}: '))
        if predicción < número_aleatorio:
            print('Intenta otra vez. Este número es muy pequeño.')

        elif predicción > número_aleatorio:
            print('Intenta otra vez. Este número es muy grande.')

    print(f'¡Felicitaciones! Adivinaste el número {número_aleatorio} correctamente.')

adivina_el_número(10)