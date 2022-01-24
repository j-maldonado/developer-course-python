import os
## validaciones para datos de entrada por consola##

##
def seguirONo():
    variable = input("Ingrese 1 para Volver al Menu Principal o 2 para Salir del Programa: ")
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
            print("encontre un numero " +i)
            return noHayNumeros

    return noHayNumeros

##fin de validacion para datos de entrada por consola

def  pedirIsbn():
    global isbn
    validadorIsbn = False
    ##primero valido que tenga la longitud adecuada, y luego, que sean todos caracteres numericos para el isbn o el dni
    while validadorIsbn == False:
        isbn = input("Ingrese el ISBN del libro: ")
        isbn = sacarTodosLosEspacios(isbn)
        if (contarLosCaracteres(isbn) > 5 and contarLosCaracteres(
                isbn) < 20):  ##aca defino cuantos caracteres tiene que tener el ISBN!
            validadorIsbn = validarNumerico(isbn)
        if validadorIsbn == False:
            print("El ISBN está mal ingresado. Debe tener entre 6 y 19 caracteres y sólo contener números.")
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
            print("El DNI está mal ingresado. Debe tener 8 caracteres, solamente numéricos.")
    return dni

## Para el futuro: parametrizar el ingreso de campos sin numeros y con la misma extension, y aprender a manejar los nombres de las variables a traves del parametro.
def pedirNombre():
    global nombre
    validadorNombre=False
    while validadorNombre==False:
        nombre=input("Ingrese el nombre del socio: ")
        nombre=sacarLosEspaciosDeLosCostados(nombre)
        if(contarLosCaracteres(nombre)>1 and contarLosCaracteres(nombre)<30):
            validadorNombre=validarSoloLetras(nombre)
        if validadorNombre==False:
            print("El nombre está mal ingresado. Debe tener entre 2 y 29 caracteres y no contener números.")
    return nombre
##
def pedirApellido():
    global apellido
    validadorApellido=False
    while validadorApellido==False:
        apellido=input("Ingrese el apellido del socio: ")
        apellido=sacarLosEspaciosDeLosCostados(apellido)
        if(contarLosCaracteres(apellido)>1 and contarLosCaracteres(apellido)<30):
            validadorApellido=validarSoloLetras(apellido)
        if validadorApellido==False:
            print("El apellido está mal ingresado. Debe tener entre 2 y 29 caracteres y no contener números.")
    return apellido

def pedirTitulo():
    global titulo
    validadorTitulo=False
    while validadorTitulo==False:
        titulo=input("Ingrese el Titulo del libro: ")
        titulo=sacarLosEspaciosDeLosCostados(titulo)
        if(contarLosCaracteres(titulo)>1 and contarLosCaracteres(titulo)<200):
            validadorTitulo=True
        if validadorTitulo==False:
            print("El Titulo está mal ingresado. Debe tener entre 2 y 199.")
    return titulo

def pedirAutor():
    global autor
    validadorAutor=False
    while validadorAutor==False:
        autor=input("Ingrese el autor del libro: ")
        autor=sacarLosEspaciosDeLosCostados(autor)
        if(contarLosCaracteres(autor)>1 and contarLosCaracteres(autor)<30):
            validadorAutor=validarSoloLetras(autor)
        if validadorAutor==False:
            print("El autor está mal ingresado. Debe tener entre 2 y 29 caracteres y no contener números.")
    return autor

def pedirDireccion():
    global direccion
    validadorDireccion=False
    while validadorDireccion==False:
        direccion=input("Ingrese la direccion: ")
        direccion=sacarLosEspaciosDeLosCostados(direccion)
        if(contarLosCaracteres(direccion)>7 and contarLosCaracteres(direccion)<100):
            validadorDireccion=True
        if validadorDireccion==False:
            print("La dirección está mal ingresada. Debe tener entre 8 y 99 caracteres.")
    return direccion

def pedirTelefono():
    global telefono
    validadorTelefono = False
    while validadorTelefono == False:
        telefono = input("Ingrese el telefono del socio: ")
        telefono = sacarTodosLosEspacios(telefono)
        if (contarLosCaracteres(telefono)> 6):
            validadorTelefono = validarNumerico(telefono)
        if validadorTelefono == False:
            print("El telefono está mal ingresado. Debe tener  más de 6 caracteres, solamente numéricos.")
    return telefono


