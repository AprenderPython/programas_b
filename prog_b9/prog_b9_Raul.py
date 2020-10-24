#!/usr/bin/python3

'''
Usuario: Raúl @spleyades (en Telegram)

Detalles: Un escáner de puertos a una ip
Requerimientos: Crea un programa que escanee los puertos de una ip, deben haber
3 tipos de escaneo:

1.Escaneo rápido: Escaneara los puertos mas comunes.
2.Escaneo personalizado: El usuario debe ingresar cuales puertos quiere escanear
, ya sea por rango (10-20) o individual (10) o separados por coma (80, 443, 445)
3.Escaneo completo: El programa escaneara todos los puertos.

Luego el programa imprimirá en pantalla los puertos que esten abiertos.

El programa se puede ejecutar de dos formas:

1.Modo interactivo: El programa le pide al usuario que ingrese los datos
mediante inputs
2.Argumentos: al ejecutar el programa, mediante las opciones que ingrese el
usuario tomara esos datos para determinar el tipo de escaneo y demás datos
(ej: python -p 80 -i 10.10.10.1 -escaneoB) (NOTA: estas opciones son de ejemplo)
'''

import os
import re
import sys
import argparse
import socket

MAX_NRO_PUERTO = 65535

TIPO_ESCANEO = ["RÁPIDO", "COMPLETO" ,"PERSONALIZADO"]

PUERTOS_COMUNES = [21, 22, 25, 80, 110, 143, 443, 587, 993, 995, 2077, 2078,
                   2082, 2083, 2086, 2087, 2095, 2096, 3306, 6584]

# Patrón de búsqueda regex que verifica que se ingrese un número IP válido
PATRON_IP = re.compile(r'''^([01]?\d\d?|2[0-4]\d|25[0-5])\.
    ([01]?\d\d?|2[0-4]\d|25[0-5])\.
    ([01]?\d\d?|2[0-4]\d|25[0-5])\.
    ([01]?\d\d?|2[0-4]\d|25[0-5])$
    ''', re.VERBOSE)

def ip_valida(ingreso_ip):
    ''' Uso expresiones regulares para verificar que sea válida la IP '''
    return bool(re.findall(PATRON_IP, ingreso_ip.strip()))


def puerto_valido(cadena):
    ''' Verifico que el puerto sea un número dentro del rango posible '''
    try:
        x = int(cadena.strip())                    
    except:
        x = -1
    else:
        if (x < 0) or (x > MAX_NRO_PUERTO):
            x = -1
    return x     


def evaluar_ip(ingreso_ip, lista_puertos, tipo=0):
    ''' Se escanea la lista de puertos para la dirección IP indicada.
    El tercer parámetro se usa para indicar por pantalla el tipo de escaneo
    '''

    print(f"\nEscaneo de puertos: {TIPO_ESCANEO[tipo]} para la dirección IP: "
          f"{ingreso_ip}")
    
    for port in lista_puertos:
        cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        cliente.settimeout(0.05)
        conexion = cliente.connect_ex((ingreso_ip, port))
        if (conexion == 0):
            print(f'Puerto {port} ->\tABIERTO')
            cliente.close()
        else:
            print(f'Puerto {port} ->\tCERRADO')        


def puertos_ingresados_validos(ingreso_puertos):
    ''' A partir de un string que almacena una lista de puertos y/o rangos
    de puertos, se verifica que sea válido
    '''
    
    lista_aux = [i.strip() for i in ingreso_puertos.split(",")]
    lista_puertos = []
    for x in lista_aux:
        if "-" in x:
            lista_rango = [i.strip() for i in x.split("-")]                
            if len(lista_rango) == 2:
                a = puerto_valido(lista_rango[0])
                b = puerto_valido(lista_rango[1])
                if (a >= 0) and (b >= 0) and (a <= b):
                    lista_puertos = lista_puertos + list(range(a, b + 1))                        
        else:
            a = puerto_valido(x)
            if a >= 0:
                lista_puertos.append(a)                    
    return sorted(list(set(lista_puertos)))


