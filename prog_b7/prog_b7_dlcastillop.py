from ipaddress import IPv4Address #Importar función IPv4Address

a = input('Introduce una dirección IPv4: ') #Pedir dato

#Buscar el rango en donde se encuentra la dirección IP introducida
if IPv4Address('0.0.0.0') <= IPv4Address(a) <= IPv4Address('0.255.255.255'):
    print('Has introducido una dirección reservada.')
else:
    if IPv4Address('127.0.0.0') <= IPv4Address(a) <= IPv4Address('127.255.255.255'):
        print('Has introducido una dirección loopback.')
    else:
        if IPv4Address('224.0.0.0') <= IPv4Address(a) <= IPv4Address('239.255.255.255'):
            print('Has introducido una dirección multicast.')
        else:
            if IPv4Address('240.0.0.0') <= IPv4Address(a) <= IPv4Address('255.255.255.255'):
                print('Has introducido una dirección broadcast.')
            else:
                if IPv4Address('1.0.0.0') <= IPv4Address(a) <= IPv4Address('127.255.255.255'):
                    print('Has introducido una dirección IPv4 de clase A.')
                    print('Puede tener hasta 16777214 hosts.')
                else:
                    if IPv4Address('128.0.0.0') <= IPv4Address(a) <= IPv4Address('191.255.255.255'):
                        print('Has introducido una dirección IPv4 de clase B.')
                        print('Puede tener hasta 65534 hosts.')
                    else:
                        if IPv4Address('192.0.0.0') <= IPv4Address(a) <= IPv4Address('223.255.255.255'):
                            print('Has introducido una dirección IPv4 de clase C.')
                            print('Puede tener hasta 254 hosts.')