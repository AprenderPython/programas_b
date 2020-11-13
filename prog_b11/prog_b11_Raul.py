#!/usr/bin/python3
'''
Usuario: Raúl @spleyades (en Telegram)

Detalles Programa semanal: Crea un programa que via argumentos lea un
documento de texto e imprima en pantalla cuantas lineas tiene y el nombre
del archivo

Requerimientos:
°Imprimir en pantalla numero de lineas del archivo de texto
°Imprimir el nombre del archivo antes.
°Mostrar con algo de estetica el resultado.
'''

import sys

from pathlib import PurePath

from colorama import init, Fore, Style

# Inicializo la librería colorama y asigno a distintas variables estilos de
# colores de texto para usar luego al mostrar en pantalla
init()
colorBorde = Style.DIM + Fore.BLUE 
colorDescripcion = Style.DIM + Fore.CYAN
colorResultado = Style.BRIGHT + Fore.CYAN
colorError = Style.DIM + Fore.RED
longitudBorde = 80

# Verifico si se ingreso algún argumento
if len(sys.argv[1:]):
    try:            
        with open(sys.argv[1], 'r') as f:
            
            # Muestro borde decorativo
            titulo = " Información sobre el archivo ingresado "
            print("\n{0}{1}{2}{3}{0}{1}".format(
                colorBorde,
                "=" * int((longitudBorde - len(titulo)) / 2),
                colorDescripcion,
                titulo))
            
            # Muestro el nombre de archivo usando la librería pathlib que me
            # permite obtener nombre y extensión del archivo sin el path
            print(colorDescripcion + "Nombre de archivo:", end=" ")
            print(colorResultado + PurePath(f.name).name)                
            
            try:
                # El método list aplicado a un objeto archivo devuelve una
                # lista con las líneas de texto
                lineas = str(len(list(f)))
            except:
                # Si no puede devolver una lista de líneas se considera
                # que no es archivo de texto
                lineas = "Indeterminado"
            
            # Muestro información sobre cantidad de líneas
            print(colorDescripcion + "Cantidad de líneas:", end=" ")
            print(colorResultado + lineas)

            print(colorBorde + "=" * longitudBorde) 
    except:   
        # Genero un mensaje si no existe el archivo o no se puede leer         
        print(colorError + "\nNo existe o no se puede acceder al archivo")                        
else:
    print(colorError + "\nNo ha ingresado un nombre de archivo como argumento")