#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------- conectamos con base de datos: MariaDB ----------------------------
# import sys
import mariadb # importa la libreria
"""
# conecto el motor de base de datos con usuario y pass que lo haya configurado en la instalacion
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            autocommit=True
        )
# print(mydb)  # veo si se conectó bien
"""
#--------------------------- creo mi base--------------------------------------------
# El cursor que conecta el sistema de administración de la base de datos como una programación 
# orientada a la recopilación y a la fila para permitir que los dos métodos de procesamiento 
# de datos se comuniquen
#-------------------------------------------------------------------------------------
"""
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mybase")
"""
# --------- verificamos si se creo la base --------------------------------------------
"""
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
"""
# intentamos conectar a la base creada ------------------------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
        )
"""
# creamos una tabla dentro de nuestra base con una clave primaria ----------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE cliente (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), dni INT, direccion VARCHAR(255))")
# si nos olvidamos de crear la clave primaria, podemos usar la siguiente sentencia para agregar un nuevo campo que sea clave primaria
# mycursor.execute("ALTER TABLE cliente ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
"""
# mostramos las tablas creadas ----------------------------------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for ind in mycursor:
  print(ind)
"""
# Utilizamos Insert para comenzar a llenar nuestra tabla --------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO cliente (nombre, dni, direccion) VALUES (%s, %s, %s)"
val = ("Eze Colonna", 28123456, "Alem 422")
mycursor.execute(sql, val)

mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
print(mycursor.rowcount, " Registro insertado.")  # muestro mensaje para saber que se insertaron bien
"""
# Para insertar multiples registros usamos executemany() -------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO cliente (nombre, dni, direccion) VALUES (%s, %s, %s)"
val = [
  ('Pedro', 42123123,'Santa Rosa 4'),
  ('Amalia', 11111111,'Dillon 652'),
  ('Analia', 22222222,'Aguado 21'),
  ('Miguel', 33333333,'Muñiz 345'),
  ('Sandra', 44444444,'Sarmiento blvd 2'),
  ('Beatriz', 55555555,'Cordoba Grass 1'),
  ('Ricardo', 66666666,'Corrientes 331'),
  ('Susana', 77777777,'Jujuy 98'),
  ('Victoria', 88888888,'Defilippi 2'),
  ('Benito', 99999999,'Argain 38'),
  ('Guillermo', 35123456,'Herrera 954'),
  ('Carlos', 28123456,'Lopez 989'),
  ('Violeta', 30123456,'Curuchet 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Fueron insertados.")
"""
# Conocer el Id de un registro insertado ------------------------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO cliente (nombre, dni, direccion) VALUES (%s, %s, %s)"
val = ('Pablo', 39123456,'Curapaligue 123')
mycursor.execute(sql, val)
mydb.commit()
print("1 registro insertado, ID:", mycursor.lastrowid)
"""
# Select from table --------------------------------------------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
#
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cliente")    # selecciono todos los registros de mi tabla cliente
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
#
print ("A partir de aquí hacemos un selec de 2 campos: nombre y direccion:")
mycursor.execute("SELECT nombre, direccion FROM cliente")  # selecciono 2 campos de la tabla
miResult = mycursor.fetchall()
for ind in miResult:
  print(ind)
#
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cliente")
myresult = mycursor.fetchone()               # recupero un solo registro con fetchone()
print("Con fetchone recupero un solo registro: ", myresult)
"""
# ---------------------------------- Select-From-Where ---------------------------------
# Seleccionar registros con filtro utilizando en el Select From Where ------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM cliente where direccion = 'Herrera 954' "
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""
# tambien podemos usar el comodin % para selecionar registros que empiecen, contengan o finalicen con
# una letra, frase o caracter
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM cliente where nombre LIKE '%Ana%' "
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""
# Podríamos seleccionar registros que cumplan con una condicion dada por el usuario:
"""
condicion = input("Ingrese el nombre que quiera buscar: ")
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM cliente where nombre LIKE '%"+condicion+"%'"
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""
# Ordenar el resultado de forma ascendente o descendente --------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM cliente ORDER BY nombre"
#sql = "SELECT * FROM cliente ORDER BY nombre DESC"  # ordenado de forma Descendente
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""
#------------------------------------------------------------------------------------
# Eliminar registros con DELETE
#------------------------------------------------------------------------------------
"""
condicion = input("Ingrese direccion a eliminar: ")
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "DELETE FROM cliente WHERE direccion LIKE '%"+condicion+"%'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " registros eliminados")
"""
# Eliminar una tabla usando DROP TABLE -----------------------------------------------
"""
# Primero creamos una nueva tabla para no perder los datos de la otra
# creamos una tabla dentro de nuestra base con una clave primaria --------------------
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE vendedor (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), dni INT, comision INT)")
mycursor.execute("SHOW TABLES")
for ind in mycursor:
  print(ind)
"""
# DROP TABLE - eliminar tabla y base si queremos -------------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
sql = "DROP TABLE vendedor"
mycursor.execute(sql)
#sql = "DROP TABLE IF EXISTS vendedor"   # Para evitar errores conviene usar Drop Table If Exist
#mycursor.execute(sql)
#sql = "DROP TABLE IF EXISTS cliente"    # Para evitar errores conviene usar Drop Table If Exist
#mycursor.execute(sql)
#sql = "DROP DATABASE mybase"            # elimino Base de datos
#mycursor.execute(sql)
mycursor.execute("SHOW TABLES")
for ind in mycursor:
  print(ind)
"""
# Actualizar registros utilizando UPDATE --------------------------------------------
"""
dni = input("Ingrese DNI de la persona: ")
dire = input("Ingrese direccion a cambiar: ")
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
# veo el registro original antes del cambio-----------------------
sql = "SELECT * FROM cliente where dni = "+dni
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
# actualizado aquí------------------------------------------------
sql = "UPDATE cliente SET direccion = '"+dire+"' WHERE dni = "+dni
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " registros modificados")
# veo el registro despues del cambio------------------------------
sql = "SELECT * FROM cliente where dni = "+dni
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""
# Podemos limitar la cantidad de registros que devuelve una consulta -------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cliente LIMIT 5")
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""
# Comenzar desde otra posición con OFFSET ---------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "mybase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM cliente LIMIT 5 OFFSET 6")
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""
#-----------------------------------------------------------------------------
# Combinar tablas utilizando JOIN --------------------------------------------
# Genero una nueva base con dos tablas relacionadas
#-----------------------------------------------------------------------------
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            autocommit=True
        )
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE videoclub")
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            database = "videoclub"
)
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "videoclub"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE peliculas (codbar INT PRIMARY KEY, nombre VARCHAR(255), genero VARCHAR(255), estado VARCHAR(255), dni INT)")
mycursor.execute("CREATE TABLE clientes (dni INT PRIMARY KEY, nombre VARCHAR(255), telefono INT, direccion VARCHAR(255), estado VARCHAR(1), codbar INT)")
mycursor = mydb.cursor()
sql = "INSERT INTO clientes (dni, nombre, telefono, direccion, estado, codbar) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
  (27178320,'Anabella Hidalgo',1112345678,'Florida 422','O',236957854),
  (38526847,'Carolina Hidalgo',1187654321,'Alem 3567','N',0),
  (35554845,'Laura Yumpa',1144556677,'Curapaligue 234','N',0),
  (25268036,'Ezequiel Colonna',1122332233,'Aguado 123','N',0),
  (46258458,'Lautaro Colonna Hidalgo',1199887766,'Muñiz 322','N',0),
  (36595485,'Cristina Aguirre',1122334455,'Sarmiento 1123','N',0),
  (25455485,'Facundo Martinez',1554218754,'Las Heras 1151','N',0),
  (36485145,'Sol Topia',1525846235,'Montes de Oca 2233','N',0),
  (35284852,'Laura Torres',1558452694,'Santa Rosa 2324','N',0),
  (45584125,'Patricia Alonso',1545216398,'Curuchet 432','N',0)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Fueron insertados en tabla Clientes.")
