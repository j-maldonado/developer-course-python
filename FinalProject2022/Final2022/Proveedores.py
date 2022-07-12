#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import mariadb

dbMayorista = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '25109',
    database = 'Mayorista_Willy'
)
mycursor = dbMayorista.cursor()
camposProveedores = ('CUIT', 'Nombre', 'Titular','Direccion','Mail', 'Telefono', 'Id_Iva')


#### Creacion Clase Proveedores
class Proveedores:
    def __init__(self, cuit, nombre, titular, direccion, mail, telefono, idIva):
        self.cuit = cuit
        self.nombre = nombre
        self.titular = titular
        self.direccion = direccion
        self.mail = mail
        self.telefono = telefono
        self.idIva = idIva


    

#### Alta Proveedor
    def altaProveedor(self):
        Campos = camposProveedores[0]
        Valores = '%s'
        for i in range(1,len(camposProveedores)):
            Campos = Campos + ',' + camposProveedores[i]
            Valores = Valores + ', %s'

        sqlAlta = 'INSERT INTO proveedores (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarProveedor()
        mycursor.execute(sqlAlta,valAlta)
        dbMayorista.commit()


#### Consulta Proveedor
    def consultarProveedor(self, campo, valor):
            if campo == 'CUIT':
                sqlConsulta = 'SELECT * FROM proveedores WHERE CUIT = ' + str(valor)
                mycursor.execute(sqlConsulta)
            elif campo == camposProveedores[2]: #busca por nombre apellido proveedor
                sqlConsulta = 'SELECT * FROM proveedores WHERE '+ str(camposProveedores[2]) + ' LIKE \"%' + valor + '%\"'
                mycursor.execute(sqlConsulta)
            Resultado = mycursor.fetchall()
            return Resultado


    #### Modificar Proveedor
    def editarProveedor(self,valor):
            ProvAux = self.mostrarProveedor()
            sqlModifica = 'UPDATE proveedores SET '
            for i in range(0, len(camposProveedores)):
                if i == 6:
                    sqlModifica = sqlModifica + camposProveedores[i] + ' = '+ str(ProvAux[i])
                elif i == 0 or i==5:
                    sqlModifica = sqlModifica + camposProveedores[i] + ' = ' + str(ProvAux[i]) + ', ' 
                else:
                    sqlModifica =  sqlModifica + camposProveedores[i] + ' = \"' + ProvAux[i] + '\", '

            sqlModifica = sqlModifica + ' WHERE CUIT = ' + str(valor)
            mycursor.execute(sqlModifica)
            dbMayorista.commit()


    #### Ver datos Proveedor
    def mostrarProveedor(self):
            return self.cuit, self.nombre, self.titular, self.direccion, self.mail, self.telefono, self.idIva

    #### Eliminar Proveedor
    def borrarProveedor(self,valor):
            sqlElimina = 'DELETE FROM proveedores WHERE CUIT = ' + str(valor)
            mycursor.execute(sqlElimina)
            dbMayorista.commit()
