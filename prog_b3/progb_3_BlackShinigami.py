import os
import sys
import platform
from datetime import datetime

#Create by: @BlackShinigami00

ip_Act = [] #para almacenar las ips activas

print(
    "======================================================================================================================\n"
    "= Escaner para buscar IPs activas en la red local                                                                    =\n"
    "= Escrito en Python 3                                                                                                =\n"
    "= Por 'BlackShinigami'                                                                                               =\n"
    "=                                                                                                                    =\n"
    "=                                                                                                                    =\n"
    "=                                                                                                                    =\n"
    "======================================================================================================================") #mensaje de vienvenida
#==================recogida del broadcast
ip = input("Ingresa la ip >>> ")

if len(ip) > 15:
    print("Direccion IP no valida\ndireccion ip demaciado larga")
    sys.exit()

if ip.count('.') != 3:
    print("Direccion IP no valida\nLa cantidad de puntos existentes '.' no son validos")
    sys.exit()

ipDiv = ip.split('.')

for i in ipDiv:
    try:
        if int(i) <= 255:
            pass
        else:
            print("Direccion IP no valida\nLas Ips van des 0 hasta 255 en cuatro octetos")
            sys.exit()
    except ValueError:
        print("La direccion IP no valida\nLa direccion no puede contener caracteres")
        sys.exit()

print("Se escaneara la red en el rango de esta IP >>> ", ip)

#======================Verificacion del sistema operativo

if (platform.system() == "Windows"):
    ping = "ping -n 1"
else:
    ping = "ping -c 1"

#=====================Divicion de la ip

red = ipDiv[0] + "." + ipDiv[1] + "." + ipDiv[2] + "."

redST = int(input("Ingresa el primer valor donde quieres que comience el escaneo >>> "))

if int(redST) > 255 or int(redST) < 0:
    print("Solo se admiten valores desde 0 a 255")
    sys.exit()

redEnd = int(input("Ingresa el ultimo valor donde quieres que finalice el escaneo >>> "))

if int(redEnd) > 255 or int(redST) < 0:
    print("Solo se admiten valores desde 0 a 255")
    sys.exit()

print("Esta operacion puede tomar varios minutos dependiendo de la cantidad de IP que tenga que analizar")
print("El escaneo ha comenzado...")
print("Por favor no cierres la consola")

timeStart = datetime.now()

for ip in range(redST, redEnd + 1):
    ip_comp = red + str(ip)
    print("Escaneando la IP >>> ",ip_comp)
    response = os.popen(ping + " " + ip_comp)
    for line in response.readlines():
        if ("ttl" in line.lower()):
            ip_Act.append(ip_comp)
            break

timeEnd = datetime.now()
Total = timeEnd - timeStart
print("Proceso finalizado con exito en %s" % Total)
print("===========================================")
for ip in ip_Act:
    print(ip, "==> Se encuentra activo")