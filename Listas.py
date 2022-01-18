provinlist = ["Buenos Aires", "Salta", "Jujuy", "Mendoza", "Chaco", "Formosa", "Misiones", "Corrientes", "Entre Rios", "La Pampa"]

"""provinlist.append(input("Ingrese nueva provincia: ")) # '.append' suma a la lista en el ultimo lugar
print(provinlist)

del provinlist[2] # 'del' elimina de la lista de la posicion indicada
print(provinlist) 

provinlist.insert(2, 'Jujuy') # '.insert' pones la posicion (ej:2,) y luego el valor que queres agregar (ej: 'Jujuy) 
print(provinlist)

print(sorted(provinlist)) # 'sorted' acomoda los trings de la lista en orden alfabetico 
print(len(provinlist)) # 'len' cuenta la cantidad de variables ingresadas en la lista

print(provinlist)
elimProv= provinlist.pop(2) #Creo una variable, donde le digo que con '.pop()' y en el () poniendo el orden de la variable, GUARDE EL ELEMENTO 'Eliminado'. '.pop()' te permite hacer algo con el elemento que sacas, aparte de sacarlo, o sea, lo podes meter en otro lado.

print(provinlist)
"""



#---------------------------EJERCICIO--------------------------------#

#Dados los meses del año definidos en una lista, eliminar el mes 7 y guardarlo en una variable, mostrar los meses ordenados de forma ascendente, la variable de elemento eliminado y agregar un elemento Biciesto


Meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

"""elimMes= Meses.pop(6)
Meses.append('Biciesto')
print(sorted(Meses))
print('El mes eliminado es', elimMes)"""


#----------------------------Clase 30-09---------------------------------#

Meses.remove('Marzo') # '.remove se usa para eliminar un elemento de la lista especifico
print(Meses)












