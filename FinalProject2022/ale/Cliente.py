#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import mariadb

dbPk = mariadb.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'root',
    database = 'Pk'
)
cur = dbPk.cursor()
Cliente_Campos = ('id_Cliente', 'DNI', 'NombreApellido', 'Direccion', 'Telefono', 'Mail', 'Id_Iva')
CamposInt = (0, 1, 6)

class Cliente:
    def __init__(self, dni, nombre, domicilio, celular, mail,  id_Iva):
        self._dni = dni
        self._nombre = nombre
        self._celular = celular
        self._domicilio = domicilio
        self._mail = mail
        self.id_situacionIva = id_Iva

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, Dni):
        self._dni = Dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, Nombre):
        self._nombre = Nombre

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, Cel):
        self._celular = Cel

    @property
    def domicilio(self):
        return self._domicilio

    @domicilio.setter
    def domicilio(self, Domicilio):
        self._domicilio = Domicilio

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    def altaCliente(self):
        Campos = Cliente_Campos[1]
        Valores = '%s'
        for i in range(2,len(Cliente_Campos)):
            Campos = Campos + ',' + Cliente_Campos[i]
            Valores = Valores + ', %s'

        sqlAlta = 'INSERT INTO clientes (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarCliente()
        cur.execute(sqlAlta,valAlta)
        dbPk.commit()

    def consultaCliente(self, campo, valor):
        if campo == 'DNI':
            sqlConsulta = 'SELECT * FROM Clientes WHERE DNI = '+str(valor)
            cur.execute(sqlConsulta)
        elif campo == Cliente_Campos[2]:
            sqlConsulta = 'SELECT * FROM clientes WHERE '+ str(Cliente_Campos[2]) + ' LIKE \"%' + valor + '%\"' #
            cur.execute(sqlConsulta)

        Resultado = cur.fetchall()
        return Resultado

    def modificaCliente(self,valor):
        CliAux = self.mostrarCliente()
        sqlModifica = 'UPDATE clientes SET '
        for i in range(1, len(Cliente_Campos)):
            if i == 6:
                sqlModifica = sqlModifica + Cliente_Campos[i] + ' = '+ str(CliAux[i-1])
            elif i == 1:
                sqlModifica = sqlModifica + Cliente_Campos[i] + ' = ' + str(CliAux[i-1]) + ', '
            else:
                sqlModifica =  sqlModifica + Cliente_Campos[i] + ' = \"' + CliAux[i-1] + '\", '

        sqlModifica = sqlModifica + ' WHERE DNI = ' + str(valor)
        cur.execute(sqlModifica)
        dbPk.commit()

    def mostrarCliente(self):
        return self.dni,self.nombre,self.domicilio,self.celular,str(self.mail),self.id_situacionIva

    def borrarCliente(self,valor):
        sqlElimina = 'DELETE FROM Clientes WHERE DNI = ' + str(valor)
        cur.execute(sqlElimina)
        dbPk.commit()

if __name__ == '__main__':
    # Cliente_Campos = ('id_Cliente', 'DNI', 'NombreApellido', 'Direccion', 'Telefono', 'Mail', 'Id_Iva')
    # Campos = Cliente_Campos[0]
    # Valores = '%s'
    # for i in range(1, len(Cliente_Campos)):
    #     Campos = Campos + ',' + Cliente_Campos[i]
    #     Valores = Valores + ', %s'
    # print(Campos)
    # print(Valores)

    Cli = Cliente(11111111,'CESAR KESTERNICH','PACHECO DE MELO 2635','1149921999','cesarkesternich@gmail.com',2)
    Cli.altaCliente()
    # consultadni= Cli.consultaCliente('DNI',24155337)
    # consultanombre=Cli.consultaCliente('NombreApellido','Ale')
    # print(consultanombre)
    # print(consultadni)
    # print(Cli.mostrarCliente())
    # CliM = Cliente(24155337,'ALEJANDRA MAGISTRALI','PACHECO DE MELO 2635','1149921315','ahilenrocio@gmail.com',1)
    # CliM.modificaCliente(24155339)
    # print(CliM.mostrarCliente())
    # consultadni = Cli.consultaCliente('DNI', 24155337)
    # print(consultadni)
    #Cli.borrarCliente(11111111)
