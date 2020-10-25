#Alias de telegram : Rumivi
import socket

print("Alias de telegram Rumivi")
print("__________________")

puertos_usuales=(20,21,22,23,25,53,67,80,81,82,123,143,156,443)
puertos_abiertos=[]


# Establece conexion con la ip
def portSc(ip,Port): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = client.connect_ex((ip,Port))
    if result == 0:
        return True
        client.close()

#Función para el escaneo comun
def escaneocomun(ip): 
    for port in puertos_usuales:
        print(f"Escaneando puerto {port}")
        result = portSc(ip,port)
        if result == True:
            puertos_abiertos.append(port)

    if len(puertos_abiertos) == 0:
        print("No se encontraron puertos abiertos")
    else:
        print("Se encontraron los siguientes puertos abiertos")
    for i in puertos_abiertos:
        print(f" El puerto {i} está abierto")

#Función para el escaneo especifico
def escaneoespecifico(ip):
    print("Introduce los numero de puerto que deseas escanear separados por comas")
    portList = input()
    listDiv = portList.split(',')
        
    for port in listDiv:
        print(f"Escaneando puerto {port}")
        result = portSc(ip,int(port))
        if result == True:
            puertos_abiertos.append(port)

    if len(puertos_abiertos) == 0:
        print("No se encontraron puertos abiertos")
    else:
        print("Se encontraron estos puertos abiertos")
    for i in puertos_abiertos:
        print(f"El puerto {i} esta abierto")

#Función para el escaneo por rango
def escaneorango(ip,puerto1,puerto2):
    for port in range(port1,port2+1):
        print(f"Escaneando puerto {port}")
        result = portSc(ip,port)
        if result == True:
            puertos_abiertos.append(port)

    if len(puertos_abiertos) == 0:
        print("No se encontraron puertos abiertos")
    else:
        print("Se encontraron estos puertos abiertos")
        for i in puertos_abiertos:
            print(f"El puerto {i} esta abierto")

if 1==0:
    sys.exit()
else:
    while True:
        try:
            modoS = int(input("Seleccione un modo de escaneo:\n1-Común (Escanea los puertos mas comunes)\n2-Rango (Escanea puertos dentro del rango introducido)\n3-Especifico (Escanea puertos especificados por el usuario)\n"))
        except ValueError:
            print("Ingresa un numero")

        if modoS >=1 and modoS <= 3:
            break
        else:
            print("Elija un modo de escaneo")

    if modoS == 1:
       	ip = input("Has seleccionado modo común. Indica la direccion IP que quieres escanear\n")
        escaneocomun(ip)

    elif modoS == 2:
        ip = input("Has seleccionado modo rango. Indica la direccion IP que quieres escanear\n")
        port1 = int(input("Introduce el puerto inicial\n"))
        port2 = int(input("Introduce el puerto final\n"))
        escaneorango(ip,port1,port2)

    elif modoS == 3:
        ip = input("Has seleccionado modo específico. Indica la direccion IP que quieres escanear\n")
        escaneoespecifico(ip)