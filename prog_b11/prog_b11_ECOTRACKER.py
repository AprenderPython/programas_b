"""Usuario: ECOTRACKER (en Telegram)
   Detalle de lo que hace el program:
   Se escribe un codigo que puede contar
   las cantidas de lineas que existe
   en un archivo txt, con uso de
   argumentos para hacer mas rapida
   las ejecución del programa."""

#LIBRERIAS A IMPORTAR
from colorama import Fore, init #Importo colorama para darle color al texto
import sys #Importo la libreria sys para poder usar argumentos
import os #Importo os para intteractuar con el sistema operativo


init() #Inicio init para poder usarla en el codigo

if __name__ == '__main__': #Defino if que se ejecutara si el nombre corresponde
	if len(sys.argv)==1: #Evaluo si la longitud de sys.argv es igual a 1 para saber si tengo entrada de argumento.
		print(Fore.GREEN+"\nEs necesario colocar por lo menos un argumento") #Imprimo mensaje indicando que no ingresaron argumentos
	else: #Si no se cumple sys.argv==1 entonces paso al siguiente nivel
		if sys.argv[1]=='help': #Si en sys.argv[1] contiene help entro a los mensajes de ayuda.
			print(Fore.BLUE+"\nHas entrado al menu de ayuda")
			print("\n  Tienes 2 opciones para pasar parametros:")
			print(Fore.YELLOW+"    1) Te para en la ruta donde quieres contar las lineas del archivo y escribes: python nombre_scripts.py nombre del archivo.txt")
			print(Fore.GREEN+"    2) Escribes: python nombre_scripts.py \"c:\\Users\\nombre_usuario\\Desktop\\nombre_de_carpeta\"\\nombre_del_archivo.txt")
		else: #Si no se cumplio lo anterior entonces entro en un try para ver si existe el fichero
			try:
				fichero = open(sys.argv[1], 'r') # Abro el archivo con permiso de lectura
				fichero.readline() # indicoa que la variable fichero se van a leer las lineas
				fichero.seek(0) # Inicio la lectura desde la linea 0
				#print(Fore.MAGENTA+"\nLa información fue buscada en:",sys.argv[1])
				a=os.path.split(sys.argv[1]) #Hago una variable que divide por / o \ para separar la ruta del nombre del archivo
				print("\n==========================RESULTADO==================================") # Para dar estetica
				print(Fore.MAGENTA+"\nEl nombre del archivo es:",a[1])
				print (Fore.MAGENTA+"La cantidad de lineas son:",len(fichero.readlines())) # Imprimo el resultado de la lectura del archivo
				fichero.close() # Cierro el fichero
				print(Fore.WHITE+"\n======================================================================") # Para dar estetica
			except: # Si el fichero o archivo no existe envio un mensaje de error al usuario.
				print(Fore.RED+"\nEl archivo o ruta:","\""+sys.argv[1]+"\"","No existe o lo escribiste mal")