import ipaddress
import socket
import os
import sys

ip = ()
mask = ()
ayu = ()
ipscan = []

#Si el sistema en el cual se ejecuta no es windows se termina el script
if os.name != "nt":
    print (input("Lo siento, solo funciono en  sistemas windows... "))
    sys.exit()

#Menu de bienvenida
print ("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                             █
█       Scanner-Host-IP       █
█             v2.0            █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
\nEste programa se basa en el protocolo icmp para descubrir host 
conectados en la red especificada usando ping. 
\nAutor: StaryDark(@dark_zly)    Siguenos en Telegram:@aprenderpython
\nSeleccione una de las siguienes opciones para empezar:\n\n
1-> Escriba la ip o red manualmente
2-> Detectar las ip de sus targetas de red\n""")

while True:
    tipo = input("Selecciones una de las opciones: ")
    if tipo == "1" or tipo == "2":
        break

#ip automatica
if tipo == "2":
    ipslocal = socket.gethostbyname_ex(socket.gethostname()) #obtener info de red
    ipslocal = (ipslocal[2]) #seleccionar las ips de las interfaces de red locales
    cont = len(ipslocal)
    ayu = 0
    #determinar si hay mas de una ip, si es solo una se guarda en la variable
    if cont == 1:
        print ("Su ip es ", ipslocal)
        ip = (ipslocal)
    #si no aparecen entonces es que no se detectaron ips
    elif cont == 0:
        print ("No se ha detectado una ip invalida, intente manualmente.")
    #si tiene mas de una ip en las interfazes tendras que elegir cual usar
    else:
        print ("\nEstas son las ips de tus interfaces de red.\n")
        #mostrar todas las ips en orden
        while ayu < cont:
            print (ayu, ".", ipslocal[ayu])
            ayu += 1
        select = int(input("\nSeleccione una interfaz: "))
        ip = ipslocal[select]
        print ("La ip seleccionada es: ",ip )
        mask = input("\nIntroduce el prefijo de red a escanear: /") 
else: #ip manual
    ip = input("Introduce la ip de red: ")
    mask = input("Introduce el prefijo de red: /")

red = (ip + "/" + mask)
ip_red = ipaddress.ip_network(red, False) #crear lista con todas las ips de la red
print ("\nRed: ", ip_red)
os.system("cls")
print ("Dispositovos encontrados:\n")
for ip in ip_red: #iterar la lista y poner cada ip en la variable 'ip'
    #ping a la ip y guardar resultado en la variable response
    response = os.popen(f"ping -n 1 -w 140 {ip}").read(100)  
    if "bytes=32" in response: #determinar si se ha recibido el ping
        ipscan.append(str(ip))
        print(ip, "is up")
print ("\nLa busqueda ha finalizado.")

#escaner de puertos
while True:
    print("\n(y=yes|default=no)")
    ayu = str(input("¿Quieres escanear puertos abiertos?->")).lower()
    if ayu == "y":
        break
    else:
        sys.exit()

ports = list(map(int, input("\nIntroduce los puertos separados por coma:\n-->").split(',')))
#en caso de dato incorrecto corregir este input de ports
for ips in ipscan:
    for port in ports:
        ayu=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = ayu.connect_ex((ips, port))
        ayu.close()
        if result == 0:
            print(f"\nPuertos abiertos de {ips}: \n->", port, "is open")
            #Organizar el resultado del print de puertos abiertos por ip
            #cuando una ip tiene mas de un puerto abierto no se muestra bien
print (input("\nEscaneo terminado, precione enter para cerrar..."))