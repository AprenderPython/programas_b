#!/usr/bin/python3
'''
Usuario: Raúl @spleyades (en Telegram)

Detalles: Extraccion de datos de cuentas de instagram
Requerimientos: Crea un programa que a partir de un nombre de usuario de
instagram ingresada por el usuario determine si la cuenta existe.
Si existe debe mostrar los siguientes datos de forma ordenada:

°Nombre de usuario
°Nombre
°Cantidad de seguidores
°Cantidad de seguidos
°Cantidad de publicaciones
°Si la cuenta es privada o publica
'''

# Uso expresiones regulares para validar la entrada del usuario y luego para
# poder quedarme con el fragmento de código fuente de la página de instagram
# donde están los datos que necesito
import re

# Uso requests para poder acceder a la página de instragram solicitada
# y quedarme con su código fuente 
import requests

# Uso la librería json para mapear el código script de la página de instagram
# y poder acceder en forma más fácil a los datos que necesito obtener
import json


def obtengo_datos(pagina):
    ''' Accedo a los datos que necesito de la cuenta de instagram usando
    la libreria json que me permite convertir el código javascript en una
    estructura de datos que maneja python con facilidad '''
    
    # Uso el siguiente patrón regex para capturar dentro del código fuente de
    # la página web el fragmento javascript donde están los datos que preciso
    PATRON_CAPTURA = r'window._sharedData = (\{.+?});</script>'
    texto_capturado = re.search(PATRON_CAPTURA, pagina.text).group(1)
    if texto_capturado:
        
        # Convierto el texto de la página web en una estructura de datos que
        # entienda python (diccionarios y listas anidados con datos)    
        texto_json = json.loads(texto_capturado)
        
        # Me quedo únicamente con un sector de esa estructura que es donde
        # están los datos del usuario de instagram
        cuenta = texto_json['entry_data']['ProfilePage'][0]['graphql']['user']
        
        # Muestro los datos 
        print('-' * 70)
        print(f"Nombre cuenta: @{cuenta['username']}")
        print(f"Nombre completo: {cuenta['full_name']}")
        print(f"Cantidad de publicaciones: "
            f"{cuenta['edge_owner_to_timeline_media']['count']}")
        print(f"Cantidad de seguidores: {cuenta['edge_followed_by']['count']}")
        print(f"Cantidad de seguidos: {cuenta['edge_follow']['count']}")
        if bool(cuenta['is_private']):
            print(f"La cuenta es privada.")
        else:   
            print(f"La cuenta es pública.")
        print('-' * 70)
    else:      
        print("Existe la cuenta de instagram pero no se puede acceder a los "
            " datos por el momento")
        
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    '''Uso expresiones regulares para controlar el ingreso. Solamente
    se pueden ingresar letras, números y guión bajo. No permito ingresar
    dos puntos seguidos, ni empezar o terminar en punto y limito la entrada
    de 1 a 30 caracteres.
    '''
    patron_ingreso = re.compile(r'^(?!.*\.\.)(?!.*\.$)\w[\w.]{0,29}$')
    
    while True:
        
        ingreso = input("\nIngrese nombre de usuario de instagram (o pulse 0 "
                        "para salir): ").strip()
        
        # Si ingreso 0, salgo del bucle y termino el programa
        if ingreso == "0":
            break
        
        # Si se pulsa Enter sin ingresar nada no se sale del bucle
        if len(ingreso) == 0:
            continue
        
        # Verifico que se ingrese una cadena de caracteres válida
        if patron_ingreso.search(ingreso):

            # Realizo la petición a la página web
            try:
                pagina = requests.get(f"https://www.instagram.com/{ingreso}/")
            except:
                # Si hubo un error al tratar de acceder a la página
                print("No se puede acceder a dicha página web.")                
            else: 
                # Si el status code = 200 implica que la página web existe
                if pagina.status_code == 200:
                    obtengo_datos(pagina)
                else:
                    print("No existe cuenta de instagram para el usuario "
                        "ingresado.")
        else:
            print("Error. Algunos de los caracteres ingresados no son válidos.")