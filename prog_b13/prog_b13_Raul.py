#!/usr/bin/python3
'''
Usuario: Raúl @spleyades (en Telegram)

Detalles:
Crea un programa que disponga de varias opciones y estas ayuden al mantenimiento
de sistema

Requerimientos:
1.Minimo 4 opciones diferentes (ya sea mediante un menú o argumentos)
2.Mostrar una barra de estado mientras el proceso transcurre y/o mostrar
en que parte del proceso esta... (ej: borrando archivos..., borrando carpetas)
(lo de la barra de progreso no está hecho)

3.Mostrar con estetica

Prerequisito: funciona solamente en Windows y requiere (creo) Python 3.7+ 
para que funcionen algunas de las librerias
'''

from colorama import init, Fore, Style
import os
import subprocess
import sys
import platform
import msvcrt
import psutil

# Esto devuelve un comando para limpiar pantalla dependiendo de la plataforma
# Como al final este proyecto solo funciona para Windows se podría omitir
LIMPIAR = "clear" if sys.platform.startswith("linux") else "cls"

def pulse_tecla_para_continuar():
    ''' Detecta una pulsación cualquiera del teclado para continuar
    '''
    print(colorDescripcion + "\nPulse una tecla para continuar...")
    while True:
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            break


def get_size(bytes, sufijo="B"):
    '''
    Convierto el formato de bytes al formato adecuado
    Ej: 1253656 => '1.20MB'
        1253656678 => '1.17GB'
    '''
    factor = 1024
    for unidad in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unidad}{sufijo}"
        bytes /= factor


def cabecera_titulo(cadena):
    ''' Creo un borde estético para mostrar los títulos    
    '''

    borde = "=" * (len(cadena) + 10)
    print("\n" + colorBorde + borde)
    print(f"{colorDescripcion}     {cadena}")
    print(colorBorde + borde + "\n")    


def ver_info_sistema():
    ''' Muestro información sobre el sistema
    '''
    cabecera_titulo("Información del sistema")
    uname = platform.uname()
    print(colorDescripcion + " Nombre Sistema Operativo:", 
        colorResultado + str(uname.system))
    print(colorDescripcion + " Versión de publicación del sistema:",
        colorResultado + str(uname.version))
    print(colorDescripcion + " Nombre Red del ordenador:", 
        colorResultado + str(uname.node))
    print(colorDescripcion + " Procesador:", colorResultado + str(uname.processor))
    pulse_tecla_para_continuar()


def ver_info_memoria():
    ''' Muestro información sobre la memoria
    '''
    cabecera_titulo("Información de Memoria")
    svmem = psutil.virtual_memory()
    print(colorDescripcion + " Memoria total:", 
        colorResultado + get_size(svmem.total))
    print(colorDescripcion + " Memoria disponible:", 
        colorResultado + get_size(svmem.available))
    print(colorDescripcion + " Memoria usada:", 
        colorResultado + get_size(svmem.used), f"({svmem.percent}%)")
    pulse_tecla_para_continuar()
    

def ver_info_IP():
    ''' Muestro información de la configuración de la red
    '''
    
    subproceso = subprocess.Popen('IPCONFIG /all', shell=True, stdout= 
        subprocess.PIPE, stderr= subprocess.PIPE, universal_newlines=True)
    texto_salida, texto_error = subproceso.communicate()
    if subproceso.returncode == 0:
        cabecera_titulo("Información de Red")
        print(colorResultado + texto_salida)
    else:
        print("\nNo se puede acceder a la información de conexión")
    pulse_tecla_para_continuar()


def generar_lista_archivos():
    '''
    Genero a partir de una carpeta ingresada un archivo de texto con un listado
    de todos los archivos contenidos en dicha carpeta y en sus subcarpetas
    '''
    print(colorDescripcion + 
        "\nIngrese la ruta de la carpeta para generar listado: ", end = "")
    carpeta_datos = input(colorResultado).strip()
    if not os.path.isdir(carpeta_datos):
        print('No existe esa carpeta o no es un nombre válido')
        pulse_tecla_para_continuar()    
        return

    print(colorDescripcion + 
        "\nIngrese la ruta donde quiere guardar el listado: ", end = "")
    carpeta_destino = input(colorResultado).strip()
    if not os.path.isdir(carpeta_destino):
        print('No existe esa carpeta o no es un nombre válido')
        pulse_tecla_para_continuar()    
        return

    filename = os.path.join(carpeta_destino, "Listado_archivos.txt")
    try:
        p = subprocess.run(['dir', carpeta_datos, "/s"], stdout=subprocess.PIPE,
            shell = True)
        with open(filename, 'wb') as f:
            f.write(p.stdout) 
    except:
        print("\nNo se pudo generar el listado")
    else:
        print("\nOperación exitosa. Se ha guardado el listado en: " +
            carpeta_destino)        
    pulse_tecla_para_continuar()


def menu():
    ''' Muestro un menú de opciones (bastante simplonas por cierto porque
        no hice tiempo a hacer más cosas) 
    '''

    # Asocio en un diccionario una acción con una función
    opciones_menu = [
       ('Ver información sobre el sistema', ver_info_sistema),
       ('Ver información de memoria', ver_info_memoria),
       ('Ver configuración de Red', ver_info_IP),
       ('Generar lista de archivos', generar_lista_archivos)       
    ]

    while True:
        # Muestro un menú de opciones
        os.system(LIMPIAR)
        cabecera_titulo("Mantenimiento del Sistema")
        for nro, opcion in enumerate(opciones_menu, 1):
            print(colorDescripcion + f' {nro}. {opcion[0]}')
        print(colorDescripcion + ' 0. Salir')    
        print(colorDescripcion + "\nIngrese opción: ", end = "")    
        try:
            eleccion = int(input(colorResultado).strip())	
        except:
            # Si no ingresa un número itero de nuevo
            continue
        else:
            #Si pulsa 0 se sale del bucle
            if eleccion == 0:
                break
            if eleccion in range(1, len(opciones_menu)+1):
                opciones_menu[eleccion-1][1]()
            else:
                # Si no ingresa un número dentro del rango de opciones
                # itero de nuevo
                continue    
            
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    if sys.platform.upper() in ["WIN32", "WIN64"]:
        # Inicializo la librería colorama y asigno a distintas variables estilos
        # de colores de texto para usar luego al mostrar en pantalla
        init()
        colorBorde = Style.DIM + Fore.BLUE 
        colorDescripcion = Style.DIM + Fore.CYAN
        colorResultado = Style.BRIGHT + Fore.CYAN
        
        menu()
    else:
        print("Lamento informarle que este proyecto sólo funciona en Windows "
            "hasta nuevo aviso")