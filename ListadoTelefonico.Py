#Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos de los clientes de una empresa. 
# El programa incorpora funciones para crear el fichero con el listado si no existe, para consultar el teléfono de un cliente, 
# añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listado debe estar guardado en el fichero de 
# texto listado.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una linea distinta

#!/usr/bin/env python
# -*- coding: utf-8 -*-

ArchiObj = open ('NuevoArchivo.txt', 'w')
ArchiObj.write ('Escribiendo contenido')
ArchiObj.write('Segunda Linea')
ArchiObj.write('Tercera Linea')
ArchiObj.close()

