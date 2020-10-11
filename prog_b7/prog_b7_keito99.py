#!/usr/local/bin/pyton

## Programa para calcular la clase a la que pertenece una IPv4 dada.
## Mostrará la cantidad de hosts permitidos en la red
## Es necesario importar la libreria ipaddress

import ipaddress

## Funcion para calcular de forma "dirty" la mascara que corresponde 
## a las redes privadas
def calcular_mascara(direccion):
	clase=direccion.split('.',3)
	ipstart=int(clase[0])
	if ((ipstart >= 0) and (ipstart <= 10)):
		return "8"
	elif (ipstart == 172):
		return "12"
	elif (ipstart == 192):
		return "24"

def calcular_clase(net):
	if (net == "8"):
		return "A"
	elif (net == "12"):
		return "B"
	elif (net == "24"):
		return "C"

direccion=input("introduce una IPv4:")
addrv4=ipaddress.ip_address(direccion)
if ( addrv4.version == 4):
	if (addrv4.is_private):
		net=direccion + "/" + calcular_mascara(direccion)
		network=calcular_mascara(direccion)
		addrv4=ipaddress.ip_network(net,strict=False)
		clase_net=calcular_clase(network)
		print ("IP: ",direccion,"pertenece a una red privada.")
		print ("La clase:",clase_net, "puede tener,",(addrv4.num_addresses - 2), "direcciones posibles:")
	
	else:
		print ("IP: ",direccion,"pertenece a una red pública")

else:
	print ("es una IPv6. Este Programa no hace calculos sobre ipv6")
