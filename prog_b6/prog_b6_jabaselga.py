""" 
Requerimiento:

Crea un programa que imprima en pantalla la si el dispositivo host tiene conexion a internet

prog_b6_tuuser.py


v0.1 20200927 Hacer ping básico


LIBRERIAS ADICIONALES
pip install pythonping
pip install requests

"""

import requests
from pythonping import ping


# Lista de hosts con los que quiero comprobar la conexión a internet
hosts = ('1.1.1.1', '8.8.8.8', '9.9.9.9')

# dicionario para contener el resultado de los pines
r={}
for h in hosts:
    r[h] = ping (h)

# convertir el dicionario a cadena para facilitar la búsqueda
cadena = str(r.values())

# buscamos a ver si ha habido alguna respuesta
t = cadena.count('Reply')

if t > 0:
    # al menos ha funcionado 1 ping
    try:
        r = requests.get('https://www.google.es')
        print ('Hay conexión a internet y el DNS parece que resuelve')
    except:
        dns = False
        print ('Hay conexión a internet pero el DNS parece que no resuelve')
else:
    print ('No hay conexión a internet')