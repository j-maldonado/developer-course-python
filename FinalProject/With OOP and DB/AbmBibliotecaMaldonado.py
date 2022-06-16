import os
from tkinter.tix import Select
import mariadb

dbbiblioteca = mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="25109",    # no le puse pass a mi base por el momento
    database='biblioteca_Maldonado'
)
cur = dbbiblioteca.cursor()

""" cur.execute("SELECT * FROM libros")    # selecciono todos los registros de mi tabla cliente
myresultado = cur.fetchall()
for ind in myresultado:
  print(ind) """

""" cur = dbbiblioteca.cursor()
cur.execute("CREATE TABLE Libros (USBN INT PRIMARY KEY, Titulo VARCHAR(255), Autor VARCHAR(255), estado VARCHAR(255), dni INT)")
dbbiblioteca.commit()
cur.execute("CREATE TABLE clientes (dni INT PRIMARY KEY, nombre VARCHAR(255), telefono INT, domicilio VARCHAR(255), estado VARCHAR(1), ISBN INT)")
dbbiblioteca.commit()"""

""" sql = "INSERT INTO clientes (dni, nombre, telefono, domicilio, estado, ISBN) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    (36596894, 'Joan Maldonado', 1557558051,
     'Mario Bravo 1155 9C', 'P', 9781569319727),
    (11111111, 'Juan Casal', 123456789,
     'Millan 567', 'D', 0),
    (22222222, 'Homero Simpson', 1122334455,
     'Falsa 123', 'D', 0),
    (33333333, 'Diego de la Vega', 1543212323,
     'Los Angeles 19', 'D', 0),
    (10101010, 'Lionel Messi', 1510101010, 'Laferrere 4800', 'D', 0)

]
cur.executemany(sql, val)
dbbiblioteca.commit()
print(cur.rowcount, "Fueron insertados en tabla Clientes.")
cur = dbbiblioteca.cursor()
sql = "INSERT INTO Libros (ISBN, Titulo, Autor, estado, dni) VALUES (%s, %s, %s, %s, %s)"
val = [
    (9788491295976, 'TODAS ESAS COSAS QUE TE DIRE MAÑANA', 'Elisabet Benavent', 'D', 0),
    (9788423361588, 'EL CAMINO DEL FUEGO', 'Maria Oruña', 'D', 0),
    (9788408252856, 'EL LIBRO NEGRO DE LAS HORAS',
     'Eva Garcia Saenz de Urturi', 'D', 0),
    (9789504975564, 'LA BESTIA', 'Carmen Mola', 'D', 0),
    (9789504975847, 'EL HECHIZO DEL AGUA', 'Florencia Bonelli', 'D', 0),
    (9789877389258, 'LOS DIAS DE LA REVOLUCION', 'Eduardo Sacheri', 'D', 0),
    (9789504976172, 'ESTRES , SUFRIMIENTO Y FELICIDAD',
     'Daniel Lopez Rosetti', 'D', 0),
    (9789500766647, 'VIOLETA', 'Isabel Allende', 'D', 0),
    (9789506446192, 'EL SUSURRO DE LAS MUJERES', 'Gabriela Exilart', 'D', 0),
    (9789504973140, 'CALLES', 'Felipe Pigna', 'D', 0)
]
cur.executemany(sql, val)
dbbiblioteca.commit()
print(cur.rowcount, "Fueron insertados en la tabla BIBLIOTECA.") """


class Libro:
    def __init__(self, ISBN, titulo, autor, estado, DNI):
        self.isbn = ISBN
        self.titulo = titulo
        self.autor = autor
        self.estado = estado
        self.dni = DNI

    def mostrar(self):
        return self.isbn, self.titulo, self.autor, self.estado, self.dni

class Cliente:
    def __init__(self, DNI, nombre, telefono, domicilio, estado, ISBN):
        self.dni = DNI
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        self.estado = estado
        self.isbn = ISBN
    
    def mostrar(self):
        return self.dni, self.nombre, self.telefono, self.domicilio, self.estado, self.isbn

## validaciones para datos de entrada por consola##

##


def seguirONo():
    variable = input(
        "Ingrese 1 para Volver al Menu Principal o 2 para Salir del Programa: ")
    if variable == "1":
        return True
    elif variable == "2":
        return False
    else:
        seguirONo()
##


def sacarTodosLosEspacios(entrada):
    return entrada.replace(" ", "")


