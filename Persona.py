#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y
# “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos.
"""
class Persona:

    # creamos la primera funcion
    # para inicializar el atributo nombre, edad, dni
    def set_nombre(self,nom):
        self.nombre=nom
    def set_edad(self,anios):
        self.edad = anios
    def set_dni(self,doc):
        self.dni = doc
 
    # creamos el segundo metodo
    # para mostrar el nombre, edad, dni
    def get_nombre(self):
        print("Nombre: ",self.nombre)
    def get_edad(self):
        print("Edad: ", self.edad)
    def get_dni(self):
        print("DNI: ", self.dni)
 
#bloque principal
# creamos una instancia de la clase persona
persona1=Persona()
persona1.set_nombre("Pedro")
persona1.get_nombre()

persona1.set_edad(40)
persona1.get_edad()

persona1.set_dni(27123456)
persona1.get_dni()

# creamos un objeto de la clase persona
persona2=Persona()
persona2.set_nombre("Clara")
persona2.get_nombre()

persona2.set_edad(25)
persona2.get_edad()

persona2.set_dni(29098765)
persona2.get_dni()
"""
# clase Humano con metodo contratar
"""
class Humano:     # creamos la clase humano
	def __init__(self, edad, nombre, dni, ocupacion):  # método constructor
		self.edad = edad           
		self.nombre = nombre
		self.dni = dni
		self.ocupacion = ocupacion
		
	def get_persona(self):
		print( "\n"
		"Nombre: ", self.nombre, "\n" 
		"DNI: ", self.dni, "\n"
		"Edad: ", self.edad, "\n"
		"Ocupación: ", self.ocupacion, "\n"
		)
		mostrar = ("Hola soy {}, tengo {} años, mi DNI es {}, y mi ocupacion {}") # mensaje respuesta
		print(mostrar.format(self.nombre, self.edad, self.dni, self.ocupacion))

# Ahora cambiemos un atributo mediante un método para mantener el encapsulamiento:
	def contratar(self, puesto):  #añadimos un nuevo parámetro en el método
		self.puesto = puesto
		print ("{} ha sido contratado como {}".format(self.nombre, self.puesto))
		self.ocupacion = puesto   #Ahora cambiamos el atributo ocupación
"""
"""
#nombre = input("Ingrese el nombre de la persona: ")
#edad = int(input("Ingrese la edad de la persona: "))
#dni = int(input("Ingrese el Nro.de Documento: "))
#ocupacion = input("Ingrese ocupación: ")
nombre = "Blanca"
edad = 35
dni = 29123456
ocupacion = "Docente"
persona3 = Humano(edad, nombre, dni, ocupacion)
persona3.get_persona()
persona3.contratar("Secretaria")  # aqui llamamos al método que cambia el atributo ocupacion
persona3.get_persona() # volvemos a mostrar con el cambio de ocupacion
"""
#def __init__(self):
#    self.var1=2
#    self.var2="hola"
#    self.var3=input("Ingresa un valor: ")
#
#def __init__(self,num1,num2):
#    self.num1=num1
#    self.num2=num2
"""
# ------- Herencia Simple ---------------------------------------------
class Estudiante(object):             #Creamos la clase padre, usamos el parámetro Object que esta definido por defecto en Python
    def __init__(self, edad, nombre): # Definimos los parámetros edad y nombre
        self.edad = edad              #Declaramos que el atributo edad es igual al argumento edad
        self.nombre = nombre          #Declaramos que el atributo nombre es igual al argumento nombre
class Ingenieria(Estudiante):           #Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
                                      #Lo que la convierte a INGENIERIA en una clase hija o secundaria
    def presentarse(self):            #Creamos el método presentarse
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio Ingenieria") #Se presenta llamando los atributos
Clara = Ingenieria(23, 'Clara Fraser') #Indicamos argumentos edad y nombre, instanciamos obj de Ingen. y hereda de Estudiante
Clara.presentarse()                  # Llamamos al método y Clara se presenta
"""
#
# declaramos la clase persona con herencia
#
"""
class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))

    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
#
# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Empleado(Persona,Humano):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))

    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no paga impuestos.")
#
#
# bloque principal
#persona1 = Persona()
#persona1.mostrar()
empleado1 = Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()
"""
#
# -------- Herencia Múltiple ------------------------------------------
#
"""
class Estudiante(object):             #Creamos la clase padre
    def __init__(self, edad, nombre): # Definimos los parámetros edad y nombre
        self.edad = edad              #Declaramos que el atributo edad es igual al argumento edad
        self.nombre = nombre          #Declaramos que el atributo nombre es igual al argumento nombre
class Instituto(object):
    def presentarinstituto (self):
        print("Estudio en el Instituto de Formación Técnica Superior N° 3")
class Ingenieria(Estudiante, Instituto): #Entre paréntesis indicamos la clase padre o principal ESTUDIANTE
                                     #Lo que la convierte a INGENIERIA en una clase hija o secundaria
    def presentarse(self):           #Creamos el método presentarse
       print (f"Soy {self.nombre} tengo {self.edad} años y estudio Ingenieria") #Se presenta llamando los atributos
       
Clara = Ingenieria(26, 'Clara Fraser') #Indicamos argumentos edad y nombre, creamos obj instanciando la clase Ingenieria y hereda de estudiante e instituto
Clara.presentarse()                 # Llamamos al método y Clara se presenta
Clara.presentarinstituto()
"""
# ------------ SUPER clase padre -------------------------------------------
"""
class Padre(object):                 #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo(Padre):                   #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas) #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara             #Especificamos el nuevo atributo para Hijo

# usando super() quedaría:
class HijoS(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        
Tomas = HijoS('Marrones', 'Negras', 'Larga')
print("Los ojos de Tomas son ", Tomas.ojos, ", sus cejas son ", Tomas.cejas, " y su cara ", Tomas.cara)
"""
# ------------- llamar un metodo de otra clase (list) padre con super() --------------------------------
"""
class Agregarelemento(list):    #Creamos una clase Agregarelemento heredando atributos de clase list (clase incorporada)
    def append(self, alumno):   #Definimos que el método append (de listas) añadirá el elemento alumno
        print (("Añadido el alumno"), (alumno)) #Imprimimos el resultado del método
        super().append(alumno)  #Incorporamos la función super SIN INDICAR LA CLASE ACTUAL, seguida
                                #del método append para la variable alumno
Lista1 = Agregarelemento()      #Definimos la clase de nuestra lista llamada "Lista1"
Lista1.append ('Pablo')         #Añadimos un elemento a la lista como lo haríamos normalmente
Lista1.append ('Juan')
print (Lista1)                  #Imprimimos la lista para corroborar que se añadió el alumno
"""
# ------------- Herencia Multiple con función Super() --------------------------------------------
"""
class Perros(object):        #Declaramos la clase principal Perros
    def ladrar (self):
        print ("GUAAAUU GUAAAUU!")
        
    def grunir (self):
        print ("GRRRRRR GRRRRR")
class Caniche (Perros):      #La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("guau guau guau")
        
    def grunir(self):
        print ("gññññiii gñññiiii")
class Pastor_Aleman(Perros):  #La clase secundaria hereda de la clase principal perros
    def ladrar(self):
        print ("GuaUUU GUAAAUUU GuaUUU")
        
    def grunir(self):
        print ("Agrfgregreff aggrrfsgrrr")
    
class Shepadoodle (Caniche, Pastor_Aleman):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()
Marty = Pastor_Aleman()
Apolo = Caniche()
Mezcla = Shepadoodle()
Mezcla.ladrarx(5) # Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
                    #Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
                    #Imprimiria el ladrido del Pastor_Aleman
                    #Y  si borramos ambos? Imprimirá el ladrido de Perros!
"""
# -------------- Herencia Multiple y Atributos no sirve Super(), hay que usar los constructores
# -------------- de las clases especificándolas por su nombre. Y si cambiamos el nombre u orden de
# -------------- la clase debemos especificarlo.
"""
class Padre(object):                 #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
class Madre(object):                 #Creamos la clase Padre llamada Madre
    def __init__(self, brazos, piernas): #Definimos los Atributos
        self.brazos = brazos
        self.piernas = piernas
        
class Hijo(Padre, Madre):            #Creamos clase hija que hereda de Padre y luego de Madre
    def __init__(self, ojos, cejas, cara, brazos, piernas): #creamos el constructor de la clase especificando atributos
        Madre.__init__(self, brazos, piernas)
        Padre.__init__(self, ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara
        
Tomas = Hijo('Marrones', 'Negras', 'Larga', 2, 2)
print (Tomas.ojos, Tomas.cejas, Tomas.cara, Tomas.piernas, Tomas.brazos)
print("Los ojos de Tomas son ", Tomas.ojos, ", sus cejas son ", Tomas.cejas, " y su cara ", Tomas.cara, ", tiene ", Tomas.piernas, " piernas y ", Tomas.brazos, " brazos.")
"""
# -------------- Declaramos Variables de Clase --------------------------------
"""
class Perros (object):
    'Clase para los perros'           #Descripción
    Collar = True                     #Variable de clase Estática
    def __init__(self, salud, hambre):
        self.salud = salud            #Variable de Instancia
        self.hambre = hambre          #Variable de Instancia
print("El perro tiene collar: ", Perros.Collar) #podemos accederla sin crear un objeto(sin instanciar)

# -------------- Accedemos a variables de Instancia ---------------------------

# print (Perros.hambre) #-> ASI NO PODES!, porque hambre es una variable de instancia
#Debes instanciar:
Pequines = Perros(100, 5)
print("¿Cuanto kilos come un Pequines?: ", Pequines.hambre)
"""
# -------------- Metodo de clase usando decorador @classmethod ------------------
"""
class Animal (object):
    @classmethod                         # decorador
    def correr(self, km):
        print ("El animal corre %s kilómetros" % km) #Aquí estamos utilizando format
    'Clase para los animales corredores' #Descripción de esta clase
Animal.correr(12)
"""
# -------------- Metodo de Instancia -------------------------------------------
"""
class Ave (object):
    'Clase para las aves' # Descripcion
    def __init__(self):
        pass              # luego ponemos algo
    
    def hablar (self, color):
        print ("Soy un ave habladora de color %s" %color) #Usamos format
#Ave.hablar ('verde')     #-> No puedes acceder de esta manera porque es un método de instancia
#Debes instanciar (crear un objeto a partir de la clase)
Loro = Ave()
Loro.hablar('verde')      # invocamos al método de instancia
"""
# ------------- Metodo Estático con decorador @staticmethod --------------------
"""
class Ave (object):
    'Clase para las aves' #Descripción
    def __init__(self):
        pass
    
    def hablar (self, color):
        print ("Soy una jodida ave de color %s" %color) #Usamos format
        
    @staticmethod        ### ######decorador staticmethod
    def funcion_volar_ave(tiene_alas, kms): #Definimos el metodo
        #####Condicional####################
        if tiene_alas == True:
            print ("El ave se fue volando %i kilometro" %kms)
        else:
            print ("Este ave no puede volar")
Ave.funcion_volar_ave(True, 1) #Llamamos el método (función) usando la clase
"""
# ------------- Creamos un Decorador -------------------------------------
"""
def decorador(func):           #Creamos la función decorador (A) con el argumento func
    def nueva_funcion():       #Creamos la nueva función (C)
        print ("Perro dice:")  #Añadimos una modificación a la función (B) dentro de (C)
        func()              #Aquí estamos incluyendo la función (B) que le dimos como argumento a (A)
    return nueva_funcion       #Para devolver (C)
@decorador                     #Decoramos la función saluda (solamente)
def saluda():
    print("Guau!")
# @decorador
def despedida():     # si queremos que vuelva a mostrar "Perro dice" debemos colocar entes el decorador
    print ("Chau")
saluda()
despedida()
"""
# -------------- decorador de clase
"""
def decorador(func):         # Damos como argumento del decorador a func
    def nueva_funcion(self, mensaje): #Aquí debemos colocar los parámetros con los que trabaja func
        print ("Perro dice:")#Código decorador
        func(self, mensaje)  #En func agregamos los parámetros con los que trabaja
    return nueva_funcion #Retornamos la nueva función
class perro(object):         #Creamos la clase heredando de object
    def __init__(self, nombre):  #Constructor con el atributo nombre
        self.nombre = nombre #Nombre es igual al argumento nombre etc.
    @decorador               #Aqui antes del método se coloca el decorador!!!
    def saluda(self, mensaje): #Metodo saludar del perro, como siempre
        self.mensaje = mensaje #El parámetro de saluda mensaje es igual a mensaje arg..
        print(mensaje)        #Imprimir el mensaje ATENCIÓN.
        print("Guau!")        #Resto del código
lucifer = perro('Lucifer') #Instanciamos
lucifer.saluda('Juro que me porto bien!') #Cuando llamamos al metodo saluda buscara añadirle el decorador
#Osea que se ira hasta arriba. Por ende allí también debimos incluir la instanciacion (self) y el
#Argumento mensaje para ambas (nueva_funcion) y func.
"""
# -------------
# cambiamos el parámetro “mensaje” por “parametro1” y volvemos a utilizar el método decorado 
# Saluda() y además añadimos otro método llamado Orden() que también es decorado con el mismo decorador.
# cambiamos los parámetros de func() por  parametro1 y self por instanciar. Agregamos otro 
# método al decorador y lo llamamos también.
"""
def decorador(func):
    def nueva_funcion(instancia, parametro1):
        print ("Perro dice:")
        func(instancia, parametro1) 
    return nueva_funcion 
class perro(object):
    def __init__(self, nombre): 
        self.nombre = nombre 
    @decorador 
    def saluda(self, mensaje): 
        self.mensaje = mensaje 
        print(mensaje)
        print("Guau!") 
    @decorador
    def ordeno(self, orden):
        self.orden = orden
        print(orden)
        print("La pata, la pataaaaa! Guau!")
lucifer = perro('Lucifer')
lucifer.saluda('Soy bueno!')
lucifer.ordeno('Doy la pata')
"""
#-------------------- Usando clases como decoradores --------------------------------
# haciendola llamable (invocable) con el método __call__ que nos permite
# emular un objeto como si fuera una función.
"""
#
class midecorador(object):
    def __init__(self, func): #Damos como parámetro una función
        print ("He construido la clase")
        func() #Llamamos a la función
        
    def __call__(self): #La definimos como llamable
        print ("Soy una clase llamada mediante call")
        
def hablar():
    print ("Hola soy la función hablar")
matute = midecorador(hablar) #instanciamos y llamamos la función hablar brindandola como argumento

# Tambien podemos recurrir al @ para decorar sin instanciar:
@midecorador
def habladora():
    print ("Hola soy la función habladora")
"""
#
# Si queremos que la llamada no sea automática, entonces:
#
"""
# 
class midecorador(object):
    def __init__(self, func): #Damos como parámetro una función
        print ("He construido la clase")
        self.func = func #La almacenamos en el constructor
        
        
    def __call__(self): #La definimos como llamable
        print ("Soy una clase llamada mediante call")
        self.func() #Ejecutamos la funcion en call
        
@midecorador
def hablar():
    print ("Hola soy la función hablar")
hablar() #Llamamos la función decorada
"""
#
# Tambien podemos pasarle parámetros/argumentos a esta función usando *args **kargs en call
#
"""
#
class midecorador(object):
	def __init__(self, func):   # pasamos como parámetro una funcion
		print("He construido la clase")
		self.func = func        # la guardamos en el constructor
#
	def __call__(self, *args, **kargs):  # la definimos como llamable
		print("Soy una clase llamada mendiate call")
		self.func(*args, **kargs)        # ejecutamos la funcion en call
#
@midecorador
def hablar(mensaje):
    print (mensaje)
hablar("Soy un argumento para el parámetro mensaje") #Llamamos la función decorada
@midecorador
def habladora(men,men2):
	print(men, men2)
habladora("Mensaje1", "Mensaje2")
"""
#
# Encapsulamiento - Atributos protegidos ("_")
#
"""
class usuario (object):
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self._clave = clave
        
Usuario1 = usuario ("Federico", "qwerty")
print (Usuario1.nombre, Usuario1._clave)
"""
#
# Atributos privados ("__") / solo si llamamos la clase con guion antes _NomClase__atributo
#
"""
class usuario(object):
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.__clave = clave
#
Usuario1 = usuario("Gaston", "qwerty")
print(Usuario1.nombre, Usuario1._usuario__clave)
"""
#
# Property: metodos setter,getter,deleter, doc
#
"""
class Perros(object): #Declaramos la clase principal Perros
    def __init__(self, nombre, peso): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos (privados ocultos)
        self.__peso = peso
    @property
    def nombre(self): #Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla" # Doc del método
        return self.__nombre #Aquí simplemente estamos retornando el atributo privado oculto
#Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
#Ahora vamos a utilizar setter y deleter para modificarlos

    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre) #Aquí vuelvo a pedir que retorne el atributo para confirmar
    @nombre.deleter #Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
        
        #Hasta aquí property#
    def peso(self):    #Definimos el método para obtener el peso
        return self.__peso #Aquí simplemente estamos retornando el atributo privado

#Instanciamos
Tomas = Perros('Tom', 27)
print (Tomas.nombre) #Imprimimos el nombre de Tomas. Se hace a través de getter
#Que en este caso como esta luego de property lo toma como el primer método..
Tomas.nombre = 'Tomasito' #Cambiamos el atributo nombre que se hace a través de setter
del Tomas.nombre #Borramos el nombre utilizando deleter
"""
#
# @property decorador predefinido, se utiliza para devolver los atributos de propiedad de una 
# clase del getter, setter y deleter establecidos como parámetros
# vamos a agregar peso, modificarlo y borrarlo. 
#
"""
class Perros(object):                 #Declaramos la clase principal Perros
    def __init__(self, nombre, peso): #Definimos los parámetros 
        self.__nombre = nombre        #Declaramos los atributos
        self.__peso = peso
    @property   # decorador incorporado en Python
    def nombre(self):                 #Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla" # Doc del método
        return self.__nombre          #Aquí simplemente estamos retornando el atributo privado
#Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
#Ahora vamos a utilizar setter y deleter para modificarlos
    @nombre.setter                    #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre) #Aquí vuelvo a pedir que retorne el atributo para confirmar
    @nombre.deleter                   #Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
        
    @property
    def peso(self):    #Definimos el método para obtener el peso #Automáticamente GETTER
        return self.__peso #Aquí simplemente estamos retornando el atributo privado
    @peso.setter
    def peso(self, nuevopeso):
        self.__peso = nuevopeso
        print ("El peso ahora es")
        print (self.__peso)
    @peso.deleter #Propiedad DELETER
    def peso(self): 
        print("Borrando peso..")
        del self.__peso
#Instanciamos
Tomas = Perros('Tom', 27)
print (Tomas.nombre) #Imprimimos el nombre de Tomas. Se hace a través de getter
#Que en este caso como esta luego de property lo toma como el primer método..
Tomas.nombre = 'Tomasito' #Cambiamos el atributo nombre que se hace a través de setter
print (Tomas.nombre) #Volvemos a imprimir
Tomas.peso = 28
del Tomas.nombre #Borramos el nombre utilizando deleter
"""
#
# ----------------- Polimorfismo -----------------------
# ejemplo de metodo con el mismo nombre en diferentes clases y objetos
#-------------------------------------------------------
"""
class Marino(): #Clase Padre
    def hablar(self): #Método Hablar que no se ejecuta por MRO - Resolucion de ordenes de metodo
        print ("Hola..")
class Pulpo(Marino): #Clase Hija
    def hablar (self): #Método Hablar
        print ("Soy un Pulpo")
class Foca(Marino): #Clase Hija
    def hablar (self, mensaje): #Método Hablar
        print (mensaje)
Pulpito = Pulpo() #Instancia
Foca = Foca() #Instancia
Pulpito.hablar() #Llamamos al método
Foca.hablar("Soy una foca, este es mi mensaje") #Llamamos al método
"""
#
# uso de Import para ejemplificar la modularidad
#
"""
import math            #Importamos el módulo math completo
x = int(input("Ingresa un numeroA: \n"))
raiz = math.sqrt(x)    #Utilizamos la función sqrt del módulo math Raiz cuadrada
print (raiz)
#
# from module import, nos permite importar determinadas funciones de un modulo y no el módulo completo
#
from math import *     #Importamos del módulo math todo lo declarado como explícito, no todo el contenido
y = int(input("Ingresa un numeroB: \n"))
raizb = sqrt(y)         #Utilizamos la función sqrt del módulo math Raiz cuadrada
print (raizb)
#
# podemos importar una determinada funcion en lugar del modulo entero
#
from math import(sqrt)
z = int(input("Ingresa un numeroC: \n"))
raizc = sqrt(z)         #Utilizamos la función sqrt del módulo math Raiz cuadrada
print (raizc)
#
# para saber el contenido de un modulo podemos:
#
import math
print(dir(math))
#
#
# podemos ver modulo o paquetes de terceros junto a su documentación en: https://pypi.org/
# luego lo importamos con pip, ejemplo:  pip install nombredelpaquete
"""
#

#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
#
class Persona():

    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    def validar_dni(self):
        if len(self.__dni) != 8:
            print("DNI incorrecto")
            self.__dni = ""

    @dni.setter
    def dni(self,dni):
        self.__dni=dni
        self.validar_dni()
      
    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad
    
    
    def mostrar(self):
        return "Nombre:"+self.nombre+" - Edad:"+str(self.edad)+" - DNI:"+self.dni

    def esMayorDeEdad(self):
        return self.edad>=18
#
nomApe = input("Ingreso Nombre y Apellido: ")
age = int(input("Ingrese su edad: "))
docu = input("Ingrese su DNI: ")
#
empleado = Persona(nomApe, age, docu)
print("Datos ingresados: ", empleado.mostrar())
print("Es mayor de edad? ", empleado.esMayorDeEdad())
