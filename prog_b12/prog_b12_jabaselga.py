""" 
Detalles Programa semanal:

Crea un programa que mediante argumentos (ej; python archivo.py argumento) pueda convertir de texto a base64 y viceversa.

Requerimientos:

°Determinar si es texto plano o base64 para luego imprimir la conversion, puede ser mediante argumentos, ej: -texto o -base64, (o como gusten)
°Imprimir el resultado de la conversion.

Programas completados::white_check_mark:
°Ecotracker: Ver programa
°Raul: Ver programa  

Programa alternativo:

Crea un programa que te pregunte tu nombre y luego te lo imprima alrevez, ej: carlos > solrac

code: progb_12_tuuser.py
@aprenderpython
#criptografia


v0.1 funciones básicas implementadas

"""

import string
import re
import argparse
from colorama import Fore, init


# genero la cadena a usar para codificar
chars64 = string.ascii_uppercase+string.ascii_lowercase+string.digits+'+/'
# creo un diccionario para las búsquedas inversas
dict_chars64 = {i:j for j,i in enumerate(chars64)}


def ascii_to_binary(cadena):
    """ 
        Devuelve una lista de string de la conversión en binario de la cadena
        ajustdo con ceros por la izquierda si tiene menos de longitud 8
    """
    # genero una lista te todos los char en binario
    cadena_bin = [bin(ord(i))[2:] for i in cadena]
    # aquellos que tienen menos de 8 digitos, los relleno con "0" por la izquierda
    for i in range(len(cadena_bin)):
        cadena_bin[i]='0'*(8-len(cadena_bin[i]))+cadena_bin[i]

    cadena_sum =""
    #uno todos los elementos de la lista en una cadena
    for s in cadena_bin:
        cadena_sum+=s
    
    return cadena_sum

def binary_to_bin64(cadena_bin):
    """ 
        Reorganizar la cadena binaria pasando de grupos de 8 a grupos de 6
    """
    # Trocear la cadena en grupos de 6
    lb=re.findall(".{1,6}", cadena_bin)
    # Si el último grupo no tiene 6 digitos se rellena con "0" por la derecha
    lb[-1]=lb[-1]+"0"*(6-len(lb[-1]))

    return lb

def calculate_fill(cadena):
    """ 
        Si la cadena no es multiplo de 3 se rellena con "="
        Devuelve la cantidad de "=" que se necesitan para completar la codificación
    """
    return  (3-len(cadena)%3)%3

def bin64_to_base64(cadena, cadena_bin):
    """ 
        Convierte la cadena bin64 a la codificacion base64. 
        Añade los correspondientes "=" si la cadena no es multiplo de 3 bytes
    """
    cadena_base64=""
    # saco de la lista todos los caracteres correspondientes y los concateno
    for i in cadena_bin:
        cadena_base64+=chars64[int(i, 2)]
        
    # añado los "=" necesarios al final de la cadena
    cadena_base64+= ('='*calculate_fill(cadena))

    return cadena_base64


def cadena64_to_dig64(cadena64):
    """ 
        convierte la cadena a su valor decimal correspondiente.
        elimina los "=" del final.
    """
    ld=[]
    # genero una lista con los valores en decimal sacandolos con un dicionario inverso
    # elimino los "=" del final
    for i in cadena64:
        if i != '=':
            ld.append(dict_chars64[i])
    
    return ld

def dig64_to_bin(dig):
    """
        Convierto la cadena decimal a binario en bloques de 8 digitos 
    """
    # primero convierto los números en binarios de 6 bits,
    cadena_bin= [bin(i)[2:] for i in dig]
    for i in range(len(cadena_bin)):
        cadena_bin[i]='0'*(6-len(cadena_bin[i]))+cadena_bin[i]

    # los uno para formar una sola cadena
    cadenasum=""
    for i in cadena_bin:
        cadenasum+=i

    # lo troceo en grupos de 8
    la=re.findall(".{1,8}", cadenasum)

    # si el último grupo no tiene 8 de longitud lo elimino
    if len(la[-1])<8:
        la.pop()

    return la

def bin_to_ascii(la):
    """ 
        Convierte una lista de binarios a una cadena ascci
    """
    cad=""
    for i in la:
        cad+=chr(int(i,2))

    return cad


def string_to_base64(cadena):
    """
        Convierte una cadena a base64
    """
    binary = ascii_to_binary (cadena)
    bin64 = binary_to_bin64 (binary)
    base64 = bin64_to_base64 (cadena, bin64)

    return base64

def base64_to_string(base64):
    """ 
        Decodifica una secuencia en base64 a cadena
    """
    dig64 = cadena64_to_dig64(base64)
    bin8 = dig64_to_bin(dig64)
    cadena=bin_to_ascii(bin8)

    return cadena


def string_reverse(cadena):
    """ 
        Devuelve la cadena inversa
    """
    reverse=""
    for i in range(len(cadena)-1, -1, -1):
        reverse+=cadena[i]

    #return cadena[::-1]
    return reverse

if __name__ == "__main__":
    parser = argparse.ArgumentParser (description="Code/Decode base64 and reverse string", epilog="@jabaselga")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encode", metavar="string", help="String to encode.")
    group.add_argument("-d", "--decode", metavar="string", help="String to decode.")
    group.add_argument("-r", "--reverse", metavar="string", help="String to reverse.")
    parser.add_argument("-v", "--verbose", help="Extra info", action="store_true")
    
    args = parser.parse_args()   

    argsn = args.encode or args.decode or args.reverse
    if not argsn:
        parser.error('No arguments to ejecute provided.')

    # colorama inicialización
    init ()

    if args.verbose:
        print (f"{Fore.BLUE}________________________________________________________________________________")
        print ('Ejercicio b12. Codificación/Decodificación e inversión de cadenas.')
        print ('@jabaselga')
        print (f"________________________________________________________________________________{Fore.RESET}")

    if args.encode:
        base64 = string_to_base64(args.encode)
        if args.verbose:
            print(f"La cadena {Fore.GREEN}{args.encode}{Fore.RESET} codificada en base64 es:")
        print (base64)
    if args.decode:
        cadena = base64_to_string(args.decode)
        if args.verbose:
            print(f"La cadena {Fore.GREEN}{args.decode}{Fore.RESET} descodificada en ASCII es:")
        print (cadena)

    # extra: programa alternativo
    if args.reverse:
        if args.verbose:
            print(f"La cadena {Fore.GREEN}{args.reverse}{Fore.RESET} invertida es:")
        cr = string_reverse(args.reverse)
        print (cr)