#Son una coleccion de Constantes. Son similares a una lista pero su contenido no es modificable

MesTupla=('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
SemanaTupla=('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')

"""EjemTupla= MesTupla+SemanaTupla

print(EjemTupla)"""

# Definir una función que calcule la longitud de una lista o una cadena dada #

def longitud(valor):
    # Validación. No aceptamos otra cosa que no sea una lista (list) o una cadena (str)
    if type(valor) is not list and type(valor) is not str:
        return -1
    # Contador que vamos incrementando en cada iteración
    contador = 0
    # Mientras haya datos que iterar, aumentar el contador
    # Nota: si es str, iteramos letra por letra.
    # si es list, iteramos elemento por elemento
    for elemento in valor:
        contador += 1
    return contador


cadena = "Hola Clase"
print("Longitud de la cadena 1:", longitud(cadena))
cadena2 = "Hola a Todos x2"
print("Longitud de la cadena 2:", longitud(cadena2))
lista = ["Elemento1", "Elemento2", "Elemento3"]
print("Longitud de lista:", longitud(lista))

