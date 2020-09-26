# Alias telegram: Rumivi
# Programa para comprobar la conexión a internet
print('Alias de telegram: Rumivi')

import os
import platform

def verificar_conexion():

    online = False

    # Hago ping a google.es, dependiendo si es windows se hace ping de una manera y otra
    if (platform.system() == 'Windows'):
        resultado = os.popen('ping -n 1 172.217.168.163')
    else:
        resultado = os.open('ping -c 1 172.217.168.163')

    # Compruebo el resultado si contiene un dato que me indique que hay conexion
    for linea in resultado.readlines():
        if ('ttl' in linea.lower()):
            online = True
            break

    return online
    

if verificar_conexion():
    print('Enhorabuena, tienes conexion a internet.')

else:
	print('Lo sentimos, no tienes conexion a internet.')
