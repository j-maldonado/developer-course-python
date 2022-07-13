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


#### Ver datos de Articulo
    def mostrarArticulo(self):
        return self.codigoBarras,self.nombre,self.idRubro,self.precioPublico,self.stock

#### Eliminar Articulo
    def borrarArticulo(self,valor):
        sqlElimina = 'DELETE FROM articulos WHERE CodigoBarras = ' + str(valor)
        mycursor.execute(sqlElimina)
        dbMayorista.commit()


#if __name__ == '__main__':
    #Articulos_Campos = ('CodigoBarras', 'Nombre', 'Id_Rubro', 'Precio_Publico', 'Stock')
 #   Art = Articulo(1234567,'Sprite',5,300,30)
    #print(Art.mostrarArticulo())
    #NueArt = Articulo(54677,'Coca',5,500,30)
  #  Art.altaArticulo()
    #NueArt.editarArticulo(54677)
    #consultacodigo= Art.consultarArticulo('Nombre','')
    # consultanombre=Cli.consultaCliente('NombreApellido','Ale')
    # print(consultanombre)
    #print(consultacodigo)
    # print(Cli.mostrarCliente())
    # CliM = Cliente(24155337,'ALEJANDRA MAGISTRALI','PACHECO DE MELO 2635','1149921315','ahilenrocio@gmail.com',1)
    
    # print(CliM.mostrarCliente())
    # consultadni = Cli.consultaCliente('DNI', 24155337)
    #print(Cli.mostrarCliente())
    #Art.borrarArticulo(234455)