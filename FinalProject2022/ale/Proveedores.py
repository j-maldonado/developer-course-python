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
Proveedores_Campos = ('id_Proveedor', 'CUIT', 'RazonSocial', 'Titular','Direccion','Mail','Id_Iva')
CamposInt = (0,1,6)

class Proveedores:
    def __init__(self, cuit, razonsocial, titular, direccion, mail, idIva):
        self._cuit = cuit
        self._nombre = razonsocial
        self._titular = titular
        self._direccion = direccion
        self._mail = mail
        self.idIva = idIva

    @property
    def cuit(self):
        return self._cuit

    @cuit.setter
    def cuit(self, cuit):
        self._cuit = cuit

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, razonsocial):
        self._nombre = razonsocial

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    def altaProveedor(self):
        Campos = Proveedores_Campos[1]
        Valores = '%s'
        for i in range(2,len(Proveedores_Campos)):
            Campos = Campos + ',' + Proveedores_Campos[i]
            Valores = Valores + ', %s'

        sqlAlta = 'INSERT INTO proveedores (' + Campos + ') VALUES (' + Valores + ')'
        valAlta = self.mostrarProveedor()
        cur.execute(sqlAlta,valAlta)
        dbPk.commit()

    def consultaProveedor(self, campo, valor):
        if campo == Proveedores_Campos[1]:
            sqlConsulta = 'SELECT * FROM proveedores WHERE CUIT = ' + str(valor)
            cur.execute(sqlConsulta)
        elif campo == Proveedores_Campos[2]:
            sqlConsulta = 'SELECT * FROM proveedores WHERE '+ str(Proveedores_Campos[2]) + ' LIKE \"%' + valor + '%\"' #
            cur.execute(sqlConsulta)
        elif campo == Proveedores_Campos[3]:
            sqlConsulta = 'SELECT * FROM proveedores WHERE ' + str(
                Proveedores_Campos[3]) + ' LIKE \"%' + valor + '%\"'  #
            cur.execute(sqlConsulta)

        Resultado = cur.fetchall()
        return Resultado

    def modificaProveedor(self,valor):
        CliAux = self.mostrarProveedor()
        sqlModifica = 'UPDATE proveedores SET '
        for i in range(1, len(Proveedores_Campos)):
            if i == 6:
                sqlModifica = sqlModifica + Proveedores_Campos[i] + ' = '+ str(CliAux[i-1])
            elif i == 1:
                sqlModifica = sqlModifica + Proveedores_Campos[i] + ' = ' + str(CliAux[i-1]) + ', '
            else:
                sqlModifica =  sqlModifica + Proveedores_Campos[i] + ' = \"' + CliAux[i-1] + '\", '

        sqlModifica = sqlModifica + ' WHERE DNI = ' + str(valor)
        cur.execute(sqlModifica)
        dbPk.commit()

    def mostrarProveedor(self):
        return self.cuit, self.nombre, self.titular, self.direccion, self.mail, self.idIva

    def borrarProveedor(self,valor):
        sqlElimina = 'DELETE FROM proveedores WHERE CUIT = ' + str(valor)
        cur.execute(sqlElimina)
        dbPk.commit()

if __name__ == '__main__':
    Cli = Proveedores(11111111, 'CESAR KESTERNICH', 'Losinstaladores', 'PACHECO DE MELO 2635', 'cesarkesternich@gmail.com', 2)
    # Cli.altaProveedor()
    consultadni= Cli.consultaProveedor('CUIT',11111111)
    consultarazon = Cli.consultaProveedor('RazonSocial', 'CESAR KESTERNICH')
    consultanombre=Cli.consultaProveedor('Titular','Losinstaladores')
    print(consultanombre)
    print(consultarazon)
    print(consultadni)
    print(Cli.mostrarProveedor())
    # CliM = Cliente(24155337,'ALEJANDRA MAGISTRALI','PACHECO DE MELO 2635','1149921315','ahilenrocio@gmail.com',1)
    # CliM.modificaCliente(24155339)
    # print(CliM.mostrarCliente())
    # consultadni = Cli.consultaCliente('DNI', 24155337)
    # print(consultadni)
    Cli.borrarProveedor(11111111)

