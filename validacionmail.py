#Validar que la direccion ingresado sea un e-mail de la mejor manera
while True:
    try:
        mail = input("Ingrese su e-mail: ")

    except ValueError:
	    print("Su mail no es válido")

    if '@' in mail:
        break
    else:
        print("Email incorrecto, re-ingrese.")
print("Su mail es válido")
