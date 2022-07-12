#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import mariadb
import os

""" ABM - Gestión Comercial
Tendremos que gestionar un comercio (pueden elegir el rubro, ejemplo: kiosco, panadería, librería, indumentaria, calzado)
Tendremos las siguientes clases principales: cliente, proveedor, artículo y las que consideren necesarias.
Deberán dar de alta la base de datos teniendo en cuenta la relación entre las tablas a crear.

Menú:
   Proveedores:
         - Alta/Baja/Modificación de Proveedor (DNI, Nombre de Fantasía, Direccion, Telefono, mail, Situacion IVA (Inscripto, Exento, etc..))
         - Pedido de reposición a Proveedor
         - Devolución a proveedor: se podrá realizar una baja de stock de articulos de un proveedor para devolver, habrá que completar un campo Observacion o Estado(vencido, dañado, etc)
   Cliente:
         - Alta/Baja/Modificacion de Cliente (Tendrá un registro con un cliente "Consumidor final" para aquel que cliente que no quiera registrarse) (campos: DNI, ApellidoNombre, Direccion, Telefono, mail, Situacion Iva)
    Articulos:
         - Alta/Baja/Modificacion de Articulo (Codigo de barra, nombre, rubro/categoría, precio, stock, DNI-proveedor)
        - Ingreso de Remito: ingreso de stock de artículos de un proveedor.
         - Listado de Artículos sin Stock
    Ventas:
         - Facturación: dado un cliente, podrá comprar uno o varios artículos mostrando el monto a pagar y descontando del stock en cada artículo.
         - Listado de ventas del día: deberá mostrar todos los artículos vendidos en el día. """

#Creacion de Base
dbMayorista = mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="25109",
    autocommit=True,
    database='MayoristaWilly')

""" print(dbMayorista)
mycursor= dbMayorista.cursor()
mycursor.execute("CREATE DATABASE MayoristaWilly")
mycursor= dbMayorista.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) """



"""
######## CREACION DE TABLAS ########


mycursor = dbMayorista.cursor()
mycursor.execute("CREATE TABLE Proveedores (CUIT INT PRIMARY KEY, Nombre VARCHAR(255), Direccion VARCHAR(255), Telefono INT ,Mail VARCHAR(255), ID_IVA INT)")
dbMayorista.commit()

mycursor.execute("CREATE TABLE Clientes (DNI INT PRIMARY KEY, NombreApellido VARCHAR(255), Direccion VARCHAR(255), Telefono INT ,Mail VARCHAR(255), ID_IVA INT)")
dbMayorista.commit()

mycursor.execute("CREATE TABLE Situacion_IVA (ID_IVA INT AUTO_INCREMENT PRIMARY KEY, Situacion_IVA VARCHAR(255))")
dbMayorista.commit()

mycursor.execute("CREATE TABLE Articulos (Codigo_de_barra INT PRIMARY KEY, Nombre VARCHAR(255), Categoría VARCHAR(255), Precio FLOAT, Stock INT, CUIT_Proveedor INT)")
dbMayorista.commit()

mycursor.execute("CREATE TABLE Ventas (NUM_fact INT, Fecha_Venta DATE, Tipo_de_factura VARCHAR(255), Dni INT, Codigo_barra_articulo INT, Cantidad_Articulo INT, Valor_Articulo FLOAT, Subtotal FLOAT)")
dbMayorista.commit()

mycursor.execute("CREATE TABLE Pedidos (ID_PEDIDO INT AUTO_INCREMENT PRIMARY KEY, Fecha_pedido DATE, CUIT_Proveedor INT, Codigo_de_barra_Articulo INT, Cantidad_Articulo INT, Numero_Remito INT, Total_Remito FLOAT)")
dbMayorista.commit()
"""


######## INSERTO VALORES EN TABLAS ########