def sacarLosEspaciosDeLosCostados(entrada):
    return entrada.strip()


def contarLosCaracteres(entrada):
    return len(entrada)


def validarNumerico(entrada):
    global listaNumeros
    sonTodosNumeros = True
    for i in entrada:
        if i not in listaNumeros:
            sonTodosNumeros = False
            return sonTodosNumeros
    return sonTodosNumeros


def validarSoloLetras(entrada):
    global listaNumeros
    noHayNumeros = True
    for i in entrada:
        if i in listaNumeros:
            noHayNumeros = False
            print("encontre un numero " + i)
            return noHayNumeros

    return noHayNumeros

##fin de validacion para datos de entrada por consola


def pedirIsbn():
    global isbn
    validadorIsbn = False
    ##primero valido que tenga la longitud adecuada, y luego, que sean todos caracteres numericos para el isbn o el dni
    while validadorIsbn == False:
        isbn = input("Ingrese el ISBN del libro: ")
        isbn = sacarTodosLosEspacios(isbn)
        if (contarLosCaracteres(isbn) > 5 and contarLosCaracteres(
                isbn) < 20):  # aca defino cuantos caracteres tiene que tener el ISBN!
            validadorIsbn = validarNumerico(isbn)
        if validadorIsbn == False:
            print(
                "El ISBN está mal ingresado. Debe tener entre 6 y 19 caracteres y sólo contener números.")
    return isbn


def pedirDni():
    global dni
    validadorDni = False
    while validadorDni == False:
        dni = input("Ingrese el DNI del socio: ")
        dni = sacarTodosLosEspacios(dni)
        if (contarLosCaracteres(dni) == 8):
            validadorDni = validarNumerico(dni)
        if validadorDni == False:
            print(
                "El DNI está mal ingresado. Debe tener 8 caracteres, solamente numéricos.")
    return dni

## Para el futuro: parametrizar el ingreso de campos sin numeros y con la misma extension, y aprender a manejar los nombres de las variables a traves del parametro.


def pedirNombre():
    global nombre
    validadorNombre = False
    while validadorNombre == False:
        nombre = input("Ingrese el nombre del socio: ")
        nombre = sacarLosEspaciosDeLosCostados(nombre)
        if(contarLosCaracteres(nombre) > 1 and contarLosCaracteres(nombre) < 30):
            validadorNombre = validarSoloLetras(nombre)
        if validadorNombre == False:
            print(
                "El nombre está mal ingresado. Debe tener entre 2 y 29 caracteres y no contener números.")
    return nombre
##


def pedirApellido():
    global apellido
    validadorApellido = False
    while validadorApellido == False:
        apellido = input("Ingrese el apellido del socio: ")
        apellido = sacarLosEspaciosDeLosCostados(apellido)
        if(contarLosCaracteres(apellido) > 1 and contarLosCaracteres(apellido) < 30):
            validadorApellido = validarSoloLetras(apellido)
        if validadorApellido == False:
            print(
                "El apellido está mal ingresado. Debe tener entre 2 y 29 caracteres y no contener números.")
    return apellido


def pedirTitulo():
    global titulo
    validadorTitulo = False
    while validadorTitulo == False:
        titulo = input("Ingrese el Titulo del libro: ")
        titulo = sacarLosEspaciosDeLosCostados(titulo)
        if(contarLosCaracteres(titulo) > 1 and contarLosCaracteres(titulo) < 200):
            validadorTitulo = True
        if validadorTitulo == False:
            print("El Titulo está mal ingresado. Debe tener entre 2 y 199.")
    return titulo


def pedirAutor():
    global autor
    validadorAutor = False
    while validadorAutor == False:
        autor = input("Ingrese el autor del libro: ")
        autor = sacarLosEspaciosDeLosCostados(autor)
        if(contarLosCaracteres(autor) > 1 and contarLosCaracteres(autor) < 30):
            validadorAutor = validarSoloLetras(autor)
        if validadorAutor == False:
            print(
                "El autor está mal ingresado. Debe tener entre 2 y 29 caracteres y no contener números.")
    return autor


def pedirDireccion():
    global direccion
    validadorDireccion = False
    while validadorDireccion == False:
        direccion = input("Ingrese la direccion: ")
        direccion = sacarLosEspaciosDeLosCostados(direccion)
        if(contarLosCaracteres(direccion) > 7 and contarLosCaracteres(direccion) < 100):
            validadorDireccion = True
        if validadorDireccion == False:
            print("La dirección está mal ingresada. Debe tener entre 8 y 99 caracteres.")
    return direccion


