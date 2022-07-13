#!/usr/bin/env python
# _*_ coding: utf-8 _*_
###rubros y sit iva NOO CLASE

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

camposVentas = ('Nro_Factura','Fecha', 'Tipo_de_Factura', 'id_Cliente','id_Articulo', 'Detalle', 'Cantidad', 'Precio_Publico', 'Subtotal')


##Creacion de Clase Clientes
class Ventas:
    def __init__(self, nroFactura, fecha, tipoFactura, idCliente, idArticulo,  detalle, cantidad, precioPublico, subtototal):
        self.nroFactura = nroFactura
        self.fecha = fecha
        self.tipoFactura = tipoFactura
        self.idCliente = idCliente
        self.idArticulo = idArticulo
        self.detalle = detalle
        self.cantidad=cantidad
        self.precioPublico=precioPublico
        self.subtototal= subtototal

                

####Alta de Venta   
    def altaVenta(self):
        Campos = camposVentas[0]
        Valores = '%s'
        for i in range(1,len(camposVentas)):
            Campos = Campos + ',' + camposVentas[i]
            Valores = Valores + ', %s'
        sqlAlta = 'INSERT INTO ventas (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarVenta()
        mycursor.execute(sqlAlta,valAlta)
        dbMayorista.commit()


####Consulta de Venta
    def consultarVenta(self, campo, valor):
        if campo == 'Nro_Factura':
            sqlConsulta = 'SELECT * FROM ventas WHERE Nro_Factura = '+str(valor)
            mycursor.execute(sqlConsulta)

        elif campo == 'Fecha':
            sqlConsulta = 'SELECT * FROM ventas WHERE Fecha =\" '+str(valor)+ '\"'
            mycursor.execute(sqlConsulta)
        
        elif campo == 'id_Cliente':
            sqlConsulta = 'SELECT * FROM ventas WHERE id_Cliente =\" '+str(valor)+ '\"'
            mycursor.execute(sqlConsulta)
    
        Resultado = mycursor.fetchall()
        return Resultado


####Modificar datos de Venta
    def editarVenta(self,valor):
        VenAux = self.mostrarVenta()
        sqlModifica = 'UPDATE ventas SET '
        for i in range(0, len(camposVentas)):
            if i == 8:   ####ultimo campo
                sqlModifica = sqlModifica + camposVentas[i] + ' = '+ str(VenAux[i])
            elif i == 1:
                sqlModifica = sqlModifica + camposVentas[i] + ' = \" '+str(VenAux[i])+ '\",'
            elif i == 0 or i == 3 or i == 4 or i == 6 or i == 7:
                sqlModifica = sqlModifica + camposVentas[i] + ' = ' + str(VenAux[i]) + ', '
            else:
                sqlModifica =  sqlModifica + camposVentas[i] + ' = \"' + VenAux[i] + '\", '

        sqlModifica = sqlModifica + ' WHERE Nro_Factura = ' + str(valor)
        mycursor.execute(sqlModifica)
        dbMayorista.commit()


#### Ver datos Pedido
    def mostrarVenta(self):
        return self.nroFactura, self.fecha, self.tipoFactura,self.idCliente,self.idArticulo,self.detalle,self.cantidad,self.precioPublico,self.subtototal

#### Eliminar Pedido
    def borrarVenta(self,valor):
        sqlElimina = 'DELETE FROM ventas WHERE Nro_Factura = ' + str(valor)
        mycursor.execute(sqlElimina)
        dbMayorista.commit()


if __name__ == '__main__':
    #Cliente_Campos = ('id_Cliente', 'DNI', 'NombreApellido', 'Direccion', 'Telefono', 'Mail', 'Id_Iva')
    #Campos = Cliente_Campos[0]
    # Valores = '%s'
    # for i in range(1, len(Cliente_Campos)):
    #     Campos = Campos + ',' + Cliente_Campos[i]
    #     Valores = Valores + ', %s'
    # print(Campos)
    # print(Valores)
    Ven = Ventas(6666, datetime.date(2022, 6, 3), 'Final', 3, 1, 'Detallado', 2 , 10 , 20)
    #NueVen=Ventas(9999, datetime.date(2022, 6, 3), 'Final', 3, 1, 'Detallado', 2 , 10 , 20)
    #NueVen.editarVenta(6666)
    Ven.altaVenta()
    #consultaVenta= Ven.consultarVenta('Nro_Factura',2345)
    # consultanombre=Cli.consultaCliente('NombreApellido','Ale')
    #print(consultaVenta)
    # print(consultadni)
    #print(Ven.mostrarVenta())
    # CliM = Cliente(24155337,'ALEJANDRA MAGISTRALI','PACHECO DE MELO 2635','1149921315','ahilenrocio@gmail.com',1)
    #Cli.editarCliente(11111111)
    # print(CliM.mostrarCliente())
    # consultadni = Cli.consultaCliente('DNI', 24155337)
    #print(Cli.mostrarCliente())
    #Ven.borrarVenta(9999)