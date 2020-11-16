"""Usuario: ECOTRACKER (en Telegram)
   Detalle de lo que hace el programa:
   Se escribe un codigo que puede
   convertir de texto a base64 y de 
   base64 a texto."""

#LIBRERIAS A IMPORTAR
from colorama import Fore, init #Importo colorama para darle color al texto
import sys #Importo la libreria sys para poder usar argumentos
import os #Importo os para intteractuar con el sistema operativo
import base64 #Importo base64 para convertir.

init() #Inicio init para poder usarla en el codigo

if __name__ == '__main__': #Defino if que se ejecutara si el nombre corresponde
	if len(sys.argv)==1: #Evaluo si la longitud de sys.argv es igual a 1 para saber si tengo entrada de argumento.
		print(Fore.GREEN+"\nEs necesario colocar por lo menos un argumento") #Imprimo mensaje indicando que no ingresaron argumentos
	else: #Si no se cumple sys.argv==1 entonces paso al siguiente nivel
		if sys.argv[1]=='help': #Si en sys.argv[1] contiene help entro a los mensajes de ayuda.
			print(Fore.BLUE+"\nHas entrado al menu de ayuda")
			print("\n  Tienes 2 opciones para pasar parametros:")
			print(Fore.YELLOW+"    1) Ejecutas el scripts junto con -texto, luego cuando te lo indique ingresas la cadena de base64 ")
			print(Fore.GREEN+"    2) Ejecutas el scripts junto con -base64, luego cuando te lo indique ingresas la cadena de texto")
		if sys.argv[1]=='-texto': # Si el argumento 1 es igual a -texto quiere decir que se va a convertir de base64 a texto
			print("\nVamos a convertir de base64 a texto") # Le indico al usuario lo que se va a realizar
			texto=input("\nIngrese el string base64:") # Pido al usuario ingrese el string base64 a convertir
			texto2=texto.encode("ascii") # Convierto la variable texto en codigo ascii
			texto_bytes=base64.b64decode(texto2) # Convierto la variable texto2 a bytes
			texto_string=texto_bytes.decode("ascii") # Covierto la vartiabla texto_bytes en ascii
			print("\nEl texto es:",texto_string) # Imprimo el resultado de la conversion
		if sys.argv[1]=='-base64': # Si el argumento 1 es igual a -base64 quiere decir que se va a convertir de texto a base64
			print("\nVamos a convertir de texto a base64")  # Le indico al usuario lo que se va a realizar
			ba64=input("\nIngrese el texto a convertir:") # Pido al usuario ingrese el string texto a convertir
			ba64_string_bytes=ba64.encode("ascii") # Convierto la varible ba64 a ascii
			ba64_byte=base64.b64encode(ba64_string_bytes) # Convierto la variable ba64_string_byte en base64
			ba64_string=ba64_byte.decode("ascii") # Convierto la variable ba64_byte en ascii
			print("\nEl string base64 es:",ba64_string)	# Imprimo el resultado de la conversion.