def pedirTelefono():
    global telefono
    validadorTelefono = False
    while validadorTelefono == False:
        telefono = input("Ingrese el telefono del socio: ")
        telefono = sacarTodosLosEspacios(telefono)
        if (contarLosCaracteres(telefono) > 6):
            validadorTelefono = validarNumerico(telefono)
        if validadorTelefono == False:
            print(
                "El telefono está mal ingresado. Debe tener  más de 6 caracteres, solamente numéricos.")
    return telefono


def muestroMenu():
    print("\n\n\n\n****************** ABM BIBLIOTECA *******************")
    print('''\n
    [0] - Consulta de disponibilidad

    [1] - Préstamo de Libro:
        -   Consultar todos los títulos
        -   Registrar préstamo
        -   Registrar Devolución

    [2] - Gestión del cliente:
        -   Alta de cliente
        -   Consulta estado del cliente
        -   Modificar teléfono o direccion del cliente
        -   Eliminar cliente

    [3] - Gestión de Libro:
        -   Alta de Libro
        -   Consultar estado de Libro
        -   Modificar Libro
        -   Eliminar Libro

    [4] - Salir

****************************************************
    ''')

#consulta estado

###########################################################################################################################


listaNumeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
validador = True
while validador == True:
    muestroMenu()
##variables de validacion de prestamo de libros
    global existeCliente
    global existeLibro
    global libroEstaLibre
    global clientePuedeTomarPrestamo
    global libroEstaPrestadoAESTECliente
    global clienteTieneESTELibro
    global quienSeEstaHaciendoElOso
    global libroQueTeEstasAfanando


