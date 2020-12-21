#!/usr/bin/python3
""" 
Detalles del programa semanal:
Crea un programa que haga una busqueda en google y tome los 3 primeros resultados 
de la busqueda y las muestre en pantalla...

Requerimientos:
1.Hacer busqueda de google y mostrar los 3 primeros resultados
2.Utilizar algun metodo de entrada de texto para que el usuario pueda hacer la 
busqueda de google.

Opcional:
Mostrar un pequeño pedazo del contenido de la web en los resultados 
(como cuando haces una busquesa desde un navegador y ves que tiene de 
contenido desde el pedazo de texto que te muestea google.

Nota: El motor de busqueda puede ser google u otro de tu preferencia (ej: bing, duckgogo, etc)

Programa alternativo:

Programa que imprima unas operaciones matematicas con numeros ingresados por el usuario (5) y 
los imprima 1 cada segundo, mientras en cada operacion ira sumando cada numero ingresado y 
mostrara el avanze...
(Ej: 
1 + 2 = 3
3 + 7 = 10
10 + 1 = 11...)

code: progb_15_tuuser.py
@aprenderpython
#webscraping
"""

# Comprobamos que estan todos modulos instalados
import sys
try: 
    from requests import get
    from bs4 import BeautifulSoup
except Exception as e:
    print ("Module requests and bs4 are obligatory to instal")
    print (e)
    print ("Please install module: 'pip install <module>'")
    sys.exit ()

import argparse
import urllib.parse
from colorama import Fore, init

def comprobar_argumentos ():
    parser = argparse.ArgumentParser (description="Búsqueda en google", epilog="@jabaselga")
    parser.add_argument ("-t", "--texto", metavar="Texto busqueda", help="Texto para realizar la busqueda")
    parser.add_argument ("-n", "--num", help="Numero de búsquedas", type=int, choices=range(1, 10), default=3)
    parser.add_argument ("-v", "--verbose", help="Muestra mas detalle", type=int, choices=[1, 2, 3], default=2)
       
    args = parser.parse_args() 

    return args 

class Busqueda():
    def __init__ (self, topic, num, verbose):
        self.__topic = topic
        self.__num = num
        self.__verbose = verbose
        self.__error = None
        self.__www = []
        self.__descripcion = []
        self.__cabecera = []
    
    def buscar (self):
        self.__URL = f"https://www.google.com/search?q={self.__topic}&num=12"
        usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        
        try:
            self.__busqueda = get(self.__URL, headers=usr_agent)
        except Exception as e:
            self.__error = e
        else:    
            if self.__busqueda.status_code == 200:
                self.__busqueda_page = self.__busqueda.content
            else:
                self.__error = "An error has occurred."
    # hacer búsqueda

    def extraer (self):
        if not self.__error:
            soup = BeautifulSoup(self.__busqueda_page, 'html.parser')
            busquedas=soup.find_all('div', attrs={'class': 'g'})
            i = 0
            for result in busquedas:
                if i == self.__num:
                    return
                else:
                    i += 1
                link = result.find('a', href=True)
                title = result.find('h3')
                c= result.span.text
                if link and title:
                    self.__cabecera.append (c)
                    self.__www.append(link['href'])
                    d= result.find('span', attrs={'class': 'aCOpRe'}).text
                    self.__descripcion.append(d)

            
    def presentar (self):
        init ()     # Inicializa colorama
        if not self.__error:
            msg = f"Mostrando las {Fore.GREEN}{self.__num}{Fore.RESET} primeras busquedas de {Fore.GREEN}{self.__topic}{Fore.RESET}."
            print (msg)
            print ("-" * (len(msg)-20))
            if self.__verbose == 3:
                print (self.__URL)
        for i in range(len (self.__www)):
            if self.__verbose == 2 or self.__verbose == 3:
                print (self.__cabecera[i])
            print (f"{Fore.BLUE}{urllib.parse.unquote(self.__www[i])}{Fore.RESET}")
            if self.__verbose == 3:
                print (f"{Fore.YELLOW}{self.__descripcion[i]}{Fore.RESET}")
            print ("")
        print ("")
    # mostrar busqueda

def main ():
    args = comprobar_argumentos()
    if args.verbose == 3:
        print (f"{Fore.BLUE}________________________________________________________________________________")
        print ('Ejercicio b15. Busquedas en Google.')
        print ('@jabaselga')
        print (f"________________________________________________________________________________{Fore.RESET}")

    if args.texto:
        texto = args.texto
    else:
        texto = input ("Introduzca texto a buscar: ")
    b = Busqueda(texto, args.num, args.verbose)
    b.buscar()
    b.extraer()
    b.presentar()

if __name__ == "__main__":
    main ()