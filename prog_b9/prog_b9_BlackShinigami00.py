import sys
import socket
import os
from datetime import datetime
import time
import argparse

# Intancia de la argparse permite el paso de parametros en consola

arg = argparse.ArgumentParser()
arg.add_argument("-i", "--ip", help= "Define la direccion IP que vas a usar")
arg.add_argument("-s", "--startPort", help= "Define el puerto donde comenzara el escanner <por defecto es 1>")
arg.add_argument("-f", "--finalPort", help= "Define el puerto donde terminara el scanner <por defecto es 65535>")
arg.add_argument("-q", "--quick", help= "Realiza un escaneo solo a los puertos principales",  action="store_true")
arg.add_argument("-c", "--custom", help= "Activa la opcion de puertos personalizados(-p)", action="store_true")
arg.add_argument("-p", "--customPorts", help= "Realiza un escaneo solo a los puertos que indiques")
args = arg.parse_args()

openPorts = [] # Guardara los puertos abiertos  
Pcomunes = (20,21,22,23,25,53,67,80,81,82,123,143,156,443) # Puertos comunes
specificsPorts = [] 

def portSc(ip,Port): # Intenta establecer comunicacion con la IP designada por el puerto que se este iterando para determinar si esta abierto o no
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = client.connect_ex((ip,Port))
    if result == 0:
        return True
        client.close()

def quickScan(ip): # Realiza el escaneo rapido iterando sobre los puertos comunes

    for port in Pcomunes:
        print(f"Escaneando Puerto >>> {port}")
        result = portSc(ip,port)
        if result == True:
            openPorts.append(port)

    if len(openPorts) == 0:
        os.system("cls")
        print("No se encontraron puertos abiertos")
    else:
        os.system("cls")
        print("Se encontraron estos puertos abiertos")
    for i in openPorts:
        print(f"Puerto {i} >>> Abierto")
    sys.exit()

def customScan(ip):
    if args.custom:
        portList = args.customPorts
        listDiv = portList.split(',')
        print(listDiv)
    else:
        print("Introduce los numero de puerto que deseas escanear separados por comas")
        portList = input(">>> ")
        listDiv = portList.split(',')
        
    for port in listDiv:
        print(f"Escaneando Puerto >>> {port}")
        result = portSc(ip,int(port))
        if result == True:
            openPorts.append(port)

    if len(openPorts) == 0:
        os.system("cls")
        print("No se encontraron puertos abiertos")
    else:
        os.system("cls")
        print("Se encontraron estos puertos abiertos")
    for i in openPorts:
        print(f"Puerto {i} >>> Abierto")
    sys.exit()


def normalScan(ip,puerto1,puerto2): # Realiza el escaneo normal en conjunto con la funcion portSc()
    for port in range(port1,port2+1):
        print(f"Escaneando Puerto >>> {port}")
        result = portSc(ip,port)
        if result == True:
            openPorts.append(port)

    if len(openPorts) == 0:
        #os.system("cls")
        print("No se encontraron puertos abiertos")
    else:
        os.system("cls")
        print("Se encontraron estos puertos abiertos")
        for i in openPorts:
            print(f"Puerto {i} >>> Abierto")

if args.custom:
    ip = args.ip
    customScan(ip)
    sys.exit()

if args.ip: # Recive los paramatros que se pasan por consola para un escaneo normal
    ip = args.ip
    if args.startPort:
        port1 = args.startPort
        port1 = int(port1)
    elif args.startPort != True and args.quick != True:
        port1 = 1
    
    if args.finalPort:
        port2 = args.finalPort 
        port2 = int(port2)
        normalScan(ip,port1,port2)
        sys.exit()
    elif args.finalPort != True and args.quick != True:
        port2 = 65535
        normalScan(ip,port1,port2)
        sys.exit()

if args.quick: # Escaneo rapido pasando parametros por consola
    ip = args.ip
    quickScan(ip)
    sys.exit()



else: # Ejecuta una interfaz si no se pasan parametros en la consola 
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("<>--------------------------------------------------------------------------------------<>")
    print("<>----------(Escanner de Puertos)-------------------------------------------------------<>")
    print("<>--------------(Escrito en Python 3)---------------------------------------------------<>")
    print("<>------------------------(Por)---------------------------------------------------------<>")
    print("<>-----------------(Black SHinigami)----------------------------------------------------<>")
    print("<>----------------------[Telegram: BlackShinigami00]------------------------------------<>")
    print("<>--------------------------------------------------------------------------------------<>")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

    while True:
        try:
            modoS = int(input("Como quieres realizar el escaneo de puertos\n1-Completo (No Recomendado)\n2-Rapido\n3-Manual\n4-Puertos Especificos\n>>> "))
        except ValueError:
            print("Error no ingresaste un numero")
            sys.exit()

        if modoS >=1 and modoS <= 4:
            break
        else:
            print("[!] Esa opcion no existe vuelve a intentar")

    if modoS == 1:
        print("\n[!]Este tipo de escaneo de puertos va a tardar varios minutos")
        print("[!]Por favor tenga en cuenta que se escanearan 65535 puertos")
        print("[!]Espere pacientemente\n")

        ip = input("Ingresa la direccion IP a la que deseas escanear puertos\n>>> ")
        os.system("cls")
        port1 = 1
        port2 = 65535
        normalScan(ip,port1,port2)

    elif modoS == 2:
        ip = input("Ingresa la direccion IP a la que deseas escanear puertos\n>>> ")
        os.system("cls")
        quickScan(ip)
    
    elif modoS == 3:
        ip = input("Ingresa la direccion IP a la que deseas escanear puertos\n>>> ")

        port1 = int(input("Introduce el numero de puerto donde comenzara el escanner\n>>> "))
    
        port2 = int(input("Introduce el numero de puerto donde finalizara el escanner\n>>> "))
        os.system("cls")
        normalScan(ip,port1,port2)

    elif modoS == 4:
        ip = input("Ingresa la direccion IP a la que deseas escanear puertos\n>>> ")
        os.system("cls")
        customScan(ip)
    
    