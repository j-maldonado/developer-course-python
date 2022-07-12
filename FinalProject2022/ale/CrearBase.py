#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import mariadb

# Crear Base
# dbPk = mariadb.connect(
#     host = "127.0.0.1",
#     user = 'root',
#     password = 'root',
#     autocommit = True
# )
#
# cur = dbPk.cursor()
# cur.execute('CREATE DATABASE Pk')

dbPk = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'root',
    database = 'Pk'
)
cur = dbPk.cursor()

#Generar las tablas
""" Cliente_Campos = ('id_Cliente','DNI','NombreApellido', 'Direccion', 'Telefono', 'Mail', 'Id_Iva')
TablaCliente = 'CREATE TABLE Clientes (id_Cliente INT AUTO_INCREMENT PRIMARY KEY, DNI BIGINT(8), NombreApellido VARCHAR(255),Direccion VARCHAR(255),Telefono BIGINT(20), Mail VARCHAR(150),Id_Iva BIGINT)'
 """

""" Proveedores_Campos = ('id_Proveedor', 'CUIT', 'RazonSocial', 'Titular','Direccion','Mail','Id_Iva')
TablaProveedores = 'CREATE TABLE Proveedores (id_Proveedor INT AUTO_INCREMENT PRIMARY KEY, CUIT BIGINT(11), RazonSocial VARCHAR(255), Titular VARCHAR(255), Direccion VARCHAR(255), Mail VARCHAR(150),Id_Iva BIGINT)'
 """

""" SituacionIVa_Campos = ('id_Iva','Situacion')
TablaSituacionIva = 'CREATE TABLE SituacionIva (id_Iva INT AUTO_INCREMENT PRIMARY KEY, Situacion VARCHAR(55))'
 """

""" 
TelProveedores_Campos = ('id_Proveedor','Telefono','Area','Contacto')
TablaTelProveedores = 'CREATE TABLE TelProveedores (' + TelProveedores_Campos[0] + ' BIGINT, '+TelProveedores_Campos[1] + ' BIGINT(20), '+TelProveedores_Campos[2] + ' VARCHAR(100), '+TelProveedores_Campos[3]+ ' VARCHAR(150))'
 """

""" Articulos_Campos = ('id_Articulo','CodigoBarras','Nombre','id_Rubro','CostoUnitario','PrecioFinal','id_Proveedor','UltimoPrecio','Stock_Minimo','Stock_Maximo','Cant_Stock')
TablaArticulos = 'CREATE TABLE Articulos (' + Articulos_Campos[0]+' INT AUTO_INCREMENT PRIMARY KEY,'+ Articulos_Campos[1] + ' BIGINT, ' + Articulos_Campos[2] + ' VARCHAR(150), '+ Articulos_Campos[3] +' INT,' + Articulos_Campos[4] + ' FLOAT, '+ Articulos_Campos[5] + ' FLOAT, ' + Articulos_Campos[6] + ' INT, ' + Articulos_Campos[7] + ' FLOAT, ' + Articulos_Campos[8] + ' INT, ' + Articulos_Campos[9] + ' INT)'
 """

""" Pedidos_Campos = ('id_Pedido','Fecha','id_Proveedor','id_Articulo','cantidad','estado','nro_Remito','Total_Remito','Motivo')
TablaPedidos = 'CREATE TABLE Pedidos (' + Pedidos_Campos[0] + ' INT AUTO_INCREMENT PRIMARY KEY,'+ Pedidos_Campos[1] + ' DATE, ' + Pedidos_Campos[2] + ' INT, '+ Pedidos_Campos[3] +' INT,' + Pedidos_Campos[4] + ' INT, '+ Pedidos_Campos[5] + ' VARCHAR(20), ' + Pedidos_Campos[6] + ' BIGINT, ' + Pedidos_Campos[7] + ' FLOAT, ' + Pedidos_Campos[8] + ' VARCHAR(20))'
 """

""" Rubros_Campos = ('id_Rubro','Detalle')
TablaRubros = 'CREATE TABLE Rubros (id_Rubro INT AUTO_INCREMENT PRIMARY KEY, Detalle VARCHAR(55))'
 """
 
Ventas_Campos = ('Nro_Factura','Fecha','Tipo_Factura','id_Cliente','id_Articulo','Detalle','Cantidad','Precio_Unitario','Subtotal')
TablaVentas = 'CREATE TABLE Ventas (' + Ventas_Campos[0] + ' BIGINT  PRIMARY KEY,'+ Ventas_Campos[1] + ' DATE, ' + Ventas_Campos[2] + ' VARCHAR(20), '+ Ventas_Campos[3] +' INT,' + Ventas_Campos[4] + ' INT, '+ Ventas_Campos[5] + ' VARCHAR(255), ' + Ventas_Campos[6] + ' INT, ' + Ventas_Campos[7] + ' FLOAT, ' + Ventas_Campos[8] + ' FLOAT)'

Art_Devolver_Campos = ('id_Articulo','Fecha','Cantidad','Estado','Motivo', 'Descripcion')
TablaArtDevolver = 'CREATE TABLE ArtDevolver (' + Art_Devolver_Campos[0] + ' INT  PRIMARY KEY,'+ Art_Devolver_Campos[1] + ' DATE, ' + Art_Devolver_Campos[2] + ' INT, '+ Art_Devolver_Campos[3] + ' VARCHAR(20),' + Art_Devolver_Campos[4] + ' VARCHAR(50), ' + Art_Devolver_Campos[5] + ' VARCHAR(255))'


cur.execute(TablaCliente)
dbPk.commit()
cur.execute(TablaProveedores)
dbPk.commit()
cur.execute(TablaPedidos)
dbPk.commit()
cur.execute(TablaVentas)
dbPk.commit()
cur.execute(TablaArtDevolver)
dbPk.commit()
cur.execute(TablaSituacionIva)
dbPk.commit()
cur.execute(TablaRubros)
dbPk.commit()
cur.execute(TablaTelProveedores)
dbPk.commit()