def muestroMenu():
    print("****************** ABM BIBLIOTECA *******************")
    print('''
    0 - Consulta de disponibilidad
    1 - Préstamo de Libro:
        - Consultar todos los títulos
        - Registrar préstamo
        - Registrar Devolución
    2 - Gestión del cliente:
        - Alta de cliente
        - Consulta estado del cliente
        - Modificar teléfono o direccion del cliente
        - Eliminar cliente
    3 - Gestión de Libro:
        - Alta de Libro
        - Consultar un libro
        - Modificar Libro
        - Eliminar Libro
    4 - Salir

****************************************************
    ''')

#consulta estado
def consulta_estado(isbn):
    with open("libros.txt", "r") as jArchi:
        linea = jArchi.readline()
        while linea != "":
            renglon = linea.split(',')
            if isbn == renglon[0]:
                enLinea=consulta_libro(isbn)
                titulo=enLinea[1]
                autor=enLinea[2]
                if (str (enLinea[3])=="L"):
                    return('El libro '+ titulo +' de '+ autor +' se encuentra Disponible')
                    
                if (str(enLinea[3])=="O"):
                    return ('El libro '+ titulo +' de '+ autor +' se encuentra Prestado')
            linea = jArchi.readline()
        else:
            return("El libro con el ISBN solicitado no se encuentra en esta biblioteca.")

        
    

def validarExisteCliente(dni):
    global existeCliente
    existeCliente = False

    with open("clientes.txt", "r") as rValExiCliArchi:
        with open("clientesCopy.txt", "w") as wValExiCliArchi:
            linea = rValExiCliArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if (str(dni) == str(renglon[0])):
                    existeCliente = True

                else:
                    wValExiCliArchi.write(linea)
                linea = rValExiCliArchi.readline()
            wValExiCliArchi.close()
        rValExiCliArchi.close()


def validarExisteLibro(isbn):
    global existeLibro
    existeLibro = False

    with open("libros.txt", "r") as rValExiLibArchi:
        with open("librosCopy.txt", "w") as wValExiLibArchi:
            linea = rValExiLibArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if (str(isbn) == str(renglon[0])):
                    existeLibro = True

                else:
                    wValExiLibArchi.write(linea)
                linea = rValExiLibArchi.readline()
            wValExiLibArchi.close()
        rValExiLibArchi.close()


def alta_libro(isbn, titulo, autor, estado, dni):
    with open("libros.txt", "a") as jArchi:
        jArchi.write(str(isbn) + "," + str(titulo) + "," + str(autor) + "," + str(estado) + "," + str(dni) + ","+"\n")
        jArchi.close()
###############################################################################################################
###############################################################################################################
def modificarLibro(isbn,titulo, autor):
    with open("libros.txt", "r") as rModLibArchi:
        with open("librosCopy.txt", "w") as wModLibArchi:
            linea = rModLibArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if isbn == renglon[0]:
                    wModLibArchi.writelines(
                        renglon[0]+ "," +titulo + "," + autor + "," + renglon[3] + "," +renglon[4]+"," + "\n")
                else:
                    wModLibArchi.write(linea)
                linea = rModLibArchi.readline()
            wModLibArchi.close()
        rModLibArchi.close()
    with open("librosCopy.txt", "r") as fcopia:
        with open("libros.txt", "w") as foriginal:
            for registro in fcopia:
                foriginal.write(registro)
            fcopia.close()
        foriginal.close()
########################################################
def modificarCliente(dni, telefono, direccion):
    with open("clientes.txt", "r") as rModCliArchi:
        with open("clientesCopy.txt", "w") as wModCliArchi:
            linea = rModCliArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni == renglon[0]:
                    wModCliArchi.writelines(
                        renglon[0] + "," + renglon[1]+ "," + telefono + "," + direccion + "," + renglon[4] + "," + renglon[5] +","+"\n")
                else:
                    wModCliArchi.write(linea)
                linea = rModCliArchi.readline()
            wModCliArchi.close()
        rModCliArchi.close()
    with open("clientesCopy.txt", "r") as fcopia:
        with open("clientes.txt", "w") as foriginal:
            for registro in fcopia:
                foriginal.write(registro)
            fcopia.close()
        foriginal.close()

################################################################33
def modificarDirecCliente(dni, direccion):
    with open("clientes.txt", "r") as rModCliArchi:
        with open("clientesCopy.txt", "w") as wModCliArchi:
            linea = rModCliArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni == renglon[0]:
                    wModCliArchi.writelines(
                        renglon[0] + "," + renglon[1]+ "," + renglon[2] + "," + direccion + "," + renglon[4] + "," + renglon[5] +","+"\n")
                else:
                    wModCliArchi.write(linea)
                linea = rModCliArchi.readline()
            wModCliArchi.close()
        rModCliArchi.close()
    with open("clientesCopy.txt", "r") as fcopia:
        with open("clientes.txt", "w") as foriginal:
            for registro in fcopia:
                foriginal.write(registro)
            fcopia.close()
        foriginal.close()
