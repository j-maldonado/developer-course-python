#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass


def limpiarPantalla(self):
    sisOper = os.name
    if sisOper == "posix":
        os.system('Clear')
    elif sisOper == 'ce' or sisOper == 'dos':
        os.system('cls')


def Menu(self):
    self.limpiarPantalla()


class usuario:
    
    def __init__(self):

        self.usuario = input('Usuario: ')
        self.password = getpass.getpass('Contrasena: ')
        self.tiposDeUsuarios = int(input(f'''
        -----------SISTEMAS DE SEGUROS -----------
        Usuario:  {self.usuario}

        Ingrese segun corresponda:
        [1] Administracion
        [2] Marketing
        [3] Productor
        [4] Siniestros
        [5] Gerencia
        [6] Sistemas

         -----------------------------------------
        '''))


    #Opcion 1 Administracion
        if self.tiposDeUsuarios == 1:
            print(f'''
            *****Menu ADMINISTRACION*****
            Usuario:  {self.usuario}
            ''')
            int(input('''
            [1] Gestiones Actuales
            [2] Nueva Gestion
            [3] Consultas de Clientes
            [4] RRHH

            [0] Salir
            -----------------------
            Seleccione la opcion deseada: 
            '''))

        #Opcion 2 MARKETING
        elif self.tiposDeUsuarios == 2:
            print(f'''
            *****Menu MARKETING*****
            Usuario:  {self.usuario}
            ''')
            int(input('''
            [1] Campanias Actuales Vigentes
            [2] Medicion de Campanias
            [3] Crear Nueva Campania
            [4] RRHH

            [0] Salir
            -----------------------
            Seleccione la opcion deseada: 
            '''))

        #Opcion 3 Productor
        elif self.tiposDeUsuarios == 3:
            print(f'''
            *****Menu PRODUCTOR*****
            Usuario:  {self.usuario}
            ''')
            int(input('''
            [1] Asegurados Actuales
            [2] Polizas Vencen este mes
            [3] Companias de Seguros
            [4] Calendario de Reuniones
            [5] RRHH

            [0] Salir
            -----------------------
            Seleccione la opcion deseada: 
            '''))

        #Opcion 4 SINIESTROS
        elif self.tiposDeUsuarios == 4:
            print(f'''
            *****Menu SINIESTROS***** 
            Usuario:  {self.usuario}
            ''')
            int(input('''
            [1] Cargar Siniestro
            [2] Seguimiento de Siniestros
            [3] Siniestros Aprobados
            [4] Siniestros Rechazados
            [5] Consulta de Clientes
            [6] Medicion de Siniestros
            [7] RRHH

            [0] Salir
            -----------------------
            Seleccione la opcion deseada: 
            '''))

        #Opcion 5 Gerencia
        elif self.tiposDeUsuarios == 5:
            print(f'''
            *****Menu GERENCIA*****
            Usuario: {self.usuario}
            ''')
            int(input('''
            [1] Personal Disponible
            [2] Proyectos Actuales
            [3] Metricas
            [4] Optimizacion de Procedmientos
            [5] Calendario de Reuniones
            [6] Asignacion de Tareas
            [7] RRHH

            [0] Salir
            -----------------------
            Seleccione la opcion deseada: 
            '''))

        #Opcion 6 Admin
        elif self.tiposDeUsuarios == 6:
             
            print(f'''
            *****Menu SISTEMAS*****
            Usuario: {self.usuario}
            ''')
            int(input('''
            [1] Alta Usuario
            [2] Baja Usuario
            [3] Modificacion Usuario

            [0] Salir
            -----------------------
            Seleccione la opcion deseada: 
            '''))


Usuario = usuario()
Usuario.Menu()
