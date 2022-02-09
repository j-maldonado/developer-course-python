#Escribe una función llamada "elimina_duplicados" que elimine los elementos duplicados de una lista y los devuelva en una nueva lista

#!/usr/bin/env python
# -*- coding: utf-8 -*-


ListaRep= [1, 2, 3, 4, 4, 5]
print('lista original ', ListaRep)
Nueva=[]
ListaRepDuplicados=[]
for elemento in ListaRep:
    if elemento not in Nueva:
        Nueva.append(elemento)
    else:
        ListaRepDuplicados.append(elemento)
ListaRepBackup=ListaRep
ListaRep=Nueva
print('La lista original es: ',ListaRepDuplicados)
print ('La lista sin repetidos es: ', ListaRep)