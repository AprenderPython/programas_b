# --------------------------------------------
# Propósito: Programa para imprimir el nombre de un archivo de texto y su cantidad de líneas a partir de la ubicación del mismo
#
# Fecha: 09/11/2020
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

from sys import argv, exit
import os

# Mostrar opción
if argv[1] == '?':
    print()
    print('python progb_11_dlcastillop.py [OPCIÓN...]')
    print('  Opción:')
    print('    -r "ruta del archivo"                       Indicar la ruta del archivo de texto')
    print()
    print('  Nota:')
    print('    1. La ruta hacia el archivo tiene que incluir el nombre del archivo y su extensión al final.')
    print('    2. Para indicar la ruta tienes que usar comillas en caso de que existan espacios en blanco.')
    print()
    exit(0)

# Inicializar variables
cantidad = 0
nombre = ''

# Opción -r
if argv[1] == '-r':
    if os.path.exists(argv[2]): # Comprobar que existe la ruta introducida
        ruta = argv[2]

        # Obtener el nombre
        for i in range(len(ruta)):
            if ruta[i] != '\\':
                nombre += ruta[i]
            else:
                nombre = ''
        
        archivo = open(argv[2], 'r') # Abrir archivo

        # Obtener cantidad de líneas
        for linea in archivo:
            cantidad += 1
        
        archivo.close() # Cerrar archivo
    
        # Imprimir nombre y cantidad de líneas
        print()
        print('Nombre del archivo:', nombre)
        if cantidad == 1:
            print('El archivo tiene una línea.')
        else:
            print('El archivo tiene', cantidad, 'líneas.')
        print()
    
    # En caso de que no exista la ruta introducida
    else:
        print()
        print('La ruta introducida no existe.')
        print()
        exit(0)

# En caso de que se introduzca otra opción
else:
    print()
    print('La opción introducida no es válida.')
    print()
    exit(0)