"""
##VALORES TABLA PROVEEDORES
 mycursor = dbMayorista.cursor()
sql = "INSERT INTO Proveedores (CUIT, Nombre, Direccion, Telefono, Mail, ID_IVA) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    (30525390086, 'COCA COLA FEMSA', "Av. Amancio Alcorta 3570", 46308999, "cocacolafemsa@mail.com" ,1),
    (30537647716, 'PEPSICO DE ARGENTINA', "Cazadores de Coquimbo 2860", 55335000,"pepsicoarg@mail.com", 2),
    (30500572309, 'JOHNSON & JOHNSON DE ARGENTINA', "RN8 km 63,5", 4490101, "j&jargentina@mail.com" , 3),
    (30605206782, 'CLOROX ARGENTINA', "Coquimbo 2860", 52308200, "cloroxargentina@mail.com",4),
    (30547242331, 'MASTELLONE HNOS', "Encarnación Ezcurra 365", 4859000, "mastellonehermanos@mail.com", 5),    
    (30501677643, 'SANCOR COOPERATIVAS UNIDAS', "Tacuarí 202", 51763699, "sancorlacteos@mail.com" , 6),
    (30502793175, 'ARCOR', "Guillermo White 4546", 43109500, "arcorarg@mail.com", 7)
    ]
mycursor.executemany(sql, val)
dbMayorista.commit()
print(mycursor.rowcount, "Fueron insertados en tabla Proveedores.")
cur = dbMayorista.cursor()


##VALORES TABLA CLIENTES
mycursor = dbMayorista.cursor()
sql = "INSERT INTO Clientes (DNI, NombreApellido, Direccion, Telefono, Mail , ID_IVA) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    (36596894, 'Joan Maldonado', "Mario Bravo 1155", 1557558051,'joanmarcelomaldonado@gmail.com', 8),
    (45150221, 'Tomas Ruiz', "Miguel 6864",1545557333, 'tomasruiz@mail.com', 9),
    (18224144, 'Isabel Gonzalez', "Galindo 22", 1550270737, 'isabelgonzalez@mail.com', 10),
    (66361440, 'Benjamín Ramos', "José 44380", 1544230399, 'benjaminramos@mail.com', 11),
    (12414255, 'Alonso Lopez', "Salomé 3", 1554091014, 'alonsolopez@mail.com', 12),    
    (42252194, 'Romina Roman', "Zamora 6187", 1544678784,'rominaroman@mail.com' , 13),
    (38138892, 'Miguel Dueñas', "Valladares 2045", 1553836062, 'migueldueñas@mail.com', 14)
    ]
mycursor.executemany(sql, val)
dbMayorista.commit()
print(mycursor.rowcount, "Fueron insertados en tabla Clientes.")
cur = dbMayorista.cursor()
 """

##VALORES TABLA ARTICULOS
mycursor = dbMayorista.cursor()
sql = "INSERT INTO Articulos (Codigo_de_barra, Nombre, Categoría, Precio, Stock, CUIT_Proveedor) (%s, %s, %s, %s, %s, %s)"
val = [
    (7790895000218 , 'Coca-Cola', "Bebida", 250,50, 30525390086),
    (7501055305650, 'Sprite', "Bebida", 240, 80, 30525390086),
    (8410199021113, 'Lays Papas Fritas', "Snack", 140, 20, 30537647716),
    (7501031311606, 'Pepsi', "Bebida", 220, 45, 30537647716),
    (7790010002301, 'Carefree', "Proteccion Femenina", 180, 25, 30500572309),
    (7891010619404, 'Listerine', "Cuidado Oral", 135, 20, 30500572309),
    (7793253000998, 'Ayudin Gel', "Limpieza", 125, 23, 30605206782),
    (7793253004439, 'Ayudin Lavandina', "Limpieza", 105, 120, 30605206782),
    (7790742162106, 'Leche Descremada', "Lacteos", 108, 130, 30547242331),
    (7790895000218, 'Manteca', "Lacteos", 127, 30, 30547242331),
    (7798321151138, 'Yogs Firme', "Lacteos", 90, 107, 30501677643),
    (7790080014709, 'Queso Rallado', "Lacteos", 180, 200, 30501677643),
    (7790580221904, 'Pure de Tomate', "Alimentos de Origen Vegetal", 120, 130, 30502793175),
    (7790580421007, 'Rocklets', "Golosinas", 150, 40, 30502793175)
    ]
