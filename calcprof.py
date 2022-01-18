#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################### BLOQUE-1-##################################################
def sumar():         #Definimos la función sumar
    resul = numA + numB
    print("Resultado", resul)
def restar():        #Definimos la función restar
    resul = numA - numB
    print("Resultado", resul)
def multiplicar():   #Definimos la función multiplicar
    resul = numA * numB
    print("Resultado", resul)
def dividir():       #Definimos la función dividir
    resul = numA / numB
    print("Resultado", resul)
##################################### BLOQUE-2-###################################################
while True:          #Creamos un bucle
    try:             #Intentamos obtener los datos de entrada
        numA = int(input("Ingresa el primer numero: \n"))    #pido 1er numero al usuario
        numB = int(input("Ingresa el segundo numero: \n"))   #pido 2do numero al usuario
        print("Que calculo quieres realizar entre", numA, "y", numB, "?\n") #Preguntamos el calc
        opcion = str(input(""" #Ofrecemos las opciones de cálculo las cuales van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
#################################### BLOQUE-3-##################################################
        if opcion == '1':        # Si el usuario elige opción 1 llamamos a sumar
            sumar()
            break
        elif opcion == '2':      # Si el usuario elige opción 2 llamamos a restar
            restar()
            break
        elif opcion == '3':      # Si el usuario elige opción 3 llamamos a multiplicar
            multiplicar()
            break    
        elif opcion == '4':      # Si el usuario elige opción 4 llamamos a dividir
            dividir()
            break
        else:
            print ("""Opcion incorrecta, re-intente""") 
    except ZeroDivisionError:
        print ("No se permite dividir por cero, intenta otro calculo!")
    except:
        print ("Error de ingreso, re-intente")
        opcion = '?'
    finally:
        print ("Gracias por utilizar nuestra calculadora")