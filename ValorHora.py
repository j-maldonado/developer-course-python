#Calcular el sueldo a pagar de un empleado dadas la cantidad de horas trabajadas y el valor de la mismas
while True:
    try:
        CantHoras = int(input("Ingrese cantidad de Horas Trabajadas: "))
        break
    except ValueError:
        print("Ingresar un Valor NUMERICO")

while True:
    try:
        ValorHora = int(input("Ingrese Valor en $$ de cada Hora: "))
        break
    except ValueError:
        print("Ingresar un Valor NUMERICO")

Sueldo = ValorHora*CantHoras
print('El sueldo a pagar del corriente mes es de', Sueldo)