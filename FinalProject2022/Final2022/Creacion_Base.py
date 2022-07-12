#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys
import mariadb
import os

##### INICIO Creacion de Base de Datos

""" dbMayorista = mariadb.connect(
    host="127.0.0.1",
    user='root',
    password='25109',
    autocommit=True
)

mycursor = dbMayorista.cursor()
mycursor.execute('CREATE DATABASE Mayorista_Willy') """

##### FIN Creacion de Base de Datos

dbMayorista = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '25109',
    database = 'Mayorista_Willy'
)
mycursor = dbMayorista.cursor()

######## CREACION DE TABLAS ########

###Creacion Tabla Proveedores con Campos
mycursor.execute('CREATE TABLE Proveedores (id_Proveedor INT AUTO_INCREMENT PRIMARY KEY, CUIT BIGINT(11), Nombre VARCHAR(255), Titular VARCHAR(255), Direccion VARCHAR(255), Mail VARCHAR(150), Telefono BIGINT(20), Id_Iva BIGINT)')
dbMayorista.commit()

###Creacion Tabla Clientes con Campos
mycursor.execute('CREATE TABLE Clientes (id_Cliente INT AUTO_INCREMENT PRIMARY KEY, DNI BIGINT(8), Nombre_Apellido VARCHAR(255),Direccion VARCHAR(255),Telefono BIGINT(20), Mail VARCHAR(150),ID_Iva BIGINT)')
dbMayorista.commit()

###Creacion Tabla Situacion Iva con Campos
mycursor.execute('CREATE TABLE Situacion_Iva (ID_Iva INT AUTO_INCREMENT PRIMARY KEY, Situacion VARCHAR(55))')
dbMayorista.commit()

###Creacion Tabla Articulos con Campos
mycursor.execute('CREATE TABLE Articulos ( id_Articulo INT AUTO_INCREMENT PRIMARY KEY, CodigoBarras BIGINT, Nombre VARCHAR(150), id_Rubro INT, Precio_Publico FLOAT, Stock INT)')
dbMayorista.commit()

###Creacion Tabla Pedidos con Campos
mycursor.execute('CREATE TABLE Pedidos (id_Pedido INT AUTO_INCREMENT PRIMARY KEY, Fecha DATE, id_Proveedor INT, id_Articulo INT, cantidad INT, estado VARCHAR(20), nro_Remito BIGINT, Total_Remito FLOAT, Comentario VARCHAR(100))')
dbMayorista.commit()

###Creacion Tabla Ventas con Campos
mycursor.execute('CREATE TABLE Ventas (Nro_Factura BIGINT PRIMARY KEY,Fecha DATE, Tipo_de_Factura VARCHAR(20), id_Cliente INT,id_Articulo INT, Detalle VARCHAR(255), Cantidad INT, Precio_Publico FLOAT, Subtotal FLOAT)')
dbMayorista.commit()

###Creacion Tabla Devolucion_Productos con Campos
mycursor.execute('CREATE TABLE Devolucion_Productos (id_Articulo INT  PRIMARY KEY,Fecha DATE, Cantidad INT, Estado VARCHAR(20), Motivo VARCHAR(50), Descripcion VARCHAR(255))')
dbMayorista.commit()

###Creacion Tabla Rubros con Campos
mycursor.execute('CREATE TABLE Rubros (id_Rubro INT AUTO_INCREMENT PRIMARY KEY, Detalle VARCHAR(55))')
dbMayorista.commit()






