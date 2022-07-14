#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from operator import truediv
from pydoc import cli
import sys
import re
from tkinter import Menu
import mariadb
import os
import Clientes
import Proveedores
import Pedidos
import Ventas
import Articulos
import datetime

dbMayorista = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '25109',
    database = 'Mayorista_Willy',
    autocommit= True

)
mycursor = dbMayorista.cursor()

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

listaNumeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


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


def pedirMail():
    validadorMail=False
    while validadorMail ==False:
        mail= input('- MAIL:')
        if (re.search(regex, mail)):
            validadorMail =True

        else:
            print('****MAIL MAL INGRESADO****')
    return mail

def buscarUltimoPedido():
    sqlBuscarUltimoPedido="select MAX(id_pedido) from pedidos"
    mycursor.execute(sqlBuscarUltimoPedido)
    resultadoBuscarUltimoPedido=mycursor.fetchone()
    if len(resultadoBuscarUltimoPedido) < 1:
        ultimoPedido = 0
        
    else:
        ultimoPedido= resultadoBuscarUltimoPedido[0]
        
    return ultimoPedido




def listarProveedores():
    sql= 'Select * From proveedores'
    mycursor.execute(sql)
    Resultado= mycursor.fetchall()
    if len(Resultado) > 0:
        for reg in Resultado:
           print(f'''[{reg[0]}] - {reg[1]}\n''')
        pedirIdProveedorLista=pedirIdProveedor()
        
    return pedirIdProveedorLista

def validarSoloLetras(entrada):
    global listaNumeros
    noHayNumeros = True
    for i in entrada:
        if i in listaNumeros:
            noHayNumeros = False
            print("Numero Encontrado " + i)
            return noHayNumeros

    return noHayNumeros


def pedirNombre():
    global nombre
    validadorNombre = False
    while validadorNombre == False:
        nombre = input("- NOMBRE Y APELLIDO: ")
        if(contarLosCaracteres(nombre) > 1 and contarLosCaracteres(nombre) < 30):
            validadorNombre = validarSoloLetras(nombre)
        if validadorNombre == False:
            print(
                "****NOMBRE MAL INGRESADO**** \n- Debe tener  mas de 2 caracteres y  no contener numéricos -")
    return nombre


def pedirTelefono():
    global telefono
    validadorTelefono = False
    while validadorTelefono == False:
        telefono = input("- TELEFONO: ")
        if (contarLosCaracteres(telefono) > 6):
            validadorTelefono = validarNumerico(telefono)
        if validadorTelefono == False:
            print(
                "****TELEFONO MAL INGRESADO**** \n- Debe tener  mas de 6 caracteres, solamente numéricos -")
    return telefono

def pedirPrecio():
    global precio
    validadorPrecio = False
    while validadorPrecio == False:
        precio = input("- PRECIO: $")
        if (contarLosCaracteres(precio) > 0):
            validadorPrecio = validarNumerico(precio)
            precio=float(precio)
        if validadorPrecio == False:
            print(
                "****PRECIO MAL INGRESADO**** \n- Debe ser mayor a $0, solamente numéricos -")
    return precio

def pedirStock():
    global stock
    validadorStock = False
    while validadorStock == False:
        stock = input("- STOCK: ")
        if (contarLosCaracteres(stock) > 0):
            validadorStock = validarNumerico(stock)
        if validadorStock == False:
            print(
                "****STOCK MAL INGRESADO**** \n- Debe ser mayor a 0, solamente numéricos -")
    return stock

def buscarSinStock ():
    sqlBusquedaArticulo= 'Select * from Articulos where stock = 0'
    mycursor.execute(sqlBusquedaArticulo)
    resultadoBusquedaArticulo=mycursor.fetchall()
    if len(resultadoBusquedaArticulo)> 0:
        return resultadoBusquedaArticulo
    else:
        print('****ARTICULO NO COINCIDE CON CONDICIONES DE BUSQUEDA ****')
        return resultadoBusquedaArticulo
        seguirONo()