###########################################################
def modificarTelCliente(dni, telefono):
    with open("clientes.txt", "r") as rModCliArchi:
        with open("clientesCopy.txt", "w") as wModCliArchi:
            linea = rModCliArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni == renglon[0]:
                    wModCliArchi.writelines(
                        renglon[0] + "," + renglon[1]+ "," + telefono + "," + renglon[3] + "," + renglon[4] + "," + renglon[5] +","+"\n")
                else:
                    wModCliArchi.write(linea)
                linea = rModCliArchi.readline()
            wModCliArchi.close()
        rModCliArchi.close()
    with open("clientesCopy.txt", "r") as fcopia:
        with open("clientes.txt", "w") as foriginal:
            for registro in fcopia:
                foriginal.write(registro)
            fcopia.close()
        foriginal.close()



#########################################################
def alta_cliente(dni, nombre, apellido, estado, isbn, telefono, direccion):
    with open("clientes.txt", "a") as jArchi:
        jArchi.write(str(dni) + "," + nombre + " " + apellido + "," + telefono + "," + direccion + "," + estado + "," + str(isbn) + "," "\n")
        jArchi.close()
################################################################       
def validarBorradoCliente(dni):
    global existeCliente
    existeCliente = False
    global clientePuedeTomarPrestamo
    clientePuedeTomarPrestamo=False
    global libroQueTeEstasAfanando

    with open("clientes.txt", "r") as rValBorCliArchi:
        with open("clientesCopy.txt", "w") as wValBorCliArchi:
            linea = rValBorCliArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if (str(dni) == str(renglon[0])):
                    existeCliente = True
                    if (renglon[4]).casefold() == "L".casefold():  ##Si el cliente no tiene libro en prestamo, o sea si esta "libre"
                        clientePuedeTomarPrestamo = True
                    else:
                        libroQueTeEstasAfanando = str(renglon[4])  # guardo en esta variable el isbn del libro que tiene
                else:
                    wValBorCliArchi.write(linea)
                linea = rValBorCliArchi.readline()
            wValBorCliArchi.close()
        rValBorCliArchi.close()


def borrar_cliente(dni):
    with open("clientes.txt", "r") as rArchi:
        with open("clientescpy.txt", "w") as wArchi:
            linea = rArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni != renglon[0]:
                    wArchi.write(linea)
                linea = rArchi.readline()
    with open('clientescpy.txt', 'r') as fcopia:
        with open('clientes.txt', 'w') as foriginal:
            linea=fcopia.readline()
            while linea !="":
                foriginal.write(linea)
                linea=fcopia.readline()

def validarBorradoLibro(isbn):
    global existeLibro
    existeLibro=False
    global libroEstaLibre
    libroEstaLibre=False
    global quienSeEstaHaciendoElOso
    with open("libros.txt", "r") as rValBorLibArchi:
        with open("libroscpy.txt", "w") as wValBorLibArchi:
            linea = rValBorLibArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if isbn == renglon[0]:
                    existeLibro=True
                    if (renglon[3]).casefold()=="L".casefold(): ##Si el libro esta libre
                        libroEstaLibre=True
                    else:
                        quienSeEstaHaciendoElOso= str(renglon[4]) #guardo en esta variable el dni del que tiene el libro

                else:
                    wValBorLibArchi.write(linea)
                linea = rValBorLibArchi.readline()
            wValBorLibArchi.close()
        rValBorLibArchi.close()

#####################################################################
def borrar_libro(isbn):
    with open("libros.txt", "r") as rArchi:
        with open("libroscpy.txt", "w") as wArchi:
            linea = rArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if isbn != renglon[0]:
                    wArchi.write(linea)
                linea = rArchi.readline()
    with open('libroscpy.txt', 'r') as fcopia:
        with open('libros.txt', 'w') as foriginal:
            linea=fcopia.readline()
            while linea !="":
                foriginal.write(linea)
                linea=fcopia.readline()

