#Es una coleccion de datos que pueden tener, listas tuplas, int, float, etc.

MiAgenda={ #EL DICCIONARIO SE INICIAN DE ESTA MANERA. FINALIZANDO CADA ITEM CON UNA ',' . 
    'Nombre': 'Maria',
    'Apellido': 'Gonzalez',
    'Telefono': '12345678',
    'Direccion': 'Calle Falsa 123',
    'Padres': ['Juan Perez', 'Agustina Crox'], #ES UNA LISTA
    'Hijos': ('Jose', 'Ramon', 'Gisela', 'Romina', 'Jorge'), #ES UNA TUPPLA
}

'''print(MiAgenda['Nombre']) 
print(MiAgenda['Padres'][0:2])
print(MiAgenda['Hijos'])

MiAgenda['Ingresos'] = 200000 #Agregamos la clave ingresos con el valor 200000
print(MiAgenda)

MiAgenda['Salario'] = MiAgenda.pop('Ingresos') #Cambiamos la var 'Ingresos' por 'Salarios'

print(MiAgenda)'''

Nlista = ['Lunes', 'Martes', 'Miercoles'] #Creamos una lista
Elista = [1, 2, 3] #Creamos otra
Diccio = dict(zip(Nlista, Elista)) #Creamos un diccionario llamado 'Diccio' con 'dict' y con 'zip' le decimos que relacion 1 a 1 los valores de cada lista. Es decis el indice 0 de Nlista con el indice 0 de Elista
print(Diccio)