def buscarVentasDelDia ():
    hoy=datetime.date.today()
    sqlBusquedaVentasDelDia= 'Select * from ventas where fecha =\"'+str(hoy)+'\"'
    mycursor.execute(sqlBusquedaVentasDelDia)
    resultadoBusquedaVentasDelDia=mycursor.fetchall()
    if len(resultadoBusquedaVentasDelDia)> 0:
        return resultadoBusquedaVentasDelDia
    else:
        print('****NO HAY VENTAS DEL DIA****')
        return resultadoBusquedaVentasDelDia
        
        

""" def pedirRubro():
    global rubro
    validadorRubro= False
    while validadorRubro== False:
        print('- SELECCIONE RUBRO:')
        rubro = listarRubros()
        for i in range(0, len(rubro)):
            print(f'[{i+1}] {rubro[i]}')
            opcionElegidaRubro = input('')
             """
""" def pedirRubro():
    global rubro
    validadorRubro = False
    while validadorRubro == False:
        rubro = listarRubros()
        if (contarLosCaracteres(rubro) == 1):
            
            validadorRubro = validarNumerico(opcionElegidaRubro)
        if validadorRubro == False:
            print(
                "****RUBRO MAL INGRESADO**** \n- Solamente numéricos -")
    return rubro """
        

def pedirDireccion():
    global direccion
    validadorDireccion = False
    while validadorDireccion == False:
        direccion = input("- DIRECCION: ")
        if(contarLosCaracteres(direccion) > 5 and contarLosCaracteres(direccion) < 100):
            validadorDireccion = True
        if validadorDireccion == False:
            print("****DIRECCION MAL INGRESADA**** \n- Debe tener  mas de 5 caracteres -")
    return direccion

def pedirDni():
    global dni
    validadorDni = False
    while validadorDni == False:
        dni = input("- DNI: ")
        if (contarLosCaracteres(dni) == 8):
            validadorDni = validarNumerico(dni)
        if validadorDni == False:
            print(
                "****DNI MAL INGRESADO**** \n- Debe tener 8 caracteres, solamente numéricos -")
    return dni

def pedirIdProveedor():
    global idProveedor
    validadoridProveedor = False
    while validadoridProveedor == False:
        idProveedor = input(": ")
        if (contarLosCaracteres(idProveedor) > 0):
            validadoridProveedor = validarNumerico(idProveedor)
        if validadoridProveedor == False:
            print(
                "****OPCION MAL INGRESADA**** \n- caracteres, solamente numéricos -")
    return idProveedor

def existeCliente(dni):
    sqlbusqueda = 'SELECT * FROM clientes WHERE DNI = ' + str(dni)
    mycursor.execute(sqlbusqueda)        
    Resultado = mycursor.fetchall()
    if len(Resultado) > 0:
        existe = True
    else:
        existe =False

    return existe

def existeProveedor(cuit):
    sqlbusqueda = 'SELECT * FROM proveedores WHERE CUIT = ' + str(cuit)
    mycursor.execute(sqlbusqueda)        
    Resultado = mycursor.fetchall()
    if len(Resultado) > 0:
        existe = True
    else:
        existe =False

    return existe

def existeArticulo(codigo):
    sqlbusqueda = 'SELECT * FROM Articulos WHERE CODIGOBARRAS = ' + str(codigo)
    mycursor.execute(sqlbusqueda)        
    Resultado = mycursor.fetchall()
    if len(Resultado) > 0:
        existe = True
    else:
        existe =False

    return existe
    

def pedirCuit():
    global cuit
    validadorCuit = False
    while validadorCuit == False:
        cuit = input("- CUIT: ")
        if (contarLosCaracteres(cuit) == 11):
            validadorCuit = validarNumerico(cuit)
        if validadorCuit == False:
            print(
                "****CUIT MAL INGRESADO**** \n- Debe tener 11 caracteres, solamente numéricos -")
    return cuit

def pedirCodigo():
    global codigo
    validadorCodigo = False
    while validadorCodigo == False:
        codigo = input("- CODIGO DE BARRAS: ")
        if (contarLosCaracteres(codigo) > 6):
            validadorCodigo = validarNumerico(codigo)
        if validadorCodigo == False:
            print(
                "****CODIGO DE BARRAS MAL INGRESADO**** \n- Debe tener 6 o mas caracteres, solamente numéricos -")
    return codigo

