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
camposDevolucion = ('id_Articulo','Fecha', 'Cantidad', 'Estado','Motivo', 'Descripcion')

##Creacion de Clase Devolucion
class Devolucion:
    def __init__(self, idArticulo , fecha, cantidad, estado, motivo,  descripcion):
        self.idArticulo = idArticulo
        self.fecha = fecha
        self.cantidad = cantidad
        self.estado = estado
        self.idArticulo = idArticulo
        self.motivo = motivo
        self.descripcion=descripcion

                

####Alta Devolucion   
    def altaDevolucion(self):
        Campos = camposDevolucion[0]
        Valores = '%s'
        for i in range(1,len(camposDevolucion)):
            Campos = Campos + ',' + camposDevolucion[i]
            Valores = Valores + ', %s'

        sqlAlta = 'INSERT INTO devolucion_productos (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarDevolucion()
        mycursor.execute(sqlAlta,valAlta)
        dbMayorista.commit()


####Consulta de Devolucion
    def consultarDevolucion(self, campo, valor):
        if campo == 'id_Articulo':
            sqlConsulta = 'SELECT * FROM devolucion_productos WHERE id_Articulo = '+str(valor)
            mycursor.execute(sqlConsulta)
        elif campo == camposDevolucion[3]:
            sqlConsulta = 'SELECT * FROM devolucion_productos WHERE '+ str(camposDevolucion[3]) + ' LIKE \"%' + valor + '%\"' #
            mycursor.execute(sqlConsulta)

        Resultado = mycursor.fetchall()
        return Resultado


####Modificar datos de pedido
    def editarDevolucion(self,valor):
        DevAux = self.mostrarDevolucion()
        sqlModifica = 'UPDATE devolucion_productos SET '
        for i in range(0, len(camposDevolucion)):
            if i == 5:   ####ultimo campo 
                sqlModifica = sqlModifica + camposDevolucion[i] + ' = \" '+ DevAux[i] + '\"'
            elif i == 0 or i == 2:
                sqlModifica = sqlModifica + camposDevolucion[i] + ' = ' + str(DevAux[i]) + ', '
            elif i == 1:
                sqlModifica = sqlModifica + camposDevolucion[i] + ' = \" '+str(DevAux[i])+ '\",'
            else:
                sqlModifica =  sqlModifica + camposDevolucion[i] + ' = \"' + DevAux[i] + '\", '

        sqlModifica = sqlModifica + ' WHERE id_Articulo = ' + str(valor)
        mycursor.execute(sqlModifica)
        dbMayorista.commit()


#### Ver datos Pedido
    def mostrarDevolucion(self):
        return self.idArticulo,self.fecha,self.cantidad,self.estado,self.motivo,self.descripcion

#### Eliminar Pedido
    def borrarDevolucion(self,valor):
        sqlElimina = 'DELETE FROM devolucion_productos WHERE id_Articulo = ' + str(valor)
        mycursor.execute(sqlElimina)
        dbMayorista.commit()


if __name__ == '__main__':
    Dev = Devolucion(2, datetime.date.today(), 3,'en Proceso', 'Mal Estado producto', 'estaba todo podrido')
    NueDev = Devolucion(5,'2022-07-01', 3,'en Proceso', 'Mal Estado producto', 'estaba todo podrido')
    #PedNuev= Pedido('2022-07-01', 2, 3, 5, 'en Proceso', 251091, 500, 'nada relevante 2')
    Dev.altaDevolucion()
    #NueDev.editarDevolucion(2)
    #consultaDev= Dev.consultarDevolucion('id_Articulo',2)
    # consultanombre=Cli.consultaCliente('NombreApellido','Ale')
    #print(Ped.mostrarPedido())
    #print(consultaDev)
    #print(Dev.mostrarDevolucion())
    #Dev.borrarDevolucion(5)