
#Calculadora

calculo= input('Ingrese: suma para SUMAR / resta para RESTAR / multi para MULTIPLICAR / div para DIVIDIR: ' )

if calculo == 'suma' or calculo == 'resta' or calculo== 'multi' or calculo=='div':
    while True:
        try:
            a = int(input('Ingrese el primer numero: '))
            break
        except ValueError:
	        print("Ingrese un Numero")

    while True:
        try:
            b = int(input('Ingrese el segundo numero: '))
            break
        except ValueError:
	        print("Ingrese un Numero")




    if calculo == 'suma':
        suma = a + b
        print(a, '+', b, 'es igual a: ', suma)

    elif calculo == 'resta':
        resta = a-b
        print(a, '-', b, 'es igual a: ', resta)

    elif calculo == 'multi':
        multi = a*b
        print(a, 'x', b, 'es igual a: ', multi)

    elif calculo == 'div':
        if b == 0:
            print('Como vas a dividir por 0?!?!?!')
        else:
            div = a/b
            print(a, '/', b, 'es igual a: ', div)

else:
    print('ingrese alguna funcion valida')