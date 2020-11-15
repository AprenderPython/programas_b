import io
import argparse
import os
import sys

# Se usa para permitir el paso de parametros por consola
arg = argparse.ArgumentParser()
arg.add_argument("-d", "--directorio", help = "Especifica la ruta donde se encuentra el documento")
args = arg.parse_args()


# La funcion que permite que el programa funciones
def leeDocumentos(dir):

    path = os.path.split(dir)

    try:

        file = open(dir, "r")

        lines = file.readlines()

        file.close()

        print("------------------------------------")
        print("Nombre del Documento --> ",path[1])
        print("------------------------------------")
        print("Cantidad de Lineas --> ",len(lines))
        print("------------------------------------")

    except (PermissionError, FileNotFoundError):
        print("En la ruta especificada no existe el documento")
        sys.exit()

# Supuesto covid no deberia derles el dia

if args.directorio:

    dir1 = args.directorio

    leeDocumentos(dir1)
else:

    dir  = input("Ingresa la ruta del documento\n>>> ")

    leeDocumentos(dir)





    