def modo_argumentos():
    ''' Si ingreso argumentos, los analizo para ver si son válidos y de ser así,
    procedo a escanear los puertos para la dirección IP ingresada
    '''
    
    parser = argparse.ArgumentParser(description='Escaner de puertos')
    parser.add_argument('-i', '--i', dest='ingreso_ip', type=str, metavar='IP',
        help='Dirección IP a escanear')
    parser.add_argument('-s', '--s', dest='simple', action='store_true',
        help='Modo Simple (se escanean los puertos más comunes solamente)')
    parser.add_argument('-c', '--c', dest='completo', action='store_true',
        help='Modo Completo (se escanean todos los puertos)')
    parser.add_argument('-p', '--p', dest='ingreso_puertos', default='',
        type=str, nargs='+', metavar='PUERTOS', help='Modo Personalizado. '
        'Se deben indicar los puertos a escanear: puede ser un número único, '
        'una lista de valores separados por coma (Ej: 80, 443, 445) y/o un '
        'rango de valores (Ej: 23-50)')
    
    try:
        args = parser.parse_args()        
    except: 
        print("\nError de argumentos.")
        sys.exit(0)

    # verifico si se ingreso al menos un número de IP
    if args.ingreso_ip:
        # verifico si es un número IP válido
        if ip_valida(args.ingreso_ip):
            # Si se indicó -c se procede al escaneo completo
            if args.completo:
                evaluar_ip(args.ingreso_ip, range(MAX_NRO_PUERTO + 1), 1)
            elif len(args.ingreso_puertos):                
                # Si se indicó -p se procede al escaneo personalizado previo
                # validar si los puertos ingresados son válidos
                lista_puertos = puertos_ingresados_validos(
                    "".join(args.ingreso_puertos))
                if len(lista_puertos):            
                    evaluar_ip(args.ingreso_ip, lista_puertos, 2)
                else:
                    print("Error. No hay valores de puertos ingresados válidos")
            else:
                # Por defecto se hace un escaneo de puertos comunes
                evaluar_ip(args.ingreso_ip, PUERTOS_COMUNES, 0)            
        else: 
            print("Error. Es necesario ingresar una dirección IP válida para "
                  "evaluar.")
    
        
def modo_interactivo():        
    ''' Se pide ingresar un número de IP y tipo de escaneo a través de un menú
        interactivo de opciones
    '''
    
    while True:
        print()
        print("=" * 70)
        print("Escaneo de puertos de un dirección IP")
        print("=" * 70)

        ingreso_ip = input("\nIngrese una IP para evaluar (o pulse 0 para "
                           "salir): ").strip()

        if ingreso_ip == '0':
            break
        
        if len(ingreso_ip) == 0:
            continue

        if not ip_valida(ingreso_ip):
            print("Error. La dirección IP no es válida")
            continue
        
        print("\n1. Escaneo rápido (se escanean solamente los puertos más "
              "comunes)")
        print("2. Escaneo completo (el programa escaneara todos los puertos)")
        print("3. Escaneo personalizado (se deben especificar los puertos a "
              "escanear)")
        print("0. Salir")

        ingreso_opcion = input("\nIngrese una opción: ").strip()

        if ingreso_opcion == "0":
            break
        elif ingreso_opcion == "1":
            evaluar_ip(ingreso_ip, PUERTOS_COMUNES, 0)
        elif ingreso_opcion == "2":    
            evaluar_ip(ingreso_ip, range(MAX_NRO_PUERTO + 1), 1)
        
        elif ingreso_opcion == "3":
                   
            ingreso_puertos = input("\nIngrese un número de puerto (Ej: 10), "
                "una lista de puertos separados por coma (Ej: 80, 443, 445) y/o "
                "un rango de valores (Ej: 23-50): ").strip()

            lista_puertos = puertos_ingresados_validos(ingreso_puertos)            
            if len(lista_puertos):            
                evaluar_ip(ingreso_ip, lista_puertos, 2)
            else:
                print("Error. No hay valores de puertos ingresados válidos")


# ---------------------------------------------------------------------------

if __name__ == "__main__":

    # Uso manejo de excepciones para poder cancelar el script con CTRL+C  
    # en caso de que tarde mucho el escaneo de puertos

    try:
        # Verifico si se ingreso algún argumento. De no ser así, se entra en
        # modo interactivo
        if len(sys.argv[1:]):
            modo_argumentos()
        else:    
            modo_interactivo()
    except KeyboardInterrupt:
        print("\nEl programa fue interrumpido")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)   
