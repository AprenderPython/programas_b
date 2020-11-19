#!/usr/bin/python3
'''
Detalles Programa semanal: Crea un programa que mediante argumentos
(ej: python archivo.py argumento) pueda convertir de texto a base64
y viceversa.

Requerimientos:
-Determinar si es texto plano o base64 para luego imprimir la conversion,
 puede ser mediante argumentos, ej: -texto o -base64, (o si no se ingresa 
 ningún argumento se presenta un menú de opciones para elegir)
-Imprimir el resultado de la conversion.
'''

import sys
import argparse
from colorama import init, Fore, Style

# Guardo en una cadena los 64 caracteres que se usan para convertir a base64
CARACTERES_BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
CARACTERES_BASE64 += "0123456789/+"

def decimal_a_binario(nro_decimal):
    ''' Convierto un número decimal (base 10) en una cadena (string)
        que represente el mismo número en binario (base 2) '''

    # Inicializo una cadena donde voy a ir concatenando las cifras binarias
    cadena = ""
    while True:

        # Si llego a obtener un nro_decimal que sea 0 o 1 salgo de la función
        # retornando dicho número concatenado al principio de la cadena 
        # que fui armando
        if nro_decimal <= 1:
            return str(nro_decimal) + cadena
        
        # Le concateno a la cadena al principio un "0" o un "1" dependiendo
        # del resto de dividir por 2 el nro_decimal
        cadena = str(nro_decimal % 2) + cadena
        
        # Voy dividiendo al nro_decimal por 2 en cada interacción del bucle
        nro_decimal = int(nro_decimal / 2)


def binario_a_decimal(cadena_binaria):
    ''' Convierto una cadena (string) que representa un número binario (base 2)
        en un número decimal (base 10) '''    

    # Inicializo una variable que va sumando los cálculos que realizo para
    #cada dígito de la cadena_binaria
    suma = 0

    # Para facilitar los cálculos invierto el orden de la cadena_binaria
    cadenaInversa = cadena_binaria[::-1]
    
    # Multiplico cada dígito de la cadenaInversa por el número 2 elevado
    # a la potencia que me indica su posición en dicha cadena. Sumo todo 
    # en una variable que va a ir formando el número decimal
    for x in range(len(cadenaInversa)):
        suma += int(cadenaInversa[x]) * (2 ** x)
    
    return suma


def textoPlano_a_Base64(texto_plano):
    ''' Retorno un texto convertido a base64 '''

    cadena = ""
    for caracter in texto_plano:
        
        # De cada caracter del texto obtengo su representación decimal ASCII
        # y lo convierto en una cadena binaria
        caracter_bin = decimal_a_binario(ord(caracter))

        # Completo con tantos "0" a la izquierda si la longitud es menor a 8
        caracter_bin = "0" * (8 - len(caracter_bin)) + caracter_bin        

        # Voy formando una cadena binaria larga 
        cadena += caracter_bin
    
    # Tengo que formar grupos de 6 caracteres para poder convertir a base64,
    # así que completo con ceros a la derecha de la cadena para que me dé
    # un múltiplo de 6
    aux = len(cadena) % 6
    if aux > 0:
        cadena += "0" * (6 - aux)

    texto_base64 = ""
    for x in range(0,len(cadena),6):    

        # Cada subcadena de 6 caracteres binarios la convierto a número
        # decimal, luego uso el resultado como índice en una lista para
        # obtener el caracter en base64, el cual concateno en una nueva 
        # cadena para ir formando el texto convertido
        texto_base64 += CARACTERES_BASE64[binario_a_decimal(cadena[x:x+6])]
    
    return texto_base64