#########################registrar prestamo ##################################################################
def validar_prestamo(isbn, dni):
    global existeLibro
    global existeCliente
    global clientePuedeTomarPrestamo
    global libroEstaLibre


    existeLibro=False
    libroEstaLibre=False

    ################################PRIMERA APERTURA de los txt:  VALIDACION #######la 2da apertura de los txt en el metodo registrar_prestamo################################
    with open("libros.txt", "r") as rprestArchi:
        with open("librosCopy.txt", "w") as wprestArchi:
            linea=rprestArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(isbn) == renglon[0]:
                    existeLibro=True
                    if (renglon[3]).casefold()=="L".casefold(): ##Si el libro esta libre
                        libroEstaLibre=True
                else:
                    wprestArchi.write(linea)
                linea = rprestArchi.readline()
            wprestArchi.close()
        rprestArchi.close()

    existeCliente=False
    clientePuedeTomarPrestamo=False
    with open("clientes.txt", "r") as rclientArchi:
        with open("clientesCopy.txt", "w") as wclientArchi:
            linea=rclientArchi.readline()
            while linea != "":
                renglonCli = linea.split(',')
                if (str(dni)) == renglonCli[0]:
                    existeCliente = True
                    if (renglonCli[5])=="0":
                        clientePuedeTomarPrestamo=True
                else:
                    wclientArchi.write(linea)
                linea = rclientArchi.readline()
                wprestArchi.close()
                rprestArchi.close()
def registrarPrestamo(isbn, dni):
    global existeCliente
    global existeLibro
    global clientePuedeTomarPrestamo
    global libroEstaLibre
#####################################AHORA VUELVO A ABRIR LOS ARCHIVOS PARA MODIFICARLOS EN EL CASO DE QUE SE CUMPLA LA VALIDACION
    if(existeCliente==True and existeLibro==True and clientePuedeTomarPrestamo==True and libroEstaLibre==True):
        with open("libros.txt", "r") as rprestArchi:
            with open("librosCopy.txt", "w") as wprestArchi:
                linea = rprestArchi.readline()
                while linea != "":
                    renglon = linea.split(',')
                    if str(isbn) == renglon[0]:
                        wprestArchi.writelines(
                            renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + "O" + "," + str(dni)+","+"\n")
                    else:
                        wprestArchi.write(linea)
                    linea = rprestArchi.readline()
                wprestArchi.close()
            rprestArchi.close()
            with open("librosCopy.txt", "r") as fcopia:
                with open("libros.txt", "w") as foriginal:
                    for registro in fcopia:
                        foriginal.write(registro)
                    fcopia.close()
                foriginal.close()

##Ahora modifico clientes
        with open("clientes.txt", "r") as rclientArchi:
            with open("clientesCopy.txt", "w") as wclientArchi:
                linea = rclientArchi.readline()
                while linea != "":
                    renglon = linea.split(',')
                    if (str(dni)) == renglon[0]:
                        wclientArchi.writelines(
                            renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + renglon[3] + "," + "O" + "," + str(
                                isbn) + ","+"\n")
                    else:
                        wclientArchi.write(linea)
                    linea = rclientArchi.readline()
                wclientArchi.close()
            rclientArchi.close()
            with open("clientesCopy.txt", "r") as fClicopia:
                with open("clientes.txt", "w") as fClioriginal:
                    for registro in fClicopia:
                        fClioriginal.write(registro)
                    fClicopia.close()
                fClioriginal.close()

## validar devolucion
def validarDevolucion(isbn, dni):
    global existeLibro
    global existeCliente
    global clienteTieneESTELibro
    global libroEstaPrestadoAESTECliente
    global libroEstaLibre
    existeLibro = False
    existeCliente=False
    clienteTieneESTELibro=False
    libroEstaLibre=True
    libroEstaPrestadoAESTECliente=False


    ################################PRIMERA APERTURA de los txt:  VALIDACION #######la 2da apertura de los txt en el metodo registrar_devolucion################################
    with open("libros.txt", "r") as rDevLibArchi:
        with open("librosCopy.txt", "w") as wDevLibArchi:
            linea = rDevLibArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if str(isbn) == renglon[0]:
                    existeLibro = True
                    if (renglon[3]).casefold() == "O".casefold():  ##Si el libro esta ocupado
                        libroEstaLibre = False
                        if(renglon[4])==dni:
                            libroEstaPrestadoAESTECliente=True
                else:
                    wDevLibArchi.write(linea)
                linea = rDevLibArchi.readline()
            wDevLibArchi.close()
        rDevLibArchi.close()

    existeCliente = False
    clienteTieneESTELibro = False
    with open("clientes.txt", "r") as rDevClientArchi:
        with open("clientesCopy.txt", "w") as wDevClientArchi:
            linea = rDevClientArchi.readline()
            while linea != "":
                renglonCli = linea.split(',')
                if (str(dni)) == renglonCli[0]:
                    existeCliente = True
                    if ((str(renglonCli[5]) )==isbn):
                        clienteTieneESTELibro = True
                else:
                    wDevClientArchi.write(linea)
                linea = rDevClientArchi.readline()
            wDevClientArchi.close()
        rDevClientArchi.close()