mycursor = mydb.cursor()
sql = "INSERT INTO peliculas (codbar, nombre, genero, estado, dni) VALUES (%s, %s, %s, %s, %s)"
val = [
  (236957854,'Ironman','Ciencia Ficcion','P',27178320),
  (629566962,'Superman','Ciencia Ficcion','N',0),
  (136952659,'Batman','Ciencia Ficcion','N',0),
  (665288421,'Spiderman','Ciencia Ficcion','N',0),
  (326541584,'Avengers','Ciencia Ficcion','N',0),
  (302250058,'X Men','Ciencia Ficcion','N',0),
  (999852154,'La casa de los espiritus','Drama','N',0),
  (515485254,'El niño del pijama a rayas','Historico','N',0),
  (887445887,'Emma','Drama','N',0),
  (325487874,'IT','Terror','N',0)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Fueron insertados en tabla Peliculas.")
"""
# Join combinaciond de tablas
"""
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            database = "videoclub"
)
mycursor = mydb.cursor()
#sql = "SELECT peliculas.nombre AS peli, clientes.nombre as user FROM peliculas INNER JOIN clientes ON clientes.dni = peliculas.dni"
# traigo aunque no cumpla con el criterio usando LEFT JOIN, en este caso peliculas
#sql = "SELECT peliculas.nombre AS peli, clientes.nombre as user FROM peliculas LEFT JOIN clientes ON clientes.dni = peliculas.dni"
# traigo aunque no cumpla con el criterio usando RIGHT JOIN, en este caso clientes
sql = "SELECT peliculas.nombre AS peli, clientes.nombre as user FROM peliculas RIGHT JOIN clientes ON clientes.dni = peliculas.dni"
mycursor.execute(sql)
myresultado = mycursor.fetchall()
for ind in myresultado:
  print(ind)
"""