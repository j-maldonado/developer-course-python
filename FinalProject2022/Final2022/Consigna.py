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
    (30525390086, 'COCA COLA FEMSA', "Juan CocaCola", "Av. Amancio Alcorta 3570", "cocacolafemsa@mail.com", 46308999, ,1),
    (30537647716, 'PEPSICO DE ARGENTINA', "Jose Pepsi", "Cazadores de Coquimbo 2860", "pepsicoarg@mail.com", 55335000, 2),
    (30500572309, 'JOHNSON & JOHNSON DE ARGENTINA', "Gerardo Johnson", "RN8 km 63,5", "j&jargentina@mail.com", 4490101, 3),
    (30605206782, 'CLOROX ARGENTINA',"Miguel Clorox", "Coquimbo 2860", "cloroxargentina@mail.com", 52308200, 4),
    (30547242331, 'MASTELLONE HNOS',"Ricardo Mastellone", "Encarnación Ezcurra 365", "mastellonehermanos@mail.com", 4859000,  5),    
    (30501677643, 'SANCOR COOPERATIVAS UNIDAS',"Fernando Sancor", "Tacuarí 202", "sancorlacteos@mail.com" , 51763699,  6),
    (30502793175, 'ARCOR', "Reinaldo Arcor","Guillermo White 4546", "arcorarg@mail.com", 43109500,  7)
    ]
mycursor.executemany(sql, val)
dbMayorista.commit()
print(mycursor.rowcount, "Fueron insertados en tabla Proveedores.")
cur = dbMayorista.cursor()


##VALORES TABLA CLIENTES
mycursor = dbMayorista.cursor()
sql = "INSERT INTO Clientes (DNI, Nombre_Apellido, Direccion, Telefono, Mail , ID_IVA) VALUES (%s, %s, %s, %s, %s, %s)"
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
""" mycursor = dbMayorista.cursor()
sql = "INSERT INTO Articulos (CodigoBarras, Nombre, id_Rubro, Precio_Publico, Stock)"
val = [
    (7790895000218 , 'Coca-Cola', 2, 250,50),
    (7501055305650, 'Sprite', 2, 240, 80),
    (8410199021113, 'Lays Papas Fritas', 5, 140, 20),
    (7501031311606, 'Pepsi', 2, 220, 45),
    (7790010002301, 'Carefree', 6, 180, 25),
    (7891010619404, 'Listerine', 7, 135, 20),
    (7793253000998, 'Ayudin Gel', 1, 125, 23),
    (7793253004439, 'Ayudin Lavandina', 1, 105, 120),
    (7790742162106, 'Leche Descremada', 4, 108, 130),
    (7790895000218, 'Manteca', 4, 127, 30),
    (7798321151138, 'Yogs Firme', 4, 90, 107),
    (7790080014709, 'Queso Rallado', 4, 180, 200),
    (7790580221904, 'Pure de Tomate', 8, 120, 130),
    (7790580421007, 'Rocklets', 3, 150, 40)
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
cur = dbMayorista.cursor() """




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