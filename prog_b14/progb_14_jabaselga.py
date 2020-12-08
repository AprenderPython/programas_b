#!/usr/bin/python3
"""
Detalles del programa semanal:

Crea un programa que disponga de diferentes diseños para texto en ascii y 
que el usuario pueda ver y elegir un diseño, luego el usuario podra convertir 
texto normal a ese estilo antes seleccionado...

Requerimientos:
1.Diferentes diseños minimo 3
2.Un menu para seleccionar el tipo de letra/diseño
3.Imprimir el texto que el usuario escriba con el diseño escrito.

Programa alternativo:
Crea un programa que ejecute un bucle infinito hasta que el usuario escriba "z"

code: progb_14_tuuser.py

INCLUYE LOS DOS PROGRAMAS, el semanal y el alternativo.

LIBRERIAS ADICIONALES 

pip install art
pip install keyboard (requiere root en linux)

"""

import sys
from colorama import Fore, init
import argparse
import re

try:
    import art
except:
    print ("Es necesaria la librería 'art', puede instalar la con 'pip install art'")
    sys.exit(1) 

def solicitar_fuente ():
    respuesta=10
    while respuesta<0 or respuesta>7:
        for i, f in enumerate(fuentes):
            t = f"{i}-{f} | "
            print (t, end="") 
#        print ("7-random")
        print ("")
        try:
            respuesta=int (input ("Elige fuente: "))
        except:
            respuesta=10
    
    return respuesta

def solicitar_texto ():
    texto = input ("Introduce el texto a formatear: ")
    return texto
    
def imprimir_texto_fuente (fuente, texto):
    a=art.text2art(texto, font=fuente)
    print (a)
    
def check_font(string):
    pattern=re.compile(r'[0-7]')
    port_re=pattern.fullmatch(string)
    if port_re:
        return int(port_re.string)
    else:
        msg = f'{string} Fuente fuera de rango.'
        raise argparse.ArgumentTypeError(msg)

def bucle_infinito ():
    try:
        import keyboard
    except:
        print ("La libreria 'keyboard' no esta instalada. Instalar con 'pip install keyboard' (requiere root en linux)")
        sys.exit(1)

    print ("Bucle infinito, termina la pulsar 'z' ...")

    while True:
        if keyboard.read_key().lower()=="z":
            print ("Bucle finalizado")
            sys.exit (0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser (description="Formateo de textos con ASCII art", epilog="@jabaselga")
    parser.add_argument ("-f", "--font", metavar="font", help="Seleciona de 0 a 7", type=check_font)
    parser.add_argument ("-t", "--text", help="Texto a formatear")
    parser.add_argument ("-i", "--infinite", help="Bucle infinito", action="store_true")
       
    args = parser.parse_args()   

    init ()
    print (f"{Fore.BLUE}________________________________________________________________________________")
    print ('Ejercicio b14. Texto en ASCII.')
    print ('@jabaselga')
    print (f"________________________________________________________________________________{Fore.RESET}")

    if args.infinite:
        bucle_infinito ()
    
    fuentes = ["acrobatic", "alligator", "cybermedium", "doh", "fancy1", "russian", "swan"]


    if args.font:
        fuentes.append("random")
        f = fuentes[args.font]
        print (f"Fuente elegida: {f}")
    else:
        print ("De las siguientes fuentes elije una:")
        for i, f in enumerate(fuentes):
            t = f"{i}.- {f} {art.text2art(f, font=f)}"
            print (t) 
        fuentes.append("random")
        f = fuentes[solicitar_fuente()]
    
    if args.text:
        t = args.text
    else:
        t = solicitar_texto ()

    imprimir_texto_fuente (f, t)