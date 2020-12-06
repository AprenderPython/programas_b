#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Usuario: Raúl @spleyades (en Telegram)

Detalles: Crea un programa que disponga de diferentes diseños para texto
en ascii y que el usuario pueda ver y elegir un diseño, luego el usuario
podra convertir texto normal a ese estilo antes seleccionado...

Requerimientos:
1.Diferentes diseños minimo 3
2.Un menu para seleccionar el tipo de letra/diseño
3.Imprimir el texto que el usuario escriba con el diseño escrito.

Programa alternativo:
Crea un programa que ejecute un bucle infinito hasta que el usuario escriba "z"

Requerimientos : instalar el módulo pyfiglet
                    pip install pyfiglet

'''

# Libreria para convertir texto en ASCII art
from pyfiglet import Figlet, FigletFont

# Libreria para mostrar texto en colores en la terminal
from colorama import init, Fore, Style, Back

import os
import sys
import msvcrt
import platform

# Constante con texto por defecto para convertir
TEXTO_POR_DEFECTO = "Python"

# Estilos de texto para usar en los menúes
ESTILO_CABECERA = Style.DIM + Fore.WHITE + Back.CYAN
ESTILO_DESCRIPCION = Style.DIM + Fore.BLACK + Back.WHITE
ESTILO_LINEA_DIVISORIA = Style.DIM + Fore.CYAN + Back.WHITE
ESTILO_RESALTADO = Style.DIM + Fore.CYAN + Back.WHITE

# Diccionario donde asocio un string con un estilo de texto 
ESTILOS_ASCII_ART = {
    'ESTILO_BLOODY' : Style.BRIGHT + Fore.RED + Back.BLACK,
    'ESTILO_BOTANY' : Style.DIM + Fore.WHITE + Back.GREEN,
    'ESTILO_SKY' : Style.NORMAL + Fore.WHITE + Back.CYAN,
    'ESTILO_STAR' : Style.NORMAL + Fore.CYAN + Back.BLACK,
    'ESTILO_STANDARD' : Style.NORMAL + Fore.CYAN + Back.BLUE,
    'ESTILO_MAGIC' : Style.DIM + Fore.BLACK + Back.MAGENTA,
    'ESTILO_SUNSET' : Style.BRIGHT + Fore.YELLOW + Back.RED,
}

# Lista de tuplas donde cada elemento es un tipo de letra ascii art y un string
# que representa una clave en un diccionario de estilos de colores de texto
TIPOGRAFIAS = [ 
        ('Bulbhead', 'ESTILO_STAR'),
        ('Block', 'ESTILO_SUNSET'),
        ('Drpepper', 'ESTILO_BOTANY'),
        ('Broadway', 'ESTILO_SKY'),
        ('Fender', 'ESTILO_SUNSET'),
        ('Banner3-D', 'ESTILO_STANDARD'), 
        ('Alligator', 'ESTILO_MAGIC'), 
        ('Starwars', 'ESTILO_STAR'),
        ('Cybermedium', 'ESTILO_STANDARD'),
        ('Contessa', 'ESTILO_BOTANY'), 
        ('Shimrod', 'ESTILO_BOTANY'),
        ('Graffiti', 'ESTILO_MAGIC'),
        ('Gothic', 'ESTILO_BLOODY'),
        ('Big', 'ESTILO_MAGIC'),
        ('Crawford', 'ESTILO_SKY'),
        ('Doom', 'ESTILO_SUNSET'),
        ('Chunky', 'ESTILO_SUNSET'), 
        ('Acrobatic', 'ESTILO_SKY'), 
        ('Poison', 'ESTILO_BLOODY'), 
        ('Univers', 'ESTILO_BOTANY') 
]

# Obtengo las tipografías ASCCI art disponibles en el sistema para luego testear
# si la puedo usar. Es una lista y paso todos los elementos a mayúsculas
TIPOGRAFIAS_DISPONIBLES = list(map(str.upper, FigletFont.getFonts()))

# Esto devuelve un comando para limpiar pantalla dependiendo de la plataforma
# Como al final este proyecto solo funciona para Windows se podría omitir
LIMPIAR = "clear" if sys.platform.startswith("linux") else "cls"

# --------------------------------- Métodos -----------------------------------

def pulse_tecla_para_continuar():
    ''' Detecta una pulsación cualquiera del teclado para continuar '''
    print(ESTILO_DESCRIPCION + " Pulse una tecla para continuar...")
    while True:
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            break


def muestro_ascii_art(texto, tipografia):    
    ''' Uso la librería Figlet para convertir el texto en ASCII art '''
    
    # Si la tipografía elegida está dentro de las instaladas puedo mostrarla
    if tipografia[0].upper() in TIPOGRAFIAS_DISPONIBLES:
        
        # Creo un objeto Figlet de la tipografía elegida
        ascii_art = Figlet(font=tipografia[0])
        
        # Limpio la pantalla y muestro la conversión
        print(ESTILO_DESCRIPCION)
        os.system(LIMPIAR)
        print(ESTILO_DESCRIPCION + "\n Tipografía usada: ", end = "")
        print(ESTILO_RESALTADO + f'"{tipografia[0]}"\n')        
        print(ESTILOS_ASCII_ART[tipografia[1]] + ascii_art.renderText(texto))        
    else:
        print(ESTILO_DESCRIPCION + "\n Hay un problema con el tipo de letra "
            f'"{tipografia[0]}" y no se puede mostrar.')
    
    pulse_tecla_para_continuar()


def mostrar_menu(texto_muestra):
    ''' Muestro con estética las opciones del menú '''
    
    # Obtengo el ancho de la pantalla (esto lo hago cada vez que muestro el
    # menú de nuevo por si se cambio el tamaño de la ventana)
    columnas = os.get_terminal_size().columns        
    
    # Asigno unos colores por defecto y limpio la pantalla
    print(ESTILO_DESCRIPCION)
    os.system(LIMPIAR)

    print(ESTILO_CABECERA + " " * columnas + "\r CONVERSOR DE TEXTO A ASCII-ART")
    print(ESTILO_DESCRIPCION + "\n Tipografías disponibles:\n")
    for nro, opcion in enumerate(TIPOGRAFIAS, 1):
        print(f"  {nro:2}. {opcion[0]}")
    print(ESTILO_DESCRIPCION + '\n Texto a convertir: ', end = "")    
    print(ESTILO_RESALTADO + f'"{texto_muestra}"')        
    print(ESTILO_LINEA_DIVISORIA + "=" * columnas)


def main():
     
    # Inicializo la librería colorama y asigno a distintas variables estilos
    # de colores de texto para usar luego al mostrar en pantalla
    init()

    # Ordeno la lista de tipografías alfabéticamente para mostrar en pantalla
    TIPOGRAFIAS.sort(key = lambda x: x[0].lower())

    # Asigno un valor por defecto al texto a mostrar
    texto_muestra = TEXTO_POR_DEFECTO

    while True:
        
        # En cada iteración vuelvo a mostrar el menú
        mostrar_menu(texto_muestra)
        
        # Pido ingresar una opción, que puede ser un número de tipografía o
        # la letra "T" para cambiar el texto o "0" para salir del script
        print(ESTILO_DESCRIPCION + ' Ingrese número de opción '
            '("T" para cambiar texto; "0" para salir): ', end = "")    
        eleccion = input(ESTILO_RESALTADO).strip()

        # Si ingreso una letra "T" pido un nuevo texto para convertir
        if eleccion.upper() == "T":
            print(ESTILO_DESCRIPCION + 
                "\n Ingrese el texto nuevo a convertir a ASCII-art: ", end = "")
            texto_muestra = input(ESTILO_RESALTADO).strip()
            if not texto_muestra:
                texto_muestra = TEXTO_POR_DEFECTO
                print("No ha ingresado nada. Se toma por defecto: "
                    f'{TEXTO_POR_DEFECTO}"')
                pulse_tecla_para_continuar()                    
            continue

        try:
            # Intento convertir a número entero
            eleccion = int(eleccion)
        except:            
            # Si no es número entero itero de nuevo en el bucle
            continue    
        else:
            #Si pulsa 0 se sale del bucle
            if eleccion == 0:
                break

            # Si ingresa un número dentro de los posibles muestro el texto
            # convertido en ASCII art
            if eleccion in range(1, len(TIPOGRAFIAS)+1):
                muestro_ascii_art(texto_muestra, TIPOGRAFIAS[eleccion-1]) 
            else:
                # Si no es número válido itero de nuevo
                continue    

    # Antes de salir del programa reseteo los colores de la pantalla
    print(Style.RESET_ALL)

# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()

    