def registrarDevolucion(isbn, dni):

###################corregir esta funcion, esta copiada de registrar prestamo. OJO con las variables!!

    global existeCliente
    global existeLibro
    global libroEstaPrestadoAESTECliente
    global libroEstaLibre
    global clienteTieneESTELibro
    #####################################AHORA VUELVO A ABRIR LOS ARCHIVOS PARA MODIFICARLOS EN EL CASO DE QUE SE CUMPLA LA VALIDACION
    if (existeCliente == True and existeLibro == True and clienteTieneESTELibro == True and libroEstaLibre == False and libroEstaPrestadoAESTECliente==True):
        with open("libros.txt", "r") as rDevArchi:
            with open("librosCopy.txt", "w") as wDevArchi:
                linea = rDevArchi.readline()
                while linea != "":
                    renglon = linea.split(',')
                    if str(isbn) == renglon[0]:
                        wDevArchi.writelines(
                            renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + "L" + "," + "0"+ "," + "\n")
                    else:
                        wDevArchi.write(linea)
                    linea = rDevArchi.readline()
                wDevArchi.close()
            rDevArchi.close()
            with open("librosCopy.txt", "r") as fDevLibcopia:
                with open("libros.txt", "w") as fDevLiboriginal:
                    for registro in fDevLibcopia:
                        fDevLiboriginal.write(registro)
                    fDevLibcopia.close()
                fDevLiboriginal.close()

        ##Ahora modifico clientes
        with open("clientes.txt", "r") as rDevCliArchi:
            with open("clientesCopy.txt", "w") as wDevCliArchi:
                linea = rDevCliArchi.readline()
                while linea != "":
                    renglon = linea.split(',')
                    if (str(dni)) == renglon[0]:
                        wDevCliArchi.writelines(
                            renglon[0] + "," + renglon[1] + "," + renglon[2] + "," + renglon[
                                3] + "," + "L" + "," + str("0") + "," + "\n")
                    else:
                        wDevCliArchi.write(linea)
                    linea = rDevCliArchi.readline()
                wDevCliArchi.close()
            rDevCliArchi.close()
            with open("clientesCopy.txt", "r") as fDevClicopia:
                with open("clientes.txt", "w") as fDevClioriginal:
                    for registro in fDevClicopia:
                        fDevClioriginal.write(registro)
                    fDevClicopia.close()
                fDevClioriginal.close()
#########################corregir para arriba toda la funcion registrar devolucion##################3
#consultar cliente
def consultaCliente(dni):
    global existeCliente
    existeCliente=False
    validarExisteCliente(dni)
    if existeCliente==False:
        print("No existe un cliente con ese DNI. Por favor, revise los datos. ")

    if existeCliente==True:

        with open("clientes.txt", "r") as jCliArchi:
            linea = jCliArchi.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni == renglon[0]:
                    jCliArchi.close()
                    return renglon
                linea = jCliArchi.readline()
            jCliArchi.close()
    seguirONo()

# consulta libro
def consulta_libro(isbn):
    with open("libros.txt", "r") as jArchi:
        linea = jArchi.readline()
        while linea != "":
            renglon = linea.split(',')
            if isbn == renglon[0]:
                jArchi.close()
                return renglon
            linea = jArchi.readline()
        jArchi.close()




