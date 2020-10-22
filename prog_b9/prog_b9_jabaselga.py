#!/usr/bin/python3

""" 
Detalles:

Un escáner de puertos a una ip

Requerimientos:

Crea un programa que escanee los puertos de una ip, deben haber 3 tipos de escaneo:

1.Escaneo rápido: Escaneara los puertos mas comunes según tu criterio o puedes escogerlos de esta web que te muestra los mas utilizados: Link

2.Escaneo personalizado: El usuario debe ingresar cuales puertos quiere escanear, ya sea por rango (10-20) o individual (10) o separados por coma (80, 443, 445).

3.Escaneo completo: El programa escaneara todos los puertos.

Luego el programa imprimirá en pantalla solo los puertos que esten abiertos.

El programa se puede ejecutar de dos formas:

1.Modo interactivo: El programa le pide al usuario que ingrese los datos mediante inputs

2.Argumentos: al ejecutar el programa, mediante las opciones que ingrese el usuario tomara esos datos para determinar el tipo de escaneo 
y demás datos (ej: python -p 80 -i 10.10.10.1 -escaneoB) (NOTA: estas opciones son de ejemplo)

Programas completados:


code: progb_9_tuuser.py
@aprenderpython
redes

"""
import socket
import sys
import argparse
import ipaddress
import re
from datetime import datetime 

def check_ip(string):
    try:
        ipaddress.IPv4Address(string)
    except:
        msg = f'{string} no es una IP.'
        raise argparse.ArgumentTypeError(msg)
    
    return string

def check_ports(string):
    pattern=re.compile(r'(((([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))-(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))),|(\d{1,5}),)*((\d{1,5}-\d{1,5})|(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))\Z)+')
    port_re=pattern.fullmatch(string)
    
    if port_re:
        lp=eval_port(port_re.string)
        if lp:
            return port_re.string
        else:
            msg = f'{string} error al escribir los puertos.'
            raise argparse.ArgumentTypeError(msg)

    else:
        msg = f'{string} error al escribir los puertos.'
        raise argparse.ArgumentTypeError(msg)

def check_ports_manual(string):
    pattern=re.compile(r'(((([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))-(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))),|(\d{1,5}),)*((\d{1,5}-\d{1,5})|(([0-9]?[0-9]?[0-9]?[0-9]?)|([0-5][0-9][0-9][0-9][0-9])|([0-6][0-4][0-9][0-9][0-9])|([0-6][0-5][0-4][0-9][0-9])|([0-6][0-5][0-5][0-2][0-9])|([0-6][0-5][0-5][0-3][0-5]))\Z)+')
    port_re=pattern.fullmatch(string)
    
    if port_re:
        lp=eval_port(port_re.string)
        if lp:
            return sorted(list(set(eval_port(port_re.string))))
    
    return False


def eval_port(ports_s):
    ports=list(ports_s.split(','))

    lp=[]
    for p in ports:
        if p.isdigit():
            lp.append(int(p))
        else:
            a, b = map(int, p.split('-'))
      
            if a>b:
                return False
            else:
                for j in range(a,b+1):
                    lp.append(int(j))
    return lp

if __name__ == "__main__":
    print ("________________________________________________________________________________")
    print ('Ejercicio b9. Escaner de puertos.')
    print ('@jabaselga')
    print ("________________________________________________________________________________")

    parser = argparse.ArgumentParser(description='Port scanner', epilog='@jabaselga')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--ports", nargs='?', help="Ports to scan",type=check_ports)
    group.add_argument("-f", "--full", help="Scan all port range (0-65535)", action='store_true')
    group.add_argument("-l", "--large", help="Scan big port range (0-10000)", action='store_true')
    group.add_argument("-q", "--quit", help="Scan more interesting ports (22, 80, 443, ...)", action='store_true')
    parser.add_argument("-i", "--ip", metavar='A.B.C.D', help="IP to port scan", type=check_ip)
    parser.add_argument("-v", "--verbose", help="Show extra information", action='store_true')
    args = parser.parse_args()

    parser.print_usage()

    if args.verbose:
        print (f'Ports: {args.ports}')
        print (f'Full scan: {args.full}')
        print (f'Large scan: {args.large}')
        print (f'Quick scan: {args.quit}')
        print (f'IP: {args.ip}')

    ip=''
    if not args.ip:
        nok=True
        while nok:
            ip=input('Input IP to scan: ')
            try:
                ipaddress.IPv4Address(ip)
                nok = False
            except:
                print ('IP wrong. Try again.')
    else:
        ip=args.ip
    
    ports=[]
    
    if args.quit:
        ports = [20, 21, 22, 23, 25, 37, 42, 49, 53, 80, 110, 123, 137, 138, 139, 143, 443, 587, 993, 995, 1080, 1194, 1433, 2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078, 3306, 5800, 5900, 8080]
    elif args.full:
        if args.verbose:
            print ('Warning: it takes several mimutes ...')
        ports=list(range(65535))
    elif args.large:
        if args.verbose:
            print ('Warning: it takes several mimutes ...')
        ports=list(range(10000))
    else:
        if not args.ports:
            nok=True
            while not ports:
                ports=input('Input ports to scan: ')
                if ports !='':
                    ports = check_ports_manual(ports)
                    if not ports:
                        print ('Ports wrong. Format -> [x,x-y,...].  Try again.')
        else:
            ports = sorted(list(set(eval_port(args.ports))))
        
    if args.verbose:
        print (f'Port to scan: {ports}')

    print("-" * 50) 
    print("Scanning Target: " + ip) 
    print("Scanning started at:" + str(datetime.now())) 
    print("-" * 50) 

    try: 
        for port in ports:
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            socket.setdefaulttimeout(0.05) 
            
            # returns an error indicator 
            result = s.connect_ex((ip,port)) 
            if result==0:
                try:
                    service='/'+socket.getservbyport(port)
                except:
                    service=""

                print(f"Port {port}{service} is OPEN") 
            s.close() 
            
    except KeyboardInterrupt: 
            print("\n Exitting Program !!!!") 
            sys.exit() 
    except: 
            print("\n Fail.. !!!!") 
            sys.exit() 

    print(f"Scanning of {len(ports)} ports finished at:" + str(datetime.now()))