mycursor.executemany(sql, val)
dbMayorista.commit()
print(mycursor.rowcount, "Fueron insertados en tabla Articulos.")
cur = dbMayorista.cursor()

##VALORES TABLA Situacion_IVA   #######NO INGRESO IDCLIENTES#######
mycursor = dbMayorista.cursor()
sql = "INSERT INTO Situacion_IVA (Situacion_Frente_a_IVA) (%s)"
val = [
   ('Monotributista'),
   ('Responsable Inscripto'),
   ('Exento'),
   ('Consumidor Final')
    ]
mycursor.executemany(sql, val)
dbMayorista.commit()
print(mycursor.rowcount, "Fueron insertados en tabla Situacion_IVA.")
cur = dbMayorista.cursor()




"""
######## CREACION DE CLASES ########


## CLASE PROVEEDORES
class Proveedores:
    def __init__ (self, cuit, nombre, direccion, telefono, mail, idIVA):
        self.cuit=cuit
        self.nombre= nombre
        self.direccion= direccion
        self.telefono= telefono
        self.mail = mail
        self.idIVA= idIVA

    def printProveedores(self):
        return self.cuit, self.nombre, self.direccion, self.telefono, self.mail, self.idIVA


## CLASE CLIENTES
class Clientes:
    def __init__ (self, dni, nombreApellido, direccion, telefono, mail, idIVA):
        self.dni=dni
        self.nombreApellido= nombreApellido
        self.direccion= direccion
        self.telefono= telefono
        self.mail = mail
        self.idIVA= idIVA

    def printClientes(self):
        return self.dni, self.nombreApellido, self.direccion, self.telefono, self.mail, self.idIVA


## CLASE SITUACION IVA
class Situacion_IVA:
    def __init__ (self, situacionIVA, idIVA):
        self.situacionIVA= situacionIVA
        self.idIVA= idIVA

    def printSituacion_IVA(self):
        return self.situacionIVA, self.idIVA

## CLASE ARTICULOS
class Articulos:
    def __init__ (self, codigoBarra, nombre, categoria, precio, cuitProveedor, stock):
        self.codigoBarra=codigoBarra
        self.nombre= nombre
        self.categoria= categoria
        self.precio= precio
        self.cuitProveedor = cuitProveedor
        self.stock= stock

    def printArticulos(self):
        return self.codigoBarra, self.nombre, self.categoria, self.precio, self.cuitProveedor, self.stock



## CLASE Ventas 
class Ventas:
    def __init__ (self, numFact, fechaVenta, tipoFactura, dniCliente , codigoArticulo, cantArticulo, valorArticulo, subtotalVenta):
        self.numFact=numFact
        self.fechaVenta= fechaVenta
        self.tipoFactura= tipoFactura
        self.dniCliente= dniCliente
        self.codigoArticulo= codigoArticulo
        self.cantArticulo= cantArticulo
        self.valorArticulo= valorArticulo
        self.subtotalVenta= subtotalVenta

    def printArticulos(self):
        return self.numFact, self.fechaVenta, self.tipoFactura, self.dniCliente, self.codigoArticulo, self.cantArticulo,  self.valorArticulo,  self.subtotalVenta


## CLASE Pedidos
class Pedidos:
    def __init__ (self, IDPedido, fechaPedido, cuitProveedor, codigoArticulo, cantArticulo, numeroRemito, totalRemito):
        self.IDPedido=IDPedido
        self.fechaPedido= fechaPedido
        self.cuitProveedor= cuitProveedor
        self.codigoArticulo= codigoArticulo
        self.cantArticulo = cantArticulo
        self.numeroRemito= numeroRemito
        self.totalRemito= totalRemito

    def printArticulos(self):
        return self.IDPedido, self.fechaPedido, self.cuitProveedor, self.codigoArticulo, self.cantArticulo, self.numeroRemito, self.totalRemito


######## FIN DE CREACION DE CLASES ########

"""