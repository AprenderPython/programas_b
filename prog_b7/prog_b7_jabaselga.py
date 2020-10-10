""" 
Requerimientos:

Crea un programa que lea una ip y determine su clase según su rango, la información que debe mostrar debe ser la siguiente:

°Clase de ip (clase a, b o c)
°Cuantos host pueden haber en esa subred 

Ej: en una clase c pueden haber 254 host por cada red, por lo tanto imprimiría 254 por la red actual)

Ejemplo de la salida del programa: 

"Tu ip es 192.168.0.1 es de clase C y pueden haber 254 host en tu red actual"

code:prog_b7_tuuser.py

Datos para elegir el tipo de IP

Class        Networks                     mask          CDIR       leading bits
A       0.0.0.0   - 127.255.255.255     255.0.0.0         /8        0
B       128.0.0.0 - 191.255.255.255     255.255.0.0       /16       10
C       192.0.0.0 - 223.255.255.255     255.255.0.0       /24       110
D       224.0.0.0 - 239.255.255.255         not defined             1110        Multicast
E       240.0.0.0 - 247.255.255.255         not defined             1111        Reserved

información procedente de:
https://en.wikipedia.org/wiki/Classful_network


LIBRERIAS ADICIONALES


"""
import ipaddress
import sys


# Interactua con el usuario para pedir la IP
def pedir_ip ():
    ip_s = input  ("Introduce una IP en notación clásica o CIDR: ")
    return ip_s

def comprobar_tipos (ipt):
    if ipt.is_multicast:
        print (f'La ip {ipt} es multicast.')
    if ipt.is_private:
        print (f'La ip {ipt} es private.')
    if ipt.is_global:
        print (f'La ip {ipt} es global.')
    if ipt.is_unspecified:
        print (f'La ip {ipt} es sin especificar.')
    if ipt.is_reserved:
        print (f'La ip {ipt} es reservada.')
    if ipt.is_loopback:
        print (f'La ip {ipt} es loopback.')
    if ipt.is_link_local:
        print (f'La ip {ipt} es link local.')    

def es_ip (ip_s):
    """  

    """
    ip      = None
    network = None
    clase   = None
    tipo    = None
    # tipo de ip 1-> notación clásica, 2-> CIDR
    dir_ok  = False

    try:
        ip = ipaddress.IPv4Address(ip_s)
        # si pasa la IP con notación clásica es valida')
        dir_ok = True
        tipo = 1
    except:
        # si no pasa la IP no es valida
        dir_ok = False

    if not dir_ok:
        try:
            network = ipaddress.IPv4Network(ip_s, strict=False)
            # si pasa es una IP con notación CIDR
            ip, _ = ip_s.split('/')
            ip = ipaddress.IPv4Address(ip)
            dir_ok = True
            tipo = 2    # Es notación CIDR, ya hemos guardo IP y network
        except:
            # si no pasa no es ningún 
            dir_ok = False
        
    if tipo == 1:   # es notación clasica, vemos de que clase sería.
        a, b, c, d = ip_s.split('.')
        a, b, c, d = int(a), int (b), int (c), int (d)

        if a < 128:
            clase = "A"
            full_ip = ip_s +'/8'
        elif a < 192:
            clase = 'B'
            full_ip = ip_s +'/16'
        elif a < 224:
            clase = 'C'
            full_ip = ip_s +'/24'
        elif a < 240:
            clase = 'D'
            full_ip = None
        else:
            clase = 'E'
            full_ip = None
        
        try:
            # generamos la variable network para los calculos de prefijo, mascara ...
            network = ipaddress.IPv4Network(full_ip, strict=False)
        except:
            network = None
            
    # devolvera ('None', 'None', 'None', 'None') si lo introducido no es una IP valida
    # en otro caso devolera los valores correctos, de IP, network, clase y tipo
    return (ip, network, clase, tipo)

def imprimir (data):
    
    print (f"Dirección ip: {data[0]}")
    if data[2]:
        print (f'Es una red de clase {data[2]}.')
    else:
        # data[1] -> network, sacamos el prefijo de la red, para luego calcular los hosts
        prefijo = data[1].prefixlen
        print ('Has introducido la dirección IP en formato CIDR.')
        # Aunque se ha usado notación CIDR, usamos el prefijo para saber que clase de red sería
        if prefijo == 24:
            print ('Que por la máscara de red podría ser de clase C')
        elif prefijo == 16:
            print ('Que por la máscara de red podría ser de clase B')
        elif prefijo == 8:
            print ('Que por la máscara de red podría ser de clase A')

    if data[1]:
        print (f'La máscara de red es: {str(data[1].netmask)}')
        # para calcular los host (2^(32-prefijo))-2
        # 32-prefijo -> número de 0 que hay en la máscara
        # -2, 1 por la IP de net y 1 por la IP de broadcast
        prefijo = data[1].prefixlen
        hosts = (2**(32-prefijo))-2 # 1 por broadcast y otro por dirección de red
        print (f'En esta red puede haber {hosts} hosts')
    else:
        print ('Es una red reservada, por tanto el numero de hosts es "not defined"')
        # Esto es por definición de las redes de clase D y E
    
    comprobar_tipos(data[0])

def main_chequear_IP ():
    """ 

    """

    data = (None, None, None, None)
        
    while data[0] == None:
        ip = pedir_ip ()
        data = es_ip (ip)
  
    imprimir (data)

# programa PRINCIPAL
if __name__ == "__main__":
    arguments_count=len(sys.argv)
    
    print ("________________________________________________________________________________")
    print ('Ejercicio b7. Para una dirección IP mostrar clase y número de hosts que admite.')
    print ('@jabaselga')
    print (f'Para ejecutar el comando: {sys.argv[0]} [IP|IP/mask|IP/prefix]')
    print ('Ejemplo de notación clásica: 192.168.4.2')
    print ('Ejemplo de notación CIDR: 192.168.4.2/23 o 192.168.5.2/255.255.240.0')
    print ("________________________________________________________________________________")

    if arguments_count > 2:
        print ('Para ejecutar el comando:')
        print (f'{sys.argv[0]} [IP|IP/mask|IP/prefix]')

    elif arguments_count == 2:
        data = es_ip (sys.argv[1])
        if data[0] != None:
            imprimir(data)
        else:
            print (f'El argumento "{sys.argv[1]}" introducido no es una dirección IP válida')
    else:
        main_chequear_IP()
        