## fin variables de validacion de prestamo y devolucion  de libros

    opcion = input("Elija la opción deseada:")
    opcion = sacarTodosLosEspacios(opcion)
    print(f"Su Opcion fue {opcion}")
    if opcion == '1':
        opcionPrestamo = input('''
Préstamo de Libro:
    1 - Consultar todos los títulos
    2 - Registrar Préstamo
    3 - Registrar Devolución
    0 - Volver al Menu Anterior
    **********************************
Elija la opción deseada: ''')
        opcionPrestamo = sacarTodosLosEspacios(opcionPrestamo)
        if opcionPrestamo == "1":  # consultar todos los titulos
            sql = "SELECT * FROM libros"
            cur.execute(sql)
            resultado = cur.fetchall()
            print("***************** LIBROS ***************")
            print(
                "{5}{0:^8}{5} {5}{1:^22}{5} {5}{2:^20}{5} {5}{3:^15}{5} {5}{4:^11}{5}".format
                ("ISBN", "Titulo", "Autor", "Estado", "DNI",
                    "|"))
            for ind in resultado:
                print(
                    "{5}{0:>8}{5} {5}{1:22s}{5} {5}{2:20s}{5} {5}{3:>15}{5} {5}{4:>11}{5}".format(ind[0],
                                                                                                    ind[1],
                                                                                                    ind[2],
                                                                                                    ind[3],
                                                                                                    ind[4], "|"))

                print("------------------------------------------------------------")
    ##seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()

        elif opcionPrestamo == "2":  # Registrar prestamo
            print("Se registrará un préstamo con los datos que le pediremos:")
            isbn = pedirIsbn()
            sqlISBN = "Select * from libros Where ISBN ="+str(isbn)
            cur.execute(sqlISBN)
            resultado = cur.fetchall()
            if len(resultado) < 1:
                print(
                    "El ISBN ingresado no coincide con ninguno existente en nuestra biblioteca. ")
            else:
                #instancio el libro
                for ind in resultado:
                    libroEncontrado = Libro(
                        ind[0], ind[1], ind[2], ind[3], ind[4])
                if libroEncontrado.estado == "L":

                    dni = pedirDni()
                    sqlDNI = "Select * from clientes where DNI ="+str(dni)
                    cur.execute(sqlDNI)
                    resultado = cur.fetchall()
                    if len(resultado) < 1:
                        print(
                            "El DNI ingresado no coincide con ninguno de nuestros socios.")
                    else:
                        for ind in resultado:
                            dniEncontrado = Cliente(
                                ind[0], ind[1], ind[2], ind[3], ind[4], ind[5])

                        if dniEncontrado.estado == "L":
                            sqlLibro = "UPDATE libros SET estado = \'O\' , DNI=" + \
                                str(dniEncontrado.dni)+" WHERE ISBN=" +str(libroEncontrado.isbn)
                            sqlCliente = "UPDATE clientes SET estado = \'O\',  ISBN=" + \
                                str(libroEncontrado.isbn)+ " WHERE DNI=" +str(dniEncontrado.dni)
                            cur.execute(sqlLibro)
                            dbbiblioteca.commit()
                            cur.execute(sqlCliente)
                            dbbiblioteca.commit()
                            print("Se le ha prestado  el libro  de ISBN  " +
                      str(libroEncontrado.isbn) + " al socio de DNI " + str(dniEncontrado.dni))

                        else:
                            print("Este cliente ya tiene un libro en prestamo, devuelva el Libro con el ISBN",
                                  dniEncontrado.isbn, "para poder tomar otro.")

                else:
                    print(
                    "Ese libro no esta disponible. Lo tiene en préstamo el cliente con el DNI", libroEncontrado.dni)

            print("Quiere seguir?: ")
            validador = seguirONo()

        elif opcionPrestamo == "3":  # Registrar devolucion
            print("Se registrará una Devolucion con los datos que le pediremos:")
            isbn = pedirIsbn()
            sqlISBN = "Select * from libros Where ISBN ="+str(isbn)
            cur.execute(sqlISBN)
            resultado = cur.fetchall()
            if len(resultado) < 1:
                print(
                    "El ISBN ingresado no coincide con ninguno existente en nuestra biblioteca. ")
            else:
                #instancio el libro
                for ind in resultado:
                    libroEncontrado = Libro(
                        ind[0], ind[1], ind[2], ind[3], ind[4])
                if libroEncontrado.estado == "O":
                    dni = pedirDni()
                    sqlDNI = "Select * from clientes where DNI ="+str(dni)
                    cur.execute(sqlDNI)
                    resultado = cur.fetchall()
                    if len(resultado) < 1:
                        print(
                            "El DNI ingresado no coincide con ninguno de nuestros socios.")
                    else:
                        for ind in resultado:
                            dniEncontrado = Cliente(
                                ind[0], ind[1], ind[2], ind[3], ind[4], ind[5])

                        if dniEncontrado.estado == "O":
                            sqlLibro = "UPDATE libros SET estado = \'L\', DNI=0 WHERE ISBN="+ str(libroEncontrado.isbn)

                            sqlCliente = "UPDATE clientes SET estado = \'L\', ISBN=0 WHERE DNI=" + str(dniEncontrado.dni)
                            cur.execute(sqlLibro)
                            dbbiblioteca.commit()
                            cur.execute(sqlCliente)
                            dbbiblioteca.commit()
                            print("Se ha registrado exitosamente la devolucion del ISBN  " +
                      str(libroEncontrado.isbn) + " correspondiente al socio de DNI " + str(dniEncontrado.dni))

                        else:
                            print("Este cliente no posee un prestamo regsitrado")

                else:
                    print(
                    "El ISBN ingresado no se encuentra en prestamo")

            print("Quiere seguir?: ")
            validador = seguirONo()