def seguirONo():
    variable = input(
        "[1] - VOLVER AL MENU PRINCIPAL\n[2] - SALIR DEL PROGRAMA\n: ")
    if variable == "1":
        return True
        
    elif variable == "2":
        exit()
        
    else:
        print('**** COLOQUE UNA OPCION VALIDA****')
        seguirONo() 

def buscarDni(valor):
    sqlBusquedaDni= 'Select * from clientes where DNI =' +str(valor)
    mycursor.execute(sqlBusquedaDni)
    resultadoBusquedaDni=mycursor.fetchall()
    if len(resultadoBusquedaDni)> 0:
        for reg in resultadoBusquedaDni:
            clienteEncontrado=Clientes.Cliente(reg[1],reg[2],reg[3],reg[4],reg[5], reg[6])
        return clienteEncontrado
    else:
        print('****CLIENTE NO EXISTE****')
        seguirONo()



def buscarCuit(valor):
    sqlBusquedaCuit= 'Select * from proveedores where CUIT =' +str(valor)
    mycursor.execute(sqlBusquedaCuit)
    resultadoBusquedaCuit=mycursor.fetchall()
    if len(resultadoBusquedaCuit)> 0:
        for reg in resultadoBusquedaCuit:
            proveedorEncontrado=Proveedores.Proveedores(reg[1],reg[2],reg[3],reg[4],reg[5], reg[6], reg[7])
        return proveedorEncontrado

    else:
        print('****PROVEEDOR NO EXISTE****')
        seguirONo()


def buscarCodigo(valor):
    sqlBusquedaCodigo= 'Select * from articulos where CodigoBarras =' +str(valor)
    mycursor.execute(sqlBusquedaCodigo)
    resultadoBusquedaCodigo=mycursor.fetchall()
    if len(resultadoBusquedaCodigo)> 0:
        for reg in resultadoBusquedaCodigo:
            codigoEncontrado=Articulos.Articulo(reg[1],reg[2],reg[3],reg[4],reg[5])
        return codigoEncontrado
    else:
        print('****ARTICULO NO EXISTE****')
        seguirONo()
        
        
def IdporString(valor):
    sql='Select * From situacion_iva Where ID_Iva=' +str(valor)
    mycursor.execute(sql)
    resultadoIdPorString=mycursor.fetchall()
    if len(resultadoIdPorString)> 0:
        for reg in resultadoIdPorString:
            idporStringEncontrado=reg[1]
        return idporStringEncontrado

def IdporStringRubro(valor):
    sql='Select * From rubros Where id_Articulo=' +str(valor)
    mycursor.execute(sql)
    resultadoIdPorString=mycursor.fetchall()
    if len(resultadoIdPorString)> 0:
        for reg in resultadoIdPorString:
            idporStringEncontrado=reg[1]
        return idporStringEncontrado


def listarSituacionIva():
    sql= 'Select * From situacion_Iva'
    mycursor.execute(sql)
    Resultado= mycursor.fetchall()
    listaSituacionIva=[]
    if len(Resultado) > 0:
        for reg in Resultado:
            listaSituacionIva.append(reg[1])
    return listaSituacionIva

def listarRubros():
    sql= 'Select * From rubros'
    mycursor.execute(sql)
    Resultado= mycursor.fetchall()
    listaRubros=[]
    if len(Resultado) > 0:
        for reg in Resultado:
            listaRubros.append(reg[1])
    return listaRubros






def muestroMenu():
    clearConsole()
    print("\n\n\n\n****************** MAYORISTA WILLY *******************")
    print('''\n
    [1] - Proveedores:
        -   Alta / Baja / Modif
        -   Pedido de reposición--------------FF
        -   Devolución a proveedor--------------FF

    [2] - Cliente:
        -   Alta
        -   Baja
        -   Modificacion
        -   Mostrar Datos

    [3] - Articulos:
        -   Alta / Baja / Modif
        -   Ingreso de Remito--------------FF
        -   Listado de Artículos sin Stock

    [4] - Ventas:
        -   Facturación--------------FF
        -   Listado de ventas del día


    
    [0] - SALIR ->

****************************************************
    ''')


validador = True
while validador == True:
    muestroMenu()
    opcion = input("Elija la opción deseada:")
    clearConsole()
    print(f"\nSu Opcion fue {opcion}")
    

