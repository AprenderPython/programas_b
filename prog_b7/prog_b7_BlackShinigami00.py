import socket
import sys
import ipaddress

print("|==============================================|")
print("|    Identificador de Clases de IPS            |")
print("|            Escrito en Python 3:              |")
print("|    por BlackShinigami                        |")
print("|        telegram: @BlackShinigami00           |")
print("|==============================================|")
def IPraneg(ip): # Analiza el primer octeto para determinar la clase de la IP

    if int(ip) <= 126:

        print("La IP es de clase 'A', y soporta 16777214 host.")

    elif int(ip) <= 191 and int(ip) > 127:
        print("La IP es de clase 'B', y soporta 65534 host.")

    elif int(ip) == 127:
        print("Esta direccion esta reservada para Localhost.")

    elif int(ip) <= 223 and int(ip) > 191:

        print("La IP es de clase 'C',y soporta 254 host.")

    elif int(ip) <= 239 and int(ip) > 191:

        print("Esta IP es de clase 'D' y se usa en el multicast.")

    elif int(ip) <= 255 and int(ip) > 239:
        print("Esta IP es de clase 'E' y es reservada.")

def getInfo(ip):

    IP = ipaddress.IPv4Address(ip)

    print(f"La vercion de la ip es IPv{IP.version}")

    if IP.is_multicast == True:
        print("La IP es para multicast")
    else:
        pass

    if IP.is_global == True:
        print("La IP es global")
    else:
        pass

    if IP.is_reserved == True:
        print("La Ip es reservada")
    else:
        pass

    if IP.is_link_local == True:
        print("La IP es reservada para un enlace local")
    else:
        pass


while True:

    print("Deseas usar tu direccion IP o deseas introducirla manualmente\n1)IP Automatica\n2)IP Manual")

    Awnser = input(">>> ")

    if Awnser == "1":
        Computer = socket.gethostbyname_ex(socket.gethostname()) # Obtiene la direccion IP de tu PC

        Host = Computer[2][0]

        ipTotal = Computer[2][0]

        print("La ip introducida  es -> ",Host)

        HostIP = Host.split('.') # Divide la IP introducida en una lista

        IPraneg(HostIP[0]) # Obtiene el primer octeto de la IP

        break

    elif Awnser == "2":
        Host = input("Introduce una direccion IP\n>>> ")
        ipTotal = Host

        for i in Host:
            if i == ".":
                pass
            else:
                try:
                    i = int(i)
                except ValueError:
                    print("Ip introducida no valida el programa se finalizado")
                    sys.exit()


        print("La ip introducida  es -> ", Host)

        HostIP = Host.split('.') # Divide la IP introducida en una lista

        IPraneg(HostIP[0]) # Obtiene el primer octeto de la IP

        break

    else: # Evita que el programa caiga si el usuario introduce una opcion incorrecta
        print("La opcion seleccionada no existe")

getInfo(ipTotal)











