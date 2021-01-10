#!/usr/bin/python3
""" 
Detalles del programa semanal:

Crea un programa para descargar archivos de repositorios de GitHub. 

Requerimientos:
1.La URL la ingresa el usuario y luego el programa descargara el código de ese archivo 
sin tener que descargar todo el repo.

2. Guardar lo descargado en el directorio actual o configurar una opción para que el 
usuario elija donde descargarlo.

Opcional:
Tener la opción de descargar todo el repositorio

Programa alternativo:
°Crea un programa que tenga una funcion que imprima un nombre un numero de veces 
especificados por el usuario, la funcion debe contener 2 parametros que son:
1: un nombre introducido por el usuario, 
2: la cantidad de veces que se imprimira ese nombre

code: progb_16_tuuser.py
@aprenderpython
#webscraping

"""

# Comprobamos que estan todos modulos instalados
import sys
import re
import os
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

def check_url (url):
    """ Comprueba que la URL empieza con la github, sino directametne generamos una excepcion
    """
    m = re.search ('^https://(www\.)?github.com', url)
    if m:
        return url
    else:
        msg=f"{url}: No es una dirección de github -> 'https://github.com/usuario/..."
        raise argparse.ArgumentTypeError(msg)

def check_path (path):
    """ Comprueba que el path para guardar existe y hay permisos para escribir
        sino generamos una excepcion
    """
    r = os.path.isdir (path)
    r_w = os.access (path, os.W_OK)
    if r and r_w:
        return path
    else:
        msg=f"{path}: No es una ruta valida donde guardar los datos"
        raise argparse.ArgumentTypeError(msg)
    
def comprobar_argumentos ():
    parser = argparse.ArgumentParser (description="Búsqueda en google", epilog="@jabaselga")
    parser.add_argument ("-u", "--url", metavar="http://github.com/usuario/...", help="URL del fichero en GitHub a descargare", type=check_url)
    parser.add_argument ("-d", "--directorio", metavar="PATH", help="Ruta donde descarga el fichero '.' para directorio actual", type=check_path)
    parser.add_argument ("-r", "--repo", help="Descarga todo el repositorio en un ZIP", action="store_true")
    parser.add_argument ("-v", "--verbose", help="Muestra mas detalle", action="store_true")
       
    args = parser.parse_args() 

    return args 

def comprobar_url (url, args):
    """ Comprueba la URL si la introducimos manualmente, sino esta bien formada finalizamos el programa
    """
    m = re.search ('^https://(www\.)?github.com', url)
    if not m:
        print ("No es una dirección de github -> 'https://github.com/usuario/...")
        sys.exit ()
    else:
        if args.verbose:
            print ("URL valida, pertenecea github.com")
        return url

def check_ruta (ruta, args):
    """ Comprobar ruta y permisos
        Sino son validos finaliza la ejecución
    """
    r = os.path.isdir (ruta)
    r_w = os.access (ruta, os.W_OK)

    if args.verbose:
        print ("Path para guardar ficheros permitido")
    return r, r_w

def github_raw (url, args):
    """ Partiendo de la URL inicial genera la URL donde esta el fichero
    """
    rurl=url.replace("github.com","raw.githubusercontent.com")
    rurl=rurl.replace ("blob/","")
    if args.verbose:
        print ("Preparando ruta de descarga del fichero ...")
    return rurl

def github_download_file(rurl, args, ruta=None):
    """ Descarga el fichero y lo guarda
    """
    r = get(rurl)
   
    if r.status_code == 200:
        *_, filename = rurl.split ('/')
    
        fichero = open (ruta+"/"+filename, 'wb')
        fichero.write(r.content)
        fichero.close ()
        if args.verbose:
            print (F"Fichero {Fore.GREEN}{filename}{Fore.RESET} descargado")
    else:
        print ("URL erronea, compruebe USUARIO, REPO y FICHERO")
        sys.exit ()

def descargar_repo (url, args, ruta):
    """ Busca el ZIP del repositorio, y lo descarga
    """
    if args.verbose:
        print ("Descargando repositiorio completo ...")
    new_url, _= url.split("blob")
    page=get(new_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a'):
        h = link.get('href')
        
        if "zip" in h:
            ruta_zip = f"https://github.com/{h}" 
            _, user, repo, *_ = h.split ("/")
    
    *_, filename = ruta_zip.split ("/")
    
    fullname = f"{ruta}/{user}_{repo}_{filename}"
    
    r = get(ruta_zip)
    with open(fullname, "wb") as zip_file:
        zip_file.write(r.content)

    if args.verbose:
        print (f"Repositorio {Fore.GREEN}{repo}{Fore.RESET} descargado en formato zip -> {fullname}")
 
def main ():
    args = comprobar_argumentos()
    if args.verbose:
        print (f"{Fore.BLUE}________________________________________________________________________________")
        print ('Ejercicio b16. Descargas de archivos de github.')
        print ('@jabaselga')
        print (f"________________________________________________________________________________{Fore.RESET}")


# Comprobamos URL
    if args.url:
        url = args.url
    else:
        url = input ("Introduzca la URL del fichero a descargar: ").strip()
        url = comprobar_url(url, args)
    
    url_raw = github_raw (url, args)
    
# Comprobamos DIRECTORIO
    if args.directorio:
        ruta = args.directorio
    else:
        ruta = input ("Introduce la ruta para descargar el fichero. (VACIO para ruta actual): ").strip()
        if ruta == "":
            ruta = os.getcwd()

    r, rw = check_ruta (ruta, args)

# Descargar fichero y grabar
    if r and rw:
        github_download_file (url_raw, args, ruta)
    else:
        print ("Problemas para guardar el fichero. Ruta erronea o sin permisos.")
        sys.exit ()

# Descargar todo el repositorio
    if args.repo:
        todo = args.repo
    else:
        todo = input ("¿Quieres descargar todo el repositorio?")

    if todo:
        descargar_repo (url, args, ruta)

if __name__ == "__main__":
    main ()