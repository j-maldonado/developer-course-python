#!/usr/bin/env python
# _*_ coding: utf-8 _*_
###rubros y sit iva NOO CLASE

import mariadb

dbMayorista = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '25109',
    database = 'Mayorista_Willy',
    autocommit= True
)
mycursor = dbMayorista.cursor()
camposClientes = ('DNI', 'Nombre_Apellido', 'Direccion', 'Telefono', 'Mail', 'Id_Iva')


##Creacion de Clase Clientes
class Cliente:
    def __init__(self, dni, nombre, domicilio, telefono, mail,  id_Iva):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        self.mail = mail
        self.id_situacionIva = id_Iva
                

####Alta de Cliente   
    def altaCliente(self):
        Campos = camposClientes[0] #no seria 0?
        Valores = '%s'
        for i in range(1,len(camposClientes)):
            Campos = Campos + ',' + camposClientes[i]
            Valores = Valores + ', %s'

        sqlAlta = 'INSERT INTO clientes (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarCliente()
        mycursor.execute(sqlAlta,valAlta)
        dbMayorista.commit()


####Consulta de Cliente
    def consultarCliente(self, campo, valor):
        if campo == 'DNI':
            sqlConsulta = 'SELECT * FROM Clientes WHERE DNI = '+str(valor)
            mycursor.execute(sqlConsulta)
        elif campo == camposClientes[2]:
            sqlConsulta = 'SELECT * FROM clientes WHERE '+ str(camposClientes[2]) + ' LIKE \"%' + valor + '%\"' #
            mycursor.execute(sqlConsulta)

        Resultado = mycursor.fetchall()
        return Resultado


####Modificar datos de Cliente
    def editarCliente(self,valor):
        CliAux = self.mostrarCliente()
        sqlModifica = 'UPDATE clientes SET '
        for i in range(0, len(camposClientes)):
            if i == 5:   ####ultimo campo de Clientes
                sqlModifica = sqlModifica + camposClientes[i] + ' = '+ str(CliAux[i])
            elif i == 0 or i==3:
                sqlModifica = sqlModifica + camposClientes[i] + ' = ' + str(CliAux[i]) + ', '
            else:
                sqlModifica =  sqlModifica + camposClientes[i] + ' = \"' + CliAux[i] + '\", '

        sqlModifica = sqlModifica + ' WHERE DNI = ' + str(valor)
        mycursor.execute(sqlModifica)
        dbMayorista.commit()


#### Ver datos Cliente
    def mostrarCliente(self):
        return self.dni,self.nombre,self.domicilio,self.telefono,str(self.mail),self.id_situacionIva

#### Eliminar Cliente
    def borrarCliente(self,valor):
        sqlElimina = 'DELETE FROM Clientes WHERE DNI = ' + str(valor)
        mycursor.execute(sqlElimina)
        dbMayorista.commit()