##

    elif opcion == "2":
        opcionGestionCli = input('''
- Gestión del cliente:
    1 - Alta de cliente
    2 - Consulta estado del cliente
    3 - Modificar teléfono o direccion del cliente
    4 - Eliminar cliente
    0 - Volver al Menu Anterior
**********************************
Elija la opción deseada: ''')

        opcionGestionCli = sacarTodosLosEspacios(opcionGestionCli)

         #Alta de Cliente
        if opcionGestionCli == '1':
            print("Se agregará un nuevo cliente")
            dni = pedirDni()
            nombre = pedirNombre()
            apellido = pedirApellido()
            telefono = pedirTelefono()
            direccion = pedirDireccion()
            estado = "L"
            isbn = 0
            sqlCliente='SELECT * FROM clientes WHERE DNI ='+str(dni)
            cur.execute(sqlCliente)
            Resultado = cur.fetchall()

            if len(Resultado) <1:
                altaCliente= Cliente(dni, nombre +" "+ apellido, telefono, direccion, estado, isbn)
                sqlAltaCliente= 'INSERT INTO clientes (DNI,nombre, telefono, domicilio, estado, ISBN) VALUES (%s,%s,%s,%s,%s,%s)'
                cur.execute(sqlAltaCliente, altaCliente.mostrar())
                dbbiblioteca.commit()
                print("----Se agregó nuevo Cliente: ",
                      altaCliente.nombre.upper(), '----')
                print("Quiere seguir?")
                validador = seguirONo()
            else:
                print(
                    "Ya existe un cliente con ese DNI en nuestra biblioteca. Por favor, revise los datos.")
                print("Quiere seguir?")
                validador = seguirONo()


        ##Consulta Estado CLIENTE
        elif opcionGestionCli == '2':
            print("Consulta de Estado de cliente")
            dni = pedirDni()
            sqlCliente='SELECT * FROM clientes WHERE DNI ='+str(dni)
            cur.execute(sqlCliente)
            Resultado = cur.fetchall()

            if len(Resultado) <1:
                print(
                    "Ese DNI no coincide con el de ninguno de nuestros clientes. Por favor, revise los datos. ")
            else:
                for ind in Resultado:
                    dniEncontrado=Cliente(ind[0],ind[1],ind[2],ind[3],ind[4],ind[5])

                print(f" --- DATOS DE CLIENTE CONSULTADO ---\n"
                      f"DNI NUMERO: {dniEncontrado.dni}\n"
                      f"NOMBRE Y APELLIDO: {dniEncontrado.nombre}\n"
                      f"DIRECCION: {dniEncontrado.domicilio}\n"
                      f"TELEFONO: {dniEncontrado.telefono}\n"
                      f"ESTADO: {dniEncontrado.estado}")

                if dniEncontrado.estado == "L":
                    print ("PUEDE TOMAR UN LIBRO EN PRESTAMO")
                else:
                    sqlLibro="SELECT * FROM libros WHERE ISBN="+str(dniEncontrado.isbn)
                    cur.execute(sqlLibro)
                    Resultado=cur.fetchall()
                    for ind in Resultado:
                        libroEncontrado=Libro(ind[0],ind[1],ind[2],ind[3],ind[4])

                    print (f"Ya posee en prestamo el Libro:  {libroEncontrado.titulo}")             

    ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()



        #modificar telefono / direccion del socio
        elif opcionGestionCli == '3':
            print("Se modificara el Socio cuyos datos se solicitaran a continuacion:")
            dni = pedirDni()
            sqlCliente='SELECT * FROM clientes WHERE DNI ='+str(dni)
            cur.execute(sqlCliente)
            Resultado = cur.fetchall()

            if len(Resultado) <1:
                print(
                    "Ese DNI no coincide con el de ninguno de nuestros clientes. Por favor, revise los datos. ")
              
            else:
                for ind in Resultado:
                    dniEncontrado=Cliente(ind[0],ind[1],ind[2],ind[3],ind[4],ind[5])

                Modifcliente = input(
                    'Modificar Direccion del socio presione 1; Si quiere modificar el Telefono presione 2: ')
                if Modifcliente == '1':
                    direccion = input(
                        "Ingrese el nuevo Domicilio del Cliente: ")
                    sqlModifDomicilio="UPDATE clientes SET domicilio=\'"+ direccion+"\' WHERE dni="+ str(dniEncontrado.dni)
                    cur.execute(sqlModifDomicilio)
                    dbbiblioteca.commit()
                    print("Ahora el cliente del DNI "+str(dniEncontrado.dni) +
                          " su direccion es " + direccion)


                elif Modifcliente == '2':
                    telefono = input("Ingrese el nuevo Telefono del Cliente: ")
                    sqlModifTelefono="UPDATE clientes SET telefono="+ telefono +" WHERE dni="+ str(dniEncontrado.dni)
                    cur.execute(sqlModifTelefono)
                    dbbiblioteca.commit()
                    print("Ahora el cliente del DNI " +
                          str(dniEncontrado.dni) +"; tiene el Tel "+telefono)
                else:
                    print("No se ha elegido una opción válida")
                    ## seguir o salir
                    print("Quiere seguir?")
                    validador = seguirONo()
            print("Quiere seguir?")
            validador = seguirONo()

        #ELIMINAR SOCIO
        elif opcionGestionCli == '4':
            print('Se eliminara el socio')
            dni = pedirDni()
            sqlCliente='SELECT * FROM clientes WHERE DNI ='+str(dni)
            cur.execute(sqlCliente)
            Resultado = cur.fetchall()
            if len(Resultado) <1:
                print(
                    "Ese DNI no corresponde a ninguno de nuestros socios, por lo tanto, no se borrara ningun socio.")
                seguirONo()


            else:
                for ind in Resultado:
                    dniEncontrado=Cliente(ind[0],ind[1],ind[2],ind[3],ind[4],ind[5])
                if dniEncontrado.estado=='O':
                    print("El cliente de DNI " + str(dniEncontrado.dni)+" tiene en prestamo el libro de ISBN " +
                        str(dniEncontrado.isbn) + "realice la devolucion para poder ser dado de baja")
                    seguirONo()
                else:
                    decision = input(
                        '***ATENCION ESTA POR ELIMINAR DEFINITIVAMENTE EL CLIENTE***\n Si desea continuar presione S o si desea volver al menu presione N: ')
                    decision = decision.upper()
                    if decision == 'S':
                        sqlEliminarCliente='DELETE FROM clientes WHERE DNI='+str(dniEncontrado.dni)
                        cur.execute(sqlEliminarCliente)
                        dbbiblioteca.commit()
                        print('----Se ha eliminado el cliente con el DNI: ', str(dniEncontrado.dni), '----')

                    elif decision == 'N':
                        print('Ha seleccionado que NO. Vuelve al Menu Principal\n')
                        seguirONo()
                    else:
                        print("La opcion ingresada no es correcta")
        ## seguir o salir
                        print("Quiere seguir?")
                        validador = seguirONo()

        elif opcionGestionCli == '0':
            validador = True
        else:
            print("No se ha elegido una opción válida")
            ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()



    elif opcion == "3":
        opcionGestionLib = input('''
Gestión de Libro:
    1 - Alta de Libro
    2 - Consultar un libro
    3 - Modificar Libro
    4 - Eliminar Libro
    0 - Volver al Menu Anterior
**********************************
Elija la opción deseada: ''')

        #Alta de Libro
        if opcionGestionLib == "1":
            print("Se agregará un nuevo Libro.")
            isbn = pedirIsbn()
            titulo = pedirTitulo()
            autor = pedirAutor()
            estado = "L"
            dni = 0
            sqlLibro='SELECT * FROM libros WHERE ISBN ='+str(isbn)
            cur.execute(sqlLibro)
            Resultado = cur.fetchall()

            if len(Resultado) <1:
                altaLibro= Libro(isbn, titulo, autor, estado, dni)
                sqlAltaLibro= 'INSERT INTO libros (ISBN,titulo, autor, estado, DNI) VALUES (%s,%s,%s,%s,%s)'
                cur.execute(sqlAltaLibro, altaLibro.mostrar())
                dbbiblioteca.commit()

                print("----Se agregó el Libro ", altaLibro.titulo.upper(), '----')
                print("Quiere seguir?")
                validador = seguirONo()
            else:
                print("Ya existe un libro con ese ISBN. Por favor, revise los datos.")
                print("Quiere seguir?")
                validador = seguirONo()
        
        ###Consulta Estado LIBRO
        elif opcionGestionLib == "2":
            print("Consulta de Estado de Libro")
            isbn = pedirIsbn()
            sqlLibro='SELECT * FROM libros WHERE ISBN ='+str(isbn)
            cur.execute(sqlLibro)
            Resultado = cur.fetchall()
            if len(Resultado) <1:
                print(
                    "El libro con el ISBN ingresado no corresponde a un item de esta biblioteca. Por favor chequee los datos.")
            else:
                for ind in Resultado:
                    isbnEncontrado=Libro(ind[0],ind[1],ind[2],ind[3],ind[4])

                print(f" --- DATOS DE LIBRO CONSULTADO ---\n"
                      f"ISBN NUMERO: {isbnEncontrado.isbn}\n"
                      f"TITULO: {isbnEncontrado.titulo}\n"
                      f"AUTOR: {isbnEncontrado.autor}\n"
                      f"ESTADO: {isbnEncontrado.estado}")

                if isbnEncontrado.estado =='L':
                    print(f"ESTE LIBRO PUEDE SER PRESTADO")

                else:
                    sqlCliente="SELECT * FROM clientes WHERE DNI="+str(isbnEncontrado.dni)
                    cur.execute(sqlCliente)
                    Resultado=cur.fetchall()
                    for ind in Resultado:
                        dniEncontrado=Cliente(ind[0],ind[1],ind[2],ind[3],ind[4],ind[5])
                    
                    print (f"El libro se encuentra en prestamo al Cliente con DNI: {dniEncontrado.dni}")

  
    ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()

        #Modificar Libro
        elif opcionGestionLib == "3":
            print("Se modificara el libro cuyos datos se solicitaran a continuacion:")
            isbn = pedirIsbn()
            sqlLibro='SELECT * FROM libros WHERE ISBN ='+str(isbn)
            cur.execute(sqlLibro)
            Resultado = cur.fetchall()
            
            if len(Resultado) <1:
                print(
                    "No existe en nuestra biblioteca un libro con ese ISBN. Revise los datos.")

            else:
                for ind in Resultado:
                    isbnEncontrado=Libro(ind[0],ind[1],ind[2],ind[3],ind[4])
                titulo = pedirTitulo()
                autor = pedirAutor()
                sqlModifTituloAutor="UPDATE libros SET titulo=\'"+ titulo+"\',autor=\'"+ autor+"\' WHERE isbn="+ str(isbnEncontrado.isbn)
                cur.execute(sqlModifTituloAutor)
                dbbiblioteca.commit()
                print("Ahora el libro del ISBN "+str(isbnEncontrado.isbn) +
                      "; se llama "+ titulo +"; y su autor es " + autor)

    ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()

        #Eliminar LIBRO
        elif opcionGestionLib == "4":
            print('Se eliminara el Libro')
            isbn = pedirIsbn()
            sqlLibro='SELECT * FROM libros WHERE ISBN ='+str(isbn)
            cur.execute(sqlLibro)
            Resultado = cur.fetchall()
            if len(Resultado) <1:
                print(
                    "Ese libro no existe en nuestra biblioteca, por lo tanto, no se puede borrar.")
                seguirONo()
            else:
                for ind in Resultado:
                    isbnEncontrado=Libro(ind[0],ind[1],ind[2],ind[3],ind[4])

                if isbnEncontrado.estado == "O":
                    print("El libro de ISBN "+str(isbnEncontrado.isbn) + " esta prestado al socio con el DNI  " + str(isbnEncontrado.dni) + "realice la devolucion para poder dar de baja el Libro.")
                    seguirONo()

                else:
                    decision = input(
                        f'\n***ATENCION ESTA POR ELIMINAR DEFINITIVAMENTE EL LIBRO -- {isbnEncontrado.titulo} DEL AUTOR {isbnEncontrado.autor}--***\n Si desea continuar presione S o si desea volver al menu presione N: ')
                    decision = decision.upper()
                    if decision == 'S':
                        sqlEliminarLibro='DELETE FROM libros WHERE ISBN='+str(isbnEncontrado.isbn)
                        cur.execute(sqlEliminarLibro)
                        dbbiblioteca.commit()
                        print(f'----Se ha eliminado el Libro -- {isbnEncontrado.titulo} DEL AUTOR {isbnEncontrado.autor} ----')
                        seguirONo()
                    elif decision == 'N':
                        print(
                            '----Ha seleccionado que NO. No se ha eliminado el libro----\n')
                        seguirONo()
                    else:
                        print("La opcion ingresada no es valida")
                        seguirONo()
                    
        elif opcionGestionLib == "0":
            validador = True

    #SALIR
    elif opcion == "4":
        print("Gracias por elegir nuestro programa.")
        validador = False

    #CONSULTAR ESTADO DE LIBRO
    elif opcion == "0":
        print("Que libro quiere consultar?")
        isbn = pedirIsbn()
        sqlIsbn="SELECT * FROM libros WHERE ISBN="+str(isbn)
        cur.execute(sqlIsbn)
        Resultado=cur.fetchall()
        if len(Resultado)<1:
            print(f"El ISBN ingresado no coincide con ninguno en nuestra base de datos")
        else:
            for ind in Resultado:
                print(f" --- DATOS DE LIBRO CONSULTADO ---\n"
                      f"ISBN: {ind[0]}\n"
                      f"TITULO: {ind[1]}\n"
                      f"AUTOR: {ind[2]}\n"
                      f"ESTADO: {ind[3]}\n"
                      f"DNI CLIENTE QUE LO TIENE: {ind[4]}")
        print("Quiere seguir?")
        validador = seguirONo()

    else:
        print("No se ha elegido una opción válida")
        ## seguir o salir
        print("Quiere seguir?")
        validador = seguirONo()
