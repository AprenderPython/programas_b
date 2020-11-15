import os
import pyfiglet
import sys
os.system("clear")

Banner = pyfiglet.figlet_format("Bienvenido!")

#Solicitamos la ruta

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(Banner)
        print("Por favor escriba la ruta del archivo como argumento")
#Explicación de __name__
#__name__ es por asi decirlo una variable ""invisible"" que viene por defecto en python
#Esta variable tiene como valor el string '__main__'
#Para que lo entiendas mejor puedes imprimir por pantalla lo siguiente
# print("__name__ in test2.py is set to " + __name__)

Ruta = sys.argv[1] 

os.system("clear")

#Abrimos el archivo
Archivo = open(Ruta, "r")

#Extras

from pyfiglet import Figlet
Custom_figlet = Figlet(font="shadow")
banner2 = Custom_figlet.renderText("Vuelva  pronto!..") #linea 18-20 banner
path, nombre = os.path.split(Ruta) #Nombre
Tamaño = os.path.getsize(Ruta) #Peso

import datetime
def modificación(Ruta): 
    M = os.path.getmtime(Ruta)
    return datetime.datetime.fromtimestamp(M)
Fecha_M = modificación(Ruta)
#Con eso consegui la fecha de modificación

#Con len  sacamos el numero de lineas del archivo
Lineas = len(Archivo.readlines())

#Resultado
print(banner2)
print()
print("Archivo: ", nombre)
print("Lineas de texto: ", Lineas)
print("Tamaño del archivo: ", Tamaño, "bytes")
print("Fecha de modificación: ", Fecha_M)

#Cerramos el archivo
Archivo.close()

#Este proyecto fue escrito por not_found!
#Muchas gracias por tomar tu tiempo de leer/usar
#Si tienes alguna duda, no dudes en hablarme ^^
#Y recuerda no te rindas!! 
#Si puedes imaginarlo puedes programarlo ;)