############MENU PROVEEDORES################

    if opcion == '1':
            print("***************** PROVEEDORES *****************")
            print('''\n
        [1] -  Alta / Baja / Modif
        [2] -  Pedido de reposición
        [3] -  Devolución a proveedor


        [0]   VOLVER AL MENU PRINCIPAL ->
            ''')
            print("***********************************************")
            opcionProveedores = input('Elija la opción deseada:')
            clearConsole()
            print(f"\nSu Opcion fue {opcionProveedores}")

            ############SUBMENU PROVEEDORES ALTA BAJA MODIF ################
            if opcionProveedores == '1':
                print("***************** PROVEEDORES  *****************")
                print("*************** ALTA/BAJA/MODIF  ***************")
                
                print('''\n
            [1] -  Alta de Proveedor
            [2] -  Baja de Proveedor
            [3] -  Modificacion de Proveedor


            [0]   VOLVER AL MENU PRINCIPAL ->
                ''')
                print("***********************************************")
                opcionProveedoresAltaBajaModif = input('Elija la opción deseada:')
                clearConsole()
                print(f"\nSu Opcion fue {opcionProveedoresAltaBajaModif}")


                ############ALTA DE PROVEEDOR################
                if opcionProveedoresAltaBajaModif =='1':
                    print("***************** PROVEEDORES *****************")
                    print("************** ALTA DE PROVEEDOR **************")
                    cuit=pedirCuit()
                    if not existeProveedor(cuit):
                        nombreEmpresa=input('- NOMBRE DE EMPRESA:')
                        titular=pedirNombre()
                        direccion=pedirDireccion()
                        mail=pedirMail()
                        telefono=pedirTelefono()
                        print('- SELECCION SITUACION ANTE IVA:')
                        situacionIva=listarSituacionIva()
                        for i in range(1,len(situacionIva)): #proveedores range 1 no CONSUMIDOR FINAL
                            print(f'[{i+1}] {situacionIva[i]}')
                        opcionElegidaIva=input('')
                        if opcionElegidaIva =='2' or opcionElegidaIva =='3' or opcionElegidaIva =='4':
                            proveedorNuevo=Proveedores.Proveedores(cuit, nombreEmpresa, titular, direccion, mail, telefono, opcionElegidaIva)
                            proveedorNuevo.altaProveedor()
                            print('*** PROVEEDOR CREADO EXITOSAMENTE ***')
                            seguirONo()
                        else:
                            print("****NO SE HA ELEGIDO UNA OPCION VALIDA****")
                            print("DESEA CONTINUAR?")
                            seguirONo()
                    
                    else:
                        print('****PROVEEDOR YA EXISTE****')
                        seguirONo()
                    

                 ############BAJA DE PROVEEDOR################
                elif opcionProveedoresAltaBajaModif =='2':
                    print("***************** PROVEEDORES *****************")
                    print("************** BAJA DE PROVEEDOR **************")
                    cuit=pedirCuit()
                    buscarCuitBaja=buscarCuit(cuit)
                    buscarCuitBaja.borrarProveedor(cuit)
                    print('****PROVEEDOR ELIMINADO****')
                    seguirONo()
                
                ############MODIFICACION DE PROVEEDOR################
                elif opcionProveedoresAltaBajaModif =='3':
                    print("***************** PROVEEDORES *****************")
                    print("******** MODIFICACION DE PROVEEDOR **********")
                    cuit=pedirCuit()
                    buscarCuitModificar= buscarCuit(cuit)
                    cuitAModificar=buscarCuitModificar.mostrarProveedor()
                    print(f'-----DATOS ACTUALES DE PROVEEDOR-----')
                    print(f'- CUIT:{cuitAModificar[0]}\n')
                    print(f'- NOMBRE EMPRESA:{cuitAModificar[1]}\n')
                    print(f'- NOMBRE TITULAR:{cuitAModificar[2]}\n')
                    print(f'- DIRECCION:{cuitAModificar[3]}\n')
                    print(f'- MAIL:{cuitAModificar[4]}\n')
                    print(f'- TELEFONO:{cuitAModificar[5]}\n')
                    print(f'- SITUACION ANTE IVA:{IdporString(cuitAModificar[6])}\n')
                    ###modifico
                    print(f'****INGRESE LOS DATOS A MODIFICAR****')
                    cuit=pedirCuit()
                    nombreEmpresa=input('- NOMBRE EMPRESA:')
                    nombreApellido=pedirNombre()
                    direccion=pedirDireccion()
                    telefono=pedirTelefono()
                    mail=pedirMail()
                    situacionIva=listarSituacionIva()
                    for i in range(1,len(situacionIva)): #proveedores range 1
                        print(f'[{i+1}] {situacionIva[i]}')
                    opcionElegidaIva=input('')
                    if opcionElegidaIva =='2' or opcionElegidaIva =='3' or opcionElegidaIva =='4':
                       ProveedorModificado=Proveedores.Proveedores(cuit, nombreEmpresa,nombreApellido, direccion, mail, telefono, opcionElegidaIva)
                       ProveedorModificado.editarProveedor(cuitAModificar[0])
                       print('****PROVEEDOR MODIFICADO****')
                       seguirONo()
                    else:
                        print("****NO SE HA ELEGIDO UNA OPCION VALIDA****")
                        print("DESEA CONTINUAR?")
                        seguirONo()


            
            ############SUBMENU PROVEEDORES PEDIDO DE REPOSICION ################
            elif opcionProveedores == '2':
                print("***************** PROVEEDORES  *****************")
                print("************ PEDIDO DE REPOSICION  ************")
                seguir=True
                ultimoPedidoEncontrado=buscarUltimoPedido()
                numeroSolicitud= ultimoPedidoEncontrado + 1
                fechaHoy= datetime.date.today()
                proveedorElegido=listarProveedores()
                while seguir:
                    articuloElegido=int(input('INGRESE ID ARTICULO: '))
                    cantidadArticulo=int(input('CANTIDAD: '))
                    estado='SOLICITADO'
                    comentario=input('COMENTARIO: ')
                    confirmacionArticulo=int(input(f'''CONFIRMA AGREGAR ARTICULO AL PEDIDO : 
                                - [1] SI
                                - [2] NO'''))
                    if confirmacionArticulo==1:
                        solicitud= Pedidos.Pedido(numeroSolicitud,fechaHoy, proveedorElegido,articuloElegido,cantidadArticulo, estado, 0,0,comentario)
                        solicitud.altaPedido()
                        dbMayorista.commit()
                        print('**** ARTICULO CARGADO ****')
                        agregarArticulo=int(input(f'''DESEA AGREGAR OTRO ARTICULO AL PEDIDO ? : 
                                - [1] SI
                                - [2] NO'''))
                        if agregarArticulo !=1:
                            seguir=False
                            print('****PEDIDO COMPLETADO****')
                    elif confirmacionArticulo==2:
                            print('**** PEDIDO ANULADO ****')
                            seguirONo()
                    else:
                        print('**** OPCION INVALIDA ****')
                        seguirONo()
                else:
                    
                    seguirONo()
                    
            ############SUBMENU PROVEEDORES DEVOLUCION A PROVEEDOR ################
            elif opcionProveedores == '3': 
                print("***************** PROVEEDORES  *****************")
                print("*********** DEVOLUCION A PROVEEDOR  ***********")
                    
                print('''\n
            [1] -  Devolucion por ID de Articulo
            [2] -  Devolucion por Codigo de Barra de Articulo
            [3] -  Devolucion por Nombre de Articulo


            [0]   VOLVER AL MENU PRINCIPAL ->
                ''')
                print("***********************************************")
                opcionProveedoresDevolucionAProveedor = input('Elija la opción deseada:')
                print(f"\nSu Opcion fue {opcionProveedoresDevolucionAProveedor}")


            ############SUBMENU PROVEEDORES VOLVER MENU PRINCIPAL ################
            elif opcionProveedores == '0':
                
                print('****VUELVE AL MENU PRINCIPAL****')
                muestroMenu()

            ############Si no coloca opcion Valida ################
            else:
                print("****NO SE HA ELEGIDO UNA OPCION VALIDA****")
                 ## seguir o salir
                print("DESEA CONTINUAR?")
                validador = seguirONo()


