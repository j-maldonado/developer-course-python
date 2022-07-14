#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import mariadb

dbMayorista = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '25109',
    database = 'Mayorista_Willy',
    autocommit= True
)
mycursor = dbMayorista.cursor()
camposArticulos = ('CodigoBarras', 'Nombre', 'Id_Rubro', 'Precio_Publico', 'Stock')


##Creacion de Clase Articulos
class Articulo:
    def __init__(self, codigoBarras, nombre, idRubro, precioPublico, stock):
        self.codigoBarras = codigoBarras
        self.nombre = nombre
        self.idRubro = idRubro
        self.precioPublico = precioPublico
        self.stock = stock
                

####Alta de Articulo   
    def altaArticulo(self):
        Campos = camposArticulos[0]
        Valores = '%s'
        for i in range(1,len(camposArticulos)):
            Campos = Campos + ',' + camposArticulos[i]
            Valores = Valores + ', %s'

        sqlAlta = 'INSERT INTO articulos (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarArticulo()
        mycursor.execute(sqlAlta,valAlta)
        dbMayorista.commit()


    
        

####Consulta de Articulo
    def consultarArticulo(self, campo, valor):
        if campo == 'CodigoBarras':
            sqlConsulta = 'SELECT * FROM Articulos WHERE CodigoBarras = '+str(valor)
            mycursor.execute(sqlConsulta)
        elif campo == camposArticulos[1]: #busca por Nombre
            sqlConsulta = 'SELECT * FROM Articulos WHERE '+ str(camposArticulos[1]) + ' LIKE \"%' + valor + '%\"' #
            mycursor.execute(sqlConsulta)
        Resultado = mycursor.fetchall()
        return Resultado


####Modificar datos de Articulo
    def editarArticulo(self,valor):
        ArtAux = self.mostrarArticulo()
        sqlModifica = 'UPDATE Articulos SET '
        for i in range(1, len(camposArticulos)):
            if i == 4:   ####ultimo campo
                sqlModifica = sqlModifica + camposArticulos[i] + ' = '+ str(ArtAux[i])
            elif i == 0 or i==2 or i==3:
                sqlModifica = sqlModifica + camposArticulos[i] + ' = ' + str(ArtAux[i]) + ', '
            else:
                sqlModifica =  sqlModifica + camposArticulos[i] + ' = \"' + ArtAux[i] + '\", '

        sqlModifica = sqlModifica + ' WHERE CodigoBarras = ' + str(valor)
        mycursor.execute(sqlModifica)
        dbMayorista.commit()
        
    ####Modificar datos de Articulo
    def descontarStock(self,valor):
        stockNuevo= self.stock-valor
        sqlModifica = 'UPDATE Articulos SET stock ='+ str(stockNuevo) + ' WHERE CodigoBarras=' + str(self.codigoBarras)
        mycursor.execute(sqlModifica)
        dbMayorista.commit()


#### Ver datos de Articulo
    def mostrarArticulo(self):
        return self.codigoBarras,self.nombre,self.idRubro,self.precioPublico,self.stock

#### Eliminar Articulo
    def borrarArticulo(self,valor):
        sqlElimina = 'DELETE FROM articulos WHERE CodigoBarras = ' + str(valor)
        mycursor.execute(sqlElimina)
        dbMayorista.commit()
