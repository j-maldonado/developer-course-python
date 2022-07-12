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
    database = 'Mayorista_Willy'
)
mycursor = dbMayorista.cursor()
camposPedidos = ('Fecha', 'id_Proveedor', 'id_Articulo', 'cantidad', 'estado', 'nro_Remito', 'Total_Remito', 'Comentario')


##Creacion de Clase Pedido
class Pedido:
    def __init__(self, fecha, idProveedor, idArticulo, cantidad,  estado,nroRemito, totalRemito, comentario):
        self.fecha = fecha
        self.idProveedor = idProveedor
        self.idArticulo = idArticulo
        self.cantidad = cantidad
        self.estado = estado
        self.nroRemito=nroRemito
        self.totalRemito=totalRemito
        self.comentario= comentario

                

####Alta de Cliente   
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
        sqlModifica = 'UPDATE Pedidos SET '
        for i in range(0, len(camposPedidos)):
            if i == 7:   ####ultimo campo
                sqlModifica = sqlModifica + camposPedidos[i] + ' = \" '+ str(PedAux[i]) + '\"'
            elif i == 0:
                sqlModifica = sqlModifica + camposPedidos[i] + ' = \" '+str(PedAux[i])+ '\",'
            elif i == 1 or i==2 or i==3 or i==5 or i==6:
                sqlModifica = sqlModifica + camposPedidos[i] + ' = ' + str(PedAux[i]) + ', '
            else:
                sqlModifica =  sqlModifica + camposPedidos[i] + ' = \"' + PedAux[i] + '\", '

        sqlModifica = sqlModifica + ' WHERE id_Pedido = ' + str(valor)
        mycursor.execute(sqlModifica)
        dbMayorista.commit()


#### Ver datos Pedido
    def mostrarPedido(self):
        return self.fecha,self.idProveedor,self.idArticulo,self.cantidad,self.estado,self.nroRemito,self.totalRemito,self.comentario

#### Eliminar Pedido
    def borrarPedido(self,valor):
        sqlElimina = 'DELETE FROM Pedidos WHERE id_Pedido = ' + str(valor)
        mycursor.execute(sqlElimina)
        dbMayorista.commit()


if __name__ == '__main__':
    # Cliente_Campos = ('id_Cliente', 'DNI', 'NombreApellido', 'Direccion', 'Telefono', 'Mail', 'Id_Iva')
    # Campos = Cliente_Campos[0]
    # Valores = '%s'
    # for i in range(1, len(Cliente_Campos)):
    #     Campos = Campos + ',' + Cliente_Campos[i]
    #     Valores = Valores + ', %s'
    # print(Campos)
    # print(Valores)
    Ped = Pedido(datetime.date(2022, 7, 1), 2, 3, 5, 'en Proceso', 251091, 500, 'nada relevante 2')
    #PedNuev= Pedido('2022-07-01', 2, 3, 5, 'en Proceso', 251091, 500, 'nada relevante 2')
    Ped.altaPedido()
    #PedNuev.editarPedido(3)
    #consultaPedido= Ped.consultarPedido('Fecha','2022-07-01')
    # consultanombre=Cli.consultaCliente('NombreApellido','Ale')
    #print(Ped.mostrarPedido())
    #print(consultaPedido)
    # print(Cli.mostrarCliente())
    # CliM = Cliente(24155337,'ALEJANDRA MAGISTRALI','PACHECO DE MELO 2635','1149921315','ahilenrocio@gmail.com',1)
    #Cli.editarCliente(11111111)
    # print(CliM.mostrarCliente())
    # consultadni = Cli.consultaCliente('DNI', 24155337)
    #print(Cli.mostrarCliente())
    #Ped.borrarPedido('2')