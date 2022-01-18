Selec = input("Ingrese 1 para PIES o 2 para PULGADAS: ")

if Selec == '1':
    pies = int (input ('Ingrese Cantidad de Pies a convertir: '))
    piesaCm = pies*30.48
    print(pies, 'pies es igual a ', piesaCm, 'cm')

elif Selec == '2':
    pulgadas=int (input ('Ingrese cantidad de pulgadas a convertir: '))
    pulgadasaCm = pulgadas*2.54
    print(pulgadas, 'pulgadas es igual a ', pulgadasaCm, 'cm')

else:
	print("La opcion ingresada no es valida")




