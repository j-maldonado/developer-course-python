#Validar que el numero ingresado sea un Dni
while True:
    try:
        dni= input('Ingrese su numero de DNI: ')

    except ValueError:
	    print("Su Dni no es válido")

    if len(dni) >=7 and len(dni) <=8 :
        break
    else:
        print("Dni incorrecto, re-ingrese...")
print("Su Dni es válido")