#!/usr/bin/env python

'''
Hola Mundo! [Python]
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para ensayar el correcto funcionamiento
del entorno de instalación Python
'''
# import only system from os 
from os import system, name 
# import sleep to show output for some time period 
from time import sleep 
# define our clear function 
def clear(): 


    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
#borra la pantalla. Arriba setea el comando dependiendo del OS
clear()


__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"
clear
print("Hola Mundo! Tremendo 2020")
print("")
sleep (5)
print("Nos vemos en la próxima clase")
sleep (5)
print('chau! \n'*3) 


