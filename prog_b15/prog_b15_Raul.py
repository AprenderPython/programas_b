#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Usuario: Raúl @spleyades (en Telegram)

Detalles del programa semanal:

Crea un programa que haga una busqueda en google y tome los 3 primeros
resultados de la busqueda y las muestre en pantalla.

Requerimientos:
1.Hacer busqueda de google y mostrar los 5 primeros resultados
2.Utilizar algun metodo de entrada de texto para que el usuario pueda hacer
la busqueda de google.

Opcional:
Mostrar un pequeño pedazo del contenido de la web en los resultados (como
cuando haces una busquesa desde un navegador y ves que tiene de contenido
desde el pedazo de texto que te muestea google.

Se deben instalar la siguiente librería:
    pip install beautifulsoup4
    
'''

import requests
import os
import sys
import msvcrt
import platform
from bs4 import BeautifulSoup
from colorama import init, Fore, Style, Back

CANT_RESULTADOS = 5

# Estilos de texto para usar en los menúes
ESTILO_CABECERA = Style.NORMAL + Fore.WHITE + Back.CYAN
ESTILO_DESCRIPCION = Style.DIM + Fore.CYAN + Back.BLACK
ESTILO_RESALTADO = Style.BRIGHT + Fore.CYAN + Back.BLACK
ESTILO_LINEA_DIVISORIA = Style.BRIGHT + Fore.CYAN + Back.BLACK

# Esto devuelve un comando para limpiar pantalla dependiendo de la plataforma
# Como al final este proyecto solo funciona para Windows se podría omitir
LIMPIAR = "clear" if sys.platform.startswith("linux") else "cls"


def pulse_tecla_para_continuar():
    ''' Detecta una pulsación cualquiera del teclado para continuar '''
    print(ESTILO_DESCRIPCION + "\nPulse una tecla para continuar...")
    while True:
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            break


def main():
    
    # Inicializo la librería colorama y asigno a distintas variables estilos
    # de colores de texto para usar luego al mostrar en pantalla
    init()

    # Se especifican los User Agent Headers los cuales permiten que
    # el servidor identifique el sistema y la aplicación, de donde los
    # browsers quieren que los datos sean descargados.
    # Las cabeceras llevan información necesaria para la comunicación y
    # pueden incluir diferentes aspectos como: tipo de navegador que realiza 
    # la petición, dirección de la página solicitada, juego de caracteres
    # utilizado, etc
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; '
        'rv:79.0) Gecko/20100101 Firefox/79.0',
        'Host': 'www.google.com',
        'Referer': 'https://www.google.com/'
    }

    while True:

        # Obtengo el ancho de la pantalla (esto lo hago cada vez que muestro
        # el menú de nuevo por si se cambio el tamaño de la ventana)
        columnas = os.get_terminal_size().columns        

        # Asigno unos colores por defecto y limpio la pantalla
        print(ESTILO_DESCRIPCION)
        os.system(LIMPIAR)
        print(ESTILO_CABECERA + " " * columnas + "\r BUSCADOR DE TEXTO EN GOOGLE")
        
        # pedir en bucle ingresar un patron de búsqueda en google y validarlo    
        print(ESTILO_DESCRIPCION + "\nIngrese texto a buscar en Google "
            "(o escriba 0 para Salir): ", end = "")
        texto_busqueda = input(ESTILO_RESALTADO).strip()
        
        # Si ingreso 0, salgo del bucle y termino el programa
        if texto_busqueda == "0":
            break
        
        # Si se pulsa Enter sin ingresar nada no se sale del bucle
        if len(texto_busqueda) == 0:
            continue
        
        print(ESTILO_LINEA_DIVISORIA + columnas * "=")
        print(ESTILO_DESCRIPCION + f"Se mostrarán los {CANT_RESULTADOS}"
            " primeros resultados (aguarde unos segundos...):")
        

        # Quizás habría que considerar el hecho de los comandos de google
        # para hacer las búsquedas, por ejemplo: si se ingresan espacios 
        # pero sin comillas hay que agregar signo '+' para que busque bien; en
        # cambio si hay comillas se busca la frase literal sin agregar '+'
        # En síntesis... es un lío
        texto_busqueda = texto_busqueda.replace(' ', '+')
        url_busqueda = f'https://www.google.com/search?hl=es&q={texto_busqueda}'
        try:
            req = requests.get(url_busqueda, headers=HEADERS)
        except:
            print("Hay un problema para acceder a la página de google")
            continue
        
        # Intento usar el parser 'lxml' si está disponible porque leí por ahí
        # que es más eficiente, sino uso el 'html.parser'
        try:
            soup = BeautifulSoup(req.text, "lxml")
        except:
            soup = BeautifulSoup(req.text, "html.parser")
                      

        cantidad = 1
        # Itero por todos los elementos div de la clase 'g' que son los que
        # contienen los resultados en la página de google.
        # Se podría buscar también por class_='rc' creo
        for resultado in soup.findAll('div', class_='g'):

            # Busco la url y el titulo de cada resultado
            enlace = resultado.find('a', href=True)
            titulo = resultado.find('h3')
            
            # Si es un resultado válido con url y título muestro dicha info
            if enlace and titulo:
                enlace = enlace['href']
                titulo = titulo.get_text()
                
                if enlace != '#':
                    print(ESTILO_RESALTADO + f"\n-{cantidad}-")
                    print(ESTILO_DESCRIPCION + enlace)
                    print(ESTILO_RESALTADO + titulo)
                    
                    # Intento obtener las primeras líneas de texto de la página
                    introduccion = resultado.find('span', class_='aCOpRe')
                    if introduccion:
                        # Si encuentro ese elemento me quedo con el texto
                        # que contiene
                        introduccion = introduccion.get_text()
                        # Si no es texto vacío lo muestro    
                        if introduccion:
                            print(ESTILO_DESCRIPCION + introduccion)                        
                    cantidad += 1
                    # Cuando llego al máximo de resultados que quiero mostrar
                    # salgo del bucle for
                    if cantidad > CANT_RESULTADOS:
                        break
                        
        pulse_tecla_para_continuar()    
    
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()

  