listaNumeros=["0","1","2","3","4","5","6","7","8","9"]
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
    opcion=sacarTodosLosEspacios(opcion)
    print(f"Su Opcion fue {opcion}")
    if opcion=='1':
        opcionPrestamo = input('''
Préstamo de Libro:
    1 - Consultar todos los títulos
    2 - Registrar Préstamo
    3 - Registrar Devolución
    0 - Volver al Menu Anterior
    **********************************
Elija la opción deseada: ''')
        opcionPrestamo=sacarTodosLosEspacios(opcionPrestamo)
        if opcionPrestamo == "1":
            with open("libros.txt", "r") as kArchi:
                print("***************** LIBROS ***************")
                print(
                    "{5}{0:^8}{5} {5}{1:^22}{5} {5}{2:^20}{5} {5}{3:^15}{5} {5}{4:^11}{5}".format
                    ("ISBN", "Titulo", "Autor", "Estado", "DNI",
                    "|"))
                linea = kArchi.readline()
                while linea != "":
                    renglon = linea.split(',')
                    print(
                        "{5}{0:>8}{5} {5}{1:22s}{5} {5}{2:20s}{5} {5}{3:>15}{5} {5}{4:>11}{5}".format(renglon[0],
                                                                                                    renglon[1],
                                                                                                    renglon[2],
                                                                                                    renglon[3],
                                                                                                    renglon[4], "|"))
                    linea = kArchi.readline()
                print("------------------------------------------------------------")
                kArchi.close()
    ##seguir o salir
                print("Quiere seguir?")
                validador=seguirONo()

        elif opcionPrestamo == "2":
            existeCliente = False
            existeLibro = False
            libroEstaLibre = False
            clientePuedeTomarPrestamo = False
            print("Se registrará un préstamo con los datos que le pediremos:")
            isbn=pedirIsbn()
            dni=pedirDni()


            validar_prestamo(isbn, dni)

    ##condiciones para que se pueda registrar: que exista el cliente y que no tenga libros prestados, y que exista el libro  y no este tomado por otro cliente#

            if(existeLibro==False):
                print("El ISBN ingresado no coincide con ninguno existente en nuestra biblioteca. ")
            if(existeCliente==False):
                print("El DNI ingresado no coincide con ninguno de nuestros socios.")
            if(existeLibro==True and existeCliente==True and libroEstaLibre==False):
                print("Ese libro no esta disponible. Lo tiene en préstamo el cliente con el DNI", dni)
            if(existeLibro==True and existeCliente==True and clientePuedeTomarPrestamo==False):
                print("Este cliente ya tiene un libro en prestamo, devuelva el Libro con el ISBN",isbn , "para poder tomar otro.")
            if (existeCliente==True and existeLibro==True and libroEstaLibre==True and clientePuedeTomarPrestamo==True):
                registrarPrestamo(isbn,dni)
                print("Se le ha prestado  el libro  de ISBN  " + isbn +  " al socio de DNI " + dni)

    ## seguir o salir
            print("Quiere seguir?: ")
            validador = seguirONo()
    ##

        elif opcionPrestamo == "3":
        # global existeCliente ya esta declarada
            existeCliente=False
            #global existeLibro
            existeLibro=False
            # global libroEstaLibre ya esta declarada
            libroEstaLibre=True
            global libroEstaPrestadoAESTECliente
            libroEstaPrestadoAESTECliente=False
            global clienteTieneESTELibro
            clienteTieneESTELibro=False
            print("Se registrará una devolución. Necesitamos los siguientes datos:")
            isbn=pedirIsbn()
            dni=pedirDni()
            #isbn = input("Ingrese el ISBN del libro: ")
            #dni = input("Ingrese el Dni del socio: ")

            validarDevolucion(isbn,dni)
            if (existeLibro == False):
                print("El ISBN ingresado no coincide con ninguno existente en nuestra biblioteca. ")
            if (existeCliente == False):
                print("El DNI ingresado no coincide con ninguno de nuestros socios.")
            if (existeLibro == True and existeCliente == True and libroEstaLibre == True):
                print("Ese libro no esta prestado. Para prestarlo, utilice la función correspondiente en el menú. ")
            if(existeLibro==True and existeCliente==True and libroEstaLibre==False and (libroEstaPrestadoAESTECliente==False or clienteTieneESTELibro==False)):
                print("El libro de ISBN " +isbn+ " esta prestado, pero no al socio de DNI " +dni+". No se puede efectuar la devolucion, por favor chequee los datos.")

            if(existeLibro==True and existeCliente==True and libroEstaLibre==False and libroEstaPrestadoAESTECliente==True and clienteTieneESTELibro==True):
                registrarDevolucion(isbn,dni)
                print("El socio con DNI " +dni+ " ha devuelto el libro de ISBN " +isbn + ". Gracias por elegir la lectura! Nos da trabajo a todos nosotros y nos sentimos parte de la cultura general")
    ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()
        elif opcionPrestamo == "0":
            validador= True
        else:
            print("No se ha elegido una opción válida")
            ## seguir o salir
            print("Quiere seguir?")
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

        opcionGestionCli=sacarTodosLosEspacios(opcionGestionCli)
        if opcionGestionCli=='1':
            print("Se agregará un nuevo cliente")
            dni=pedirDni()
            #dni = input("Ingrese el DNI: ")
            nombre=pedirNombre()
            apellido=pedirApellido()
            telefono=pedirTelefono()
            direccion=pedirDireccion()
            isbn = str('0')
            estado="L"
            validarExisteCliente(dni)
            if existeCliente== False:
                alta_cliente(dni, nombre, apellido, estado, isbn, telefono, direccion)
                print("----Se agregó nuevo Cliente: ", nombre.upper(), apellido.upper(),'----')
                print("Quiere seguir?")
                validador = seguirONo()
            else:
                print("Ya existe un cliente con ese DNI en nuestra biblioteca. Por favor, revise los datos.")
                print("Quiere seguir?")
                validador = seguirONo()
                
    ##

        elif opcionGestionCli=='2':
            #global existeCliente
            existeCliente=False
            print("Consulta de Estado de cliente")
            dni = pedirDni()
            validarExisteCliente(dni)
            if existeCliente==False:
                print("Ese DNI no coincide con el de ninguno de nuestros clientes. Por favor, revise los datos. ")
            if existeCliente==True:
                enLinea = consultaCliente(dni)
                nombreYApellido = str( enLinea[1])
                telefono = str (enLinea[2])
                direccion=str (enLinea[3])
                if (str(enLinea[4])=="L"):
                    estado="Puede tomar un libro en prestamo" #puede tomar prestamos
                if (str(enLinea[4]) == "O"):
                    estado = "Ya tiene un libro en prestamo"
                    queLibroTiene = str(enLinea[5])

                #print("El cliente de dni " +dni + " se llama "+nombreYApellido +". Su direccion es " +direccion+". Su telefono es "+telefono+ ". Y ademas "+estado)
                print(f" --- DATOS DE CLIENTE CONSULTADO ---\n"
                      f"DNI NUMERO: {dni}\n"
                      f"NOMBRE Y APELLIDO: {nombreYApellido}\n"
                      f"DIRECCION: {direccion}\n"
                      f"TELEFONO: {telefono}\n"
                      f"ESTADO: {estado}")
                if estado=="Ya posee un libro en prestamo":
                    print("El del ISBN" +queLibroTiene)

    ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()
    ##

        elif opcionGestionCli=='3':
            existeCliente=False
            print("Se modificara el Socio cuyos datos se solicitaran a continuacion:")
            dni=pedirDni()
            validarExisteCliente(dni)
            if existeCliente==False:
                print("No existe en nuestro registro un socio con ese DNI. Revise los datos.")
            if existeCliente==True:
                Modifcliente = input('Si quiere modificar la Direccion del socio presione 1; Si quiere modificar el Telefono presione 2: ')
                if Modifcliente == '1':
                    direccion=input("Ingrese el nuevo Domicilio del Cliente: ")
                    modificarDirecCliente(dni, direccion)
                    print("Ahora el cliente del DNI "+dni+" su direccion es " +direccion)
                    

                elif Modifcliente =='2':
                    telefono=input("Ingrese el nuevo Telefono del Cliente: ")
                    modificarTelCliente(dni, telefono)
                    print("Ahora el cliente del DNI "+dni+"; tiene el Tel "+telefono)
                else:
                    print("No se ha elegido una opción válida")
                    ## seguir o salir
                    print("Quiere seguir?")
                    validador = seguirONo()
            print("Quiere seguir?")
            validador = seguirONo()

        elif opcionGestionCli=='4':
            print('Se eliminara el socio')
            dni= pedirDni()
            validarBorradoCliente(dni)
            if existeCliente==False:
                print("Ese DNI no corresponde a ninguno de nuestros socios, por lo tanto, no se borrara ningun socio.")
                seguirONo()
            if(existeCliente==True and clientePuedeTomarPrestamo==False):
                print("El cliente de DNI " + dni+" tiene en prestamo el libro de ISBN "+libroQueTeEstasAfanando+ "realice la devolucion para poder ser dado de baja" )
                seguirONo()
            if(existeCliente==True and clientePuedeTomarPrestamo==True):
                decision=input('***ATENCION ESTA POR ELIMINAR DEFINITIVAMENTE EL CLIENTE***\n Si desea continuar presione S o si desea volver al menu presione N: ')
                decision=decision.upper()
                if decision=='S':
                    borrar_cliente(dni)
                    print('----Se ha eliminado el cliente con el DNI: ', dni, '----')
                elif decision =='N':
                    print('Ha seleccionado que NO. Vuelve al Menu Principal\n')
                    seguirONo()
                else:
                    print("La opcion ingresada no es correcta")
    ## seguir o salir
                    print("Quiere seguir?")
                    validador = seguirONo()

        elif opcionGestionCli=='0':
            validador=True
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


        if opcionGestionLib == "1":
            print("Se agregará un nuevo Libro.")
            isbn = pedirIsbn()
            titulo = pedirTitulo()
            autor = pedirAutor()
            #estado = input("Ingrese el Estado 'L' para Libre o 'O' para ocupado: ")
            estado = "L"
            # estado.upper()
            # if estado =='L':
            dni = str('0')
            validarExisteLibro(isbn)
            if existeLibro ==False:

                alta_libro(isbn, titulo, autor, estado, dni)
                print("----Se agregó el Libro ", titulo.upper(), '----')
                print("Quiere seguir?")
                validador = seguirONo()
            else:
                print("Ya existe un libro con ese ISBN. Por favor, revise los datos.")
                print("Quiere seguir?")
                validador = seguirONo()
        elif opcionGestionLib == "2":
            #global existeLibro
            existeLibro=False
            print("Que libro quiere consultar?")
            isbn = pedirIsbn()
            validarExisteLibro(isbn)
            if existeLibro==False:
                print("El libro con el ISBN ingresado no corresponde a un item de esta biblioteca. Por favor chequee los datos.")
            if existeLibro==True:

                enLinea=consulta_libro(isbn)
                titulo=enLinea[1]
                autor=enLinea[2]
                if ((str (enLinea[3]))=="L"):
                    estado="disponible"

                if((str(enLinea[3]))=="O"):
                    estado="prestado"
                    quienLoTiene = str(enLinea[4])

                print("El titulo del libro es: \'"+titulo+"\'. Su autor es "+ autor+" y su ISBN es " +isbn)
                if estado=="prestado":
                    print("En este momento esta prestado al socio de DNI " + quienLoTiene)
                if estado=="disponible":
                    print("En este momento esta disponible. Puede sacarlo en prestamo eligiendo la opcion correspondiente en el menu principal. ")

            #print("El libro es: ", consulta_libro(isbn))
    ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()
    ##

        elif opcionGestionLib == "3":
            #global existeLibro
            existeLibro=False
            print("Se modificara el libro cuyos datos se solicitaran a continuacion:")
            isbn=pedirIsbn()
            validarExisteLibro(isbn)
            if existeLibro==False:
                print("No existe en nuestra biblioteca un libro con ese ISBN. Revise los datos.")
            if existeLibro==True:
                titulo=pedirTitulo()
                autor=pedirAutor()
                modificarLibro(isbn, titulo, autor)
                print("Ahora el libro del ISBN "+isbn+"; se llama "+titulo+"; y su autor es " +autor)
    ## seguir o salir
            print("Quiere seguir?")
            validador = seguirONo()
    ##

        elif opcionGestionLib == "4":
            print('Se eliminara el Libro')
            isbn= pedirIsbn()
            validarBorradoLibro(isbn)
            if(existeLibro==False):
                print("Ese libro no existe en nuestra biblioteca, por lo tanto, no se puede borrar.")
                seguirONo()
            if(existeLibro==True and libroEstaLibre==False):
                print("El libro de ISBN "+isbn + " esta prestado al socio de  " + str(quienSeEstaHaciendoElOso)+ "realice la devolucion para poder dar de baja el Libro.")
                seguirONo()
            if(existeLibro==True and libroEstaLibre==True):
                decision=input('***ATENCION ESTA POR ELIMINAR DEFINITIVAMENTE AL LIBRO***\n Si desea continuar presione S o si desea volver al menu presione N: ')
                decision=decision.upper()
                if decision=='S':
                    borrar_libro(isbn)
                    print('----Se ha eliminado el Libro con el ISBN: ', isbn,'----')
                    seguirONo()
                elif decision =='N':
                    print('----Ha seleccionado que NO. No se ha eliminado el libro----\n')
                    seguirONo()
                else:
                    print("La opcion ingresada no es valida")
                    seguirONo()
        elif opcionGestionLib == "0":
            validador=True

    elif opcion=="4":
        print("Gracias por elegir nuestro programa.")
        validador=False
    elif opcion=="0":
        print("Que libro quiere consultar?")
        isbn = pedirIsbn()
        print(consulta_estado(isbn))
        print("Quiere seguir?")
        validador = seguirONo()

    else:
        print("No se ha elegido una opción válida")
        ## seguir o salir
        print("Quiere seguir?")
        validador = seguirONo()