def base64_a_TextoPlano(texto_base64):
    ''' Retorno un texto en texto plano a partir de un texto en base64 '''

    # Creo un diccionario auxiliar que asocia cada caracter válido en base64
    # a un número dado de 0 a 63
    diccio_aux = dict(zip(CARACTERES_BASE64, range(len(CARACTERES_BASE64))))
        
    cadena = ""
    for caracter in texto_base64:

        # De cada caracter del texto obtengo su representación decimal usando
        # el diccionario de caracteres y convierto eso a una cadena binaria
        caracter_base64 = decimal_a_binario(diccio_aux[caracter])
        
        # Completo con tantos "0" a la izquierda si la longitud es menor a 6
        caracter_base64 = "0" * (6 - len(caracter_base64)) + caracter_base64        

        # Voy formando una cadena binaria larga 
        cadena += caracter_base64

    # Tengo que formar grupos de 8 caracteres para poder convertir de nuevo
    # a decimal el texto codificado, así que elimino los ceros al final 
    # para que me dé un múltiplo de 8
    aux = len(cadena) % 8
    if aux > 0:        
        cadena = cadena[:len(cadena)- aux]

    texto_plano = ""
    for x in range(0,len(cadena),8):

        # Cada subcadena de 8 caracteres binarios la convierto a número
        # decimal, luego uso la función chr para volver a obtener el caracter
        # real de texto plano, el cual concateno en una nueva cadena para
        # ir formando el texto convertido
        texto_plano += chr(binario_a_decimal(cadena[x:x+8]))
    
    return texto_plano


def modo_interactivo():
    ''' Codifico/decodifico en base64 a partir de un menú de opciones 
        y luego muestro el resultado en pantalla '''
            
    while True:
        
        # Muestro un menú de opciones
        print()
        print(colorBorde + "=" * 50)
        print(colorDescripcion + " Codificar/Decodificar texto con Base64")
        print(colorBorde + "=" * 50)
        print(colorDescripcion + "\n  1. Texto plano --> Base64")
        print("  2. Base64 --> Texto plano")        
        print("  0. Salir")
        print(colorDescripcion + "\nIngrese una opción:" + colorResultado,
            end = " ")
        ingreso_opcion = input("").strip()

        if ingreso_opcion == "0":
            break

        if ingreso_opcion in ["1", "2"]:
            print(colorDescripcion + "Ingrese texto a convertir:" + 
                colorResultado, end = " ")
            ingreso_texto = input("").strip()
        
            # Verifico que se haya ingresado algún texto para convertir
            if len(ingreso_texto) == 0:
                continue        
            
            if ingreso_opcion == "1":
                print(colorDescripcion + 
                    "Resultado de la conversión a base64:", end = " ")
                print(colorResultado + 
                    textoPlano_a_Base64(ingreso_texto))
                print()
            elif ingreso_opcion == "2":
                print(colorDescripcion + 
                    "Resultado de la conversión a texto plano:", end = " ")
                print(colorResultado + base64_a_TextoPlano(ingreso_texto))
                print()


def modo_argumentos():
    ''' Codifico/decodifico en base64 a partir de los argumentos ingresados
        y luego muestro el resultado en pantalla '''

    parser = argparse.ArgumentParser(description='Codificador Base64')
    parser.add_argument('cadena', help="texto a convertir")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-base64', action="store_true", help="convertir a base64")
    group.add_argument('-texto', action="store_true", 
        help="convertir a texto plano")
    
    try:
        args = parser.parse_args()        
    except: 
        print("\nError de argumentos.")
        sys.exit(0)
    
    # De acuerdo al parámetro ingresado convierto a texto plano o a base64
    if args.texto:
        print(colorDescripcion + "Resultado de la conversión a texto plano:",
         end = " ")
        print(colorResultado + base64_a_TextoPlano(args.cadena))   
    elif args.base64:
        print(colorDescripcion + "Resultado de la conversión a base64:",
         end = " ")
        print(colorResultado + textoPlano_a_Base64(args.cadena))
    else:
        # Por defecto si no se ingresa tipo de conversión se convierte a base64
        print(colorDescripcion + "No ha ingresado tipo de conversión. " +
            "Por defecto se convierte a base64.")
        print(colorDescripcion + "Resultado de la conversión a base64:",
         end = " ")
        print(colorResultado + textoPlano_a_Base64(args.cadena))

# ---------------------------------------------------------------------------

if __name__ == "__main__":

    # Inicializo la librería colorama y asigno a distintas variables estilos
    # de colores de texto para usar luego al mostrar en pantalla
    init()
    colorBorde = Style.DIM + Fore.BLUE 
    colorDescripcion = Style.DIM + Fore.CYAN
    colorResultado = Style.BRIGHT + Fore.CYAN
    
    # Verifico si se ingreso algún argumento. De no ser así, se entra en
    # modo interactivo (con menú de opciones)
    if len(sys.argv[1:]):            
        modo_argumentos()
    else:   
        modo_interactivo()