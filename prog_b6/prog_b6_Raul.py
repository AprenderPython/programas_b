'''
Usuario: Raúl @spleyades (en Telegram)

Detalles: Crea un programa que imprima en pantalla la si el dispositivo host
          tiene conexion a internet
'''

import os
import platform

def hay_conexion_internet():

    conectado = False

    # Uso el comando ping para acceder a un servidor siempre activo, en este
    # caso el de google (8.8.8.8), para verificar si hay conexión a internet
    if (platform.system() == "Windows"):
        respuesta = os.popen("ping -n 1 8.8.8.8")
    else:
        respuesta = os.open("ping -c 1 8.8.8.8")

    # Leo el objeto de tipo archivo para encontrar el patrón de texto "ttl"
    # que determina que se pudo conectar al sitio
    for linea in respuesta.readlines():
        if ("ttl" in linea.lower()):
            conectado = True
            break

    return conectado
    

if hay_conexion_internet():
    print("Hay conexión a internet")
else:
    print("No hay conexión a internet")
