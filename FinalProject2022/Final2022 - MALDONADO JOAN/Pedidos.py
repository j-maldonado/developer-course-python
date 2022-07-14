#!/usr/bin/env python
# _*_ coding: utf-8 _*_
###rubros y sit iva NOO CLASE

from sqlite3 import Date
import mariadb
import datetime


dbMayorista = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '25109',
    database = 'Mayorista_Willy',
    autocommit= True
)
mycursor = dbMayorista.cursor()
camposPedidos = ('id_Pedido','Fecha', 'id_Proveedor', 'id_Articulo', 'cantidad', 'estado', 'nro_Remito', 'Total_Remito', 'Comentario')


##Creacion de Clase Pedido
class Pedido:
    def __init__(self, id_Pedidos, fecha, idProveedor, idArticulo, cantidad,  estado,nroRemito, totalRemito, comentario):
        self.id_Pedidos= id_Pedidos
        self.fecha = fecha
        self.idProveedor = idProveedor
        self.idArticulo = idArticulo
        self.cantidad = cantidad
        self.estado = estado
        self.nroRemito=nroRemito
        self.totalRemito=totalRemito
        self.comentario= comentario

                

####Alta de Pedido   
    def altaPedido(self):
        Campos = camposPedidos[0]
        Valores = '%s'
        for i in range(1,len(camposPedidos)):
            Campos = Campos + ',' + camposPedidos[i]
            Valores = Valores + ', %s'

        sqlAlta = 'INSERT INTO pedidos (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarPedido()
        mycursor.execute(sqlAlta,valAlta)
        dbMayorista.commit()


####Consulta de Pedido
    def consultarPedido(self, campo, valor):
        if campo == 'Fecha': #busca por id Fecha
            sqlConsulta = 'SELECT * FROM pedidos WHERE Fecha =\" '+str(valor)+ '\"'
            mycursor.execute(sqlConsulta)
        
        elif campo == 'id_Pedido': #busca por id pedido
            sqlConsulta = 'SELECT * FROM pedidos WHERE id_Pedido = '+str(valor)
            mycursor.execute(sqlConsulta)
        
        elif campo == camposPedidos[1]: #busca por id proveedor
            sqlConsulta = 'SELECT * FROM pedidos WHERE id_Proveedor = '+str(valor)
            mycursor.execute(sqlConsulta)


        Resultado = mycursor.fetchall()
        return Resultado


####Modificar datos de pedido
    def editarPedido(self,valor):
        PedAux = self.mostrarPedido()
        sqlModifica = 'UPDATE pedidos SET '
        for i in range(4, len(camposPedidos)):
            if i == 8:   ####ultimo campo
                sqlModifica = sqlModifica + camposPedidos[i] + ' = \" '+ str(PedAux[i]) + '\"'
            elif i == 1:
                sqlModifica = sqlModifica + camposPedidos[i] + ' = \" '+str(PedAux[i])+ '\",'
            elif i==4 or i==6 or i==7:
                sqlModifica = sqlModifica + camposPedidos[i] + ' = ' + str(PedAux[i]) + ', '
            else:
                sqlModifica =  sqlModifica + camposPedidos[i] + ' = \"' + str(PedAux[i]) + '\", '

        sqlModifica = sqlModifica + ' WHERE id_Pedido = ' + str(valor)
        mycursor.execute(sqlModifica)
        dbMayorista.commit()


#### Ver datos Pedido
    def mostrarPedido(self):
        return self.id_Pedidos, self.fecha,self.idProveedor,self.idArticulo,self.cantidad,self.estado,self.nroRemito,self.totalRemito,self.comentario

#### Eliminar Pedido
    def borrarPedido(self,valor):
        sqlElimina = 'DELETE FROM Pedidos WHERE id_Pedido = ' + str(valor)
        mycursor.execute(sqlElimina)
        dbMayorista.commit()

