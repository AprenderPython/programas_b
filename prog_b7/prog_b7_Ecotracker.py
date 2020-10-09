
"""Usuario: ECOTRACKER (en Telegram)
   Detalle de lo que hace el program:
   	Se escribe un codigo que puede saber a
   	que clase de IP pertenece una IP
   	que introduzca un usuario por teclado
   	de ingresar un texto le indica que no
   	es un una IP lo ingresado y termian
   	de correr el programa"""

import ipaddress #Importo ipaddress
from ipaddress import IPv4Address, IPv4Network #Importo de ipaddress IPv4 (address y network)

#Creo variables on el uso de IPv4Network donde definos las 3 clases de IP que voy testear.
classA = IPv4Network(("10.0.0.0", "255.0.0.0"))  # or IPv4Network("10.0.0.0/8")
classB = IPv4Network(("172.16.0.0", "255.240.0.0"))  # or IPv4Network("172.16.0.0/12")
classC = IPv4Network(("192.168.0.0", "255.255.0.0"))  # or IPv4Network("192.168.0.0/16")

entrada = input("por favor igresa una IP ==>") #Defino una varible y pido ingreso por teclado
result = "puedes estar ingresando una IP reservada o de host local, por favor reinicia el progrma y coloca una IP valida" #Defino una variable con un mensaje predeterminado.

try: #Con Try filtro que si es texto muestre un mensaje que diga que no he introducido una ip
	ip = IPv4Address(entrada) #Variable IP que va a testear la información introducidad de la variable entrada para sensar si es validad o no.
	ip = ipaddress.ip_address(entrada)
	"""#Defino IF para revisar las 3 posibles opciones de clase de ip que voy analizar. si no se cuumple ningunas de las tres
	 	imprimo el en mensaje inicializado en con result"""

	if ip in classA :
  		result = "la ip:",entrada ," es Clase A y puede tener: 16.777.214 HOST"
	elif ip in classB : 
		result = "la ip:",entrada ,"  es Clase B y puede tener: 65.534 HOST"
	elif ip in classC : 
		result = "la ip:",entrada ,"  es Clase C y puede tener: 254 HOST"
	print (result)
except:
	print("No has escrito una IP")