############MENU CLIENTES################
    elif opcion == '2':
                print("***************** CLIENTES *****************")
                print('''\n
            [1] -  Alta de Cliente
            [2] -  Baja de Cliente
            [3] -  Modificacion de Cliente
            [4] -  Mostrar Cliente


            [0]   VOLVER AL MENU PRINCIPAL ->
                ''')
                print("***********************************************")
                opcionClientes = input('Elija la opción deseada:')
                clearConsole()
                print(f"\nSu Opcion fue {opcionClientes}")

                ############ALTA DE CLIENTE################
                if opcionClientes =='1':
                    print("***************** CLIENTES *****************")
                    print("************** ALTA DE CLIENTE **************")    
                    dni=pedirDni()
                    if not existeCliente(dni):
                        nombreApellido=pedirNombre()
                        direccion=pedirDireccion()
                        telefono=pedirTelefono()
                        mail=pedirMail()
                        print('- SELECCION SITUACION ANTE IVA:')
                        situacionIva=listarSituacionIva()
                        for i in range(0,len(situacionIva)): #proveedores range 1
                            print(f'[{i+1}] {situacionIva[i]}')
                        opcionElegidaIva=input('')
                        if opcionElegidaIva == '1' or opcionElegidaIva =='2' or opcionElegidaIva =='3' or opcionElegidaIva =='4':
                            clienteNuevo=Clientes.Cliente(dni, nombreApellido, direccion, telefono, mail, opcionElegidaIva)
                            clienteNuevo.altaCliente()
                            dbMayorista.commit()
                            print('*** CLIENTE CREADO EXITOSAMENTE ***')
                            seguirONo()
                        else:
                            print("****NO SE HA ELEGIDO UNA OPCION VALIDA****")
                            print("DESEA CONTINUAR?")
                            seguirONo()
                    else:
                        print('****CLIENTE YA EXISTE****')
                        seguirONo()
                    
                
                ############BAJA DE CLIENTE################
                elif opcionClientes =='2':
                    print("***************** CLIENTES *****************")
                    print("************** BAJA DE CLIENTE **************")
                    dni=pedirDni()
                    buscarDniBaja=buscarDni(dni)
                    buscarDniBaja.borrarCliente(dni)
                    dbMayorista.commit()
                    print('****CLIENTE ELIMINADO****')
                    seguirONo()



                ############MODIFICACION DE CLIENTE################
                elif opcionClientes =='3':
                    print("***************** CLIENTES *****************")
                    print("******** MODIFICACION DE CLIENTE **********")
                    dni=pedirDni()
                    buscarDniModificar= buscarDni(dni)
                    dniAModificar=buscarDniModificar.mostrarCliente()
                    print(f'DNI:{dniAModificar[0]}\n')
                    print(f'NOMBRE Y APELLIDO:{dniAModificar[1]}\n')
                    print(f'DIRECCION:{dniAModificar[2]}\n')
                    print(f'TELEFONO:{dniAModificar[3]}\n')
                    print(f'MAIL:{dniAModificar[4]}\n')
                    print(f'SITUACION ANTE IVA:{IdporString(dniAModificar[5])}\n')
                    ###modifico
                    print(f'****INGRESE LOS DATOS A MODIFICAR****')
                    dni=pedirDni()
                    nombreApellido=pedirNombre()
                    direccion=pedirDireccion()
                    telefono=pedirTelefono()
                    mail=pedirMail()
                    situacionIva=listarSituacionIva()
                    for i in range(0,len(situacionIva)): #proveedores range 1
                        print(f'[{i+1}] {situacionIva[i]}')
                    opcionElegidaIva=input('')

                    clienteModificado=Clientes.Cliente(dni, nombreApellido, direccion, telefono, mail, opcionElegidaIva)
                    clienteModificado.editarCliente(dniAModificar[0])
                    dbMayorista.commit()
                    print('****CLIENTE MODIFICADO****')
                    seguirONo()

                    ############MOSTRAR DATOS DE CLIENTE################
                elif opcionClientes =='4':
                    print("***************** CLIENTES *****************")
                    print("******** BUSCAR Y MOSTRAR CLIENTE **********")
                    dni=pedirDni()
                    buscarDniBuscar= buscarDni(dni)
                    dniABuscar=buscarDniBuscar.consultarCliente('DNI', dni)
                    if len(dniABuscar)>0:
                        for reg in dniABuscar:
                            print(f'DNI:{reg[1]}\n')
                            print(f'NOMBRE Y APELLIDO:{reg[2]}\n')
                            print(f'DIRECCION:{reg[3]}\n')
                            print(f'TELEFONO:{reg[4]}\n')
                            print(f'MAIL:{reg[5]}\n')
                            print(f'SITUACION ANTE IVA:{IdporString(reg[6])}\n')
                            
                    seguirONo()
                
                 ############SUBMENU CLIENTES VOLVER MENU PRINCIPAL ################
                elif opcionClientes == '0':
                    print('****VUELVE AL MENU PRINCIPAL****')
                    muestroMenu()

                ############Si no coloca opcion Valida ################
                else:
                    print("****NO SE HA ELEGIDO UNA OPCION VALIDA****")
                    ## seguir o salir
                    print("DESEA CONTINUAR?")
                    validador = seguirONo()


############MENU ARRICULOS################
    elif opcion == '3':
        print("***************** ARTICULOS *****************")
        print('''\n
            [1] -   Alta / Baja / Modif
            [2] -   Ingreso de Remito
            [3] -   Listado de Artículos sin Stock


            [0]   VOLVER AL MENU PRINCIPAL ->
                ''')
        print("***********************************************")
        opcionArticulos = input('Elija la opción deseada:')
        clearConsole()
        print(f"\nSu Opcion fue {opcionArticulos}")

        ############SUBMENU ARTICULOS ALTA BAJA MODIF################
        if opcionArticulos =='1':
            print("***************** ARTICULOS *****************")
            print("************** ALTA/BAJA/MODIF  **************")
            print('''\n
            [1] -  Alta de Articulo
            [2] -  Baja de Articulo
            [3] -  Modificacion de Articulo


            [0]   VOLVER AL MENU PRINCIPAL ->
                ''')
            print("***********************************************")
            opcionArticuloAltaBajaModificacion = input('Elija la opción deseada:')
            clearConsole()
            print(f"\nSu Opcion fue {opcionArticuloAltaBajaModificacion}")

            ############ALTA DE ARTICULO################
            if opcionArticuloAltaBajaModificacion =='1':
                print("***************** ARTICULOS *****************")
                print("************* ALTA DE ARTICULO *************")
                codigo = pedirCodigo()
                if not existeArticulo(codigo):
                    nombreArticulo = input('- NOMBRE DE ARTICULO:')
                    print('- SELECCION RUBRO:')
                    rubro=listarRubros()
                    for i in range(0,len(rubro)):
                        print(f'[{i+1}] {rubro[i]}')
                    opcionRubro=input('')
                    precio=pedirPrecio()
                    stock= pedirStock()
                    articuloNuevo= Articulos.Articulo(codigo,nombreArticulo,opcionRubro, precio, stock)
                    articuloNuevo.altaArticulo()
                    dbMayorista.commit()
                    print('*** ARTICULO CREADO EXITOSAMENTE ***')
                    seguirONo()   
                else:
                    print('****ARTICULO YA EXISTE****')
                    seguirONo()
                        

            ############BAJA DE ARTICULO################
            elif opcionArticuloAltaBajaModificacion =='2':
                print("***************** ARTICULOS *****************")
                print("************* BAJA DE ARTICULO *************")
                codigo=pedirCodigo()
                buscarCodigoBaja=buscarCodigo(codigo)
                buscarCodigoBaja.borrarArticulo(codigo)
                dbMayorista.commit()
                print('****ARTICULO ELIMINADO****')
                seguirONo()
            
            ############MODIFICACION DE ARTICULO################
            elif opcionArticuloAltaBajaModificacion =='3':
                
                print("***************** ARTICULOS *****************")
                print("******** MODIFICACION DE ARTICULO ********")
                codigo=pedirCodigo()
                buscarCodigoModificar = buscarCodigo(codigo)
                codigoAModificar = buscarCodigoModificar.mostrarArticulo()
                print(f'CODIGO DE BARRA:{codigoAModificar[0]}\n')
                print(f'NOMBRE ARTICULO:{codigoAModificar[1]}\n')
                print(f'RUBRO:{IdporString(codigoAModificar[2])}\n')
                print(f'PRECIO:{codigoAModificar[3]}\n')
                print(f'STOCK:{codigoAModificar[4]}\n')
                
                ###modifico
                print(f'****INGRESE LOS DATOS A MODIFICAR****')
                codigo = pedirCodigo()
                nombreArticulo = input('- NOMBRE DE ARTICULO:')
                print('- SELECCION RUBRO:')
                rubro=listarRubros()
                for i in range(0,len(rubro)):
                    print(f'[{i+1}] {rubro[i]}')
                opcionRubro=input('')
                precio=pedirPrecio()
                stock= pedirStock()
                articuloModificado=Articulos.Articulo(codigo,nombreArticulo,opcionRubro,precio,stock)
                articuloModificado.editarArticulo(codigoAModificar[0])
                dbMayorista.commit()
                print('****ARTICULO MODIFICADO*****')
                seguirONo()
                
            
             ############SUBMENU ARTICULOS VOLVER MENU PRINCIPAL ################
            elif opcionArticuloAltaBajaModificacion == '0':
                print('****VUELVE AL MENU PRINCIPAL****')
                muestroMenu()

            
            ############Si no coloca opcion Valida ################
            else:
                print("****NO SE HA ELEGIDO UNA OPCION VALIDA****")
                ## seguir o salir
                print("DESEA CONTINUAR?")
                validador = seguirONo()

        ############SUBMENU ARTICULOS INGRESO DE REMITO################
        elif opcionArticulos =='2':
            print("***************** ARTICULOS *****************")
            print("************ INGRESO DE REMITO  ************")
        
        ############SUBMENU ARTICULOS ARTICULOS SIN STOCK################
        elif opcionArticulos =='3':
            print("***************** ARTICULOS *****************")
            print("*********** ARTICULOS SIN STOCK ***********")
            sinStock=buscarSinStock()
            for reg in sinStock:
                print(f'ID PRODUCTO: {reg[0]}')
                print(f'CODIGO DE BARRA:{reg[1]}')
                print(f'NOMBRE ARTICULO:{reg[2]}')
                print(f'ID RUBRO: {reg[3]}')
                print(f'PRECIO PUBLICO:{reg[4]}')
                print(f'STOCK: {reg[5]}')
                print(f'-------------------------')
                
            seguirONo()
        
        elif opcionArticulos =='0':
            print('****VUELVE AL MENU PRINCIPAL****')
            muestroMenu()
        
        else:
            print("****NO SE HA ELEGIDO UNA OPCION VALIDA****")
            ## seguir o salir
            print("DESEA CONTINUAR?")
            validador = seguirONo()

    ############MENU VENTAS################
    elif opcion == '4':
        print("***************** VENTAS *****************")
        print(f'''\n
    [1] -   Facturacion
    [2] -   Listado de ventas del dia {datetime.date.today()}


    [0]   VOLVER AL MENU PRINCIPAL ->
                ''')
        print("***********************************************")
        opcionVentas = input('Elija la opción deseada:')
        clearConsole()
        print(f"\nSu Opcion fue {opcionVentas}")

         ############SUBMENU VENTAS FACTURACION################
        if opcionVentas =='1':
            print("**************** VENTAS ****************")
            print("************** FACTURACION **************")
        
        ############SUBMENU VENTAS FACTURACION################
        elif opcionVentas =='2':
            print("**************** VENTAS ****************")
            print(f"******* VENTAS DEL DIA {datetime.date.today()} **************")
            ventasdelDia=buscarVentasDelDia()
            if len(ventasdelDia)>0:
                for reg in ventasdelDia:
                    print(f'NRO FACTURA: {reg[0]}')
                    print(f'FECHA: {reg[1]}')
                    print(f'TIPO DE FACTURA: {reg[3]}')
                    print(f'ID CLIENTE: {reg[4]}')
                    print(f'ID ARTICULO: {reg[5]}')
                    print(f'SUBTOTAL: {reg[8]}')
                    print(f'-------------------------')
                    
                seguirONo()
            else:
                seguirONo()
    
    if opcion == '0':
        print('******MUCHAS GRACIAS POR UTILIZAR SISTEMA MAYORISTA WILLY ******')
        exit()
        
        
        
        
        
        




                        
                    



    



    
    

