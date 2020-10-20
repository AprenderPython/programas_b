# --------------------------------------------
# Propósito: Programa para determinar los puertos TCP abiertos en tu PC
#
# Fecha: 20/10/2020
# --------------------------------------------
# Autor: Daniel Castillo
# 
# Página web: https://certificadocisco.blogspot.com
#
# Redes sociales:
# https://linkedin.com/in/dlcastillop
# https://twitter.com/dlcastillop
# https://github.com/dlcastillop
# --------------------------------------------

# Importar módulo socket
from socket import *

# --------------------------------------------
# FUNCIONES
# --------------------------------------------

# Función para escanear puertos TCP
# Se le pasa una cadena que representa una dirección IP y una lista de enteros que representan los puertos
def escaner_puertos (IP, lista_puertos):
    # Se recorren los puertos
    for puertos in lista_puertos:
        # Crear un socket. AF_INET indica que se usa IPv4 y SOCK_STREAM indica que se usa TCP
        cliente = socket(AF_INET, SOCK_STREAM)
        # Se guarda el resultado de la conexión a la dirección IP introducida con en un puerto. 
        resultado = cliente.connect_ex((IP, puertos))

        # Si resultado es 0 significa que el puerto está abierto
        if resultado == 0:
            print('Puerto', puertos, 'abierto')
            # Cerrar la conexión
            cliente.close()

# Función para obtener los puertos introducidos por el usuario en el formato que se especifica
# Se le pasa una cadena que representa a los puertos introducidos por el usuario y un caracter (- o ,) que es delimitador
def acomodar(cadena, caracter):
    #Inicializar variables
    puerto = ''
    puertos = []

    # Eliminar los espacios
    cadena = cadena.replace(' ','')

    # Añadir al final de la cadena el caracter
    cadena += caracter

    # Proceso de obtener los puertos introducidos por el usuario
    for i in range(len(cadena)):
        if cadena[i] != caracter:
            puerto += cadena[i]
        else:
            puerto = int(puerto)
            puertos.append(puerto)
            puerto = ''
    return puertos

# --------------------------------------------
# PROGRAMA
# --------------------------------------------

# Título
print('----------------------------------')
print('Programa para escanear puertos TCP')
print('----------------------------------')
print()

# Mostrar las opciones
print('Opciones:')
print('(1) Escaneo rápido')
print('(2) Escaneo personalizado')
print('(3) Escaneo completo')

# Pedir la opción deseada
opcion = input('Indica que opción quieres: ')

try:
    # Pedir dirección IP
    IP = input('Introduce la dirección IP que quieres escanear: ')

    # Acciones de la opción 1
    if opcion == '1':
        # Puertos más comunes de TCP
        puertos = [80, 443, 21, 22, 110, 995, 143, 993, 25, 26, 2525, 587, 3306, 2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078]
        
        # Escanear puertos de la IP
        escaner_puertos(IP, puertos)

    # Acciones de la opción 2
    elif opcion == '2':
        # Explicar cómo introducir los puertos
        print('Introduce los puertos que quieres escanear. Puedes introducir:')
        print('- Un puerto individual (ejemplo: 10)')
        print('- Un rango de puertos (ejemplo: 10 - 20)')
        print('- Una serie de puertos separados por comas(ejemplo: 10, 15, 18)')
        
        # Pedir los puertos
        cadena = input('Introduce los puertos: ')
        
        # Determinar la forma en que se ha introducido los puertos y posteriormente se escanea la IP con los puertos
        if cadena.find('-') != -1:
            cadena = acomodar(cadena, '-')
            puertos = list(range(cadena[0], cadena[1]+1))
            escaner_puertos(IP, puertos)
        elif cadena.find(',') != -1:
            puertos = acomodar(cadena, ',')
            escaner_puertos(IP, puertos)
        else:
            puerto = int(cadena)
            puerto = list(range(puerto, puerto + 1))
            escaner_puertos(IP, puerto)
    
    # Acciones de la opción 3
    elif opcion == '3':
        # Obtener todos los puertos
        puertos = list(range(0,65536))

        escaner_puertos(IP, puertos)
    
    # Acciones en caso de no introducir una opción válida
    else:
        print('No has introducido una opción válida.')

# Acciones en caso de que se introduzcan los puertos mal
except ValueError:
    print('Has introducido los puertos erróneamente.')

# Acciones en caso de que se introduzcan la dirección IP mal
except:
    print('No has introducido una dirección IP válida.')