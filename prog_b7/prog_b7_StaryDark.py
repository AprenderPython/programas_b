import ipaddress

ip = ipaddress.IPv4Address(input("Introduce ipv4: "))
#ip_max es la ip maxima que puede llegar una ip
ip_max = 2147483647 #(formato int)2147483647 = (formato ip)127.255.255.255

if int(ipaddress.IPv4Address(ip)) <= ip_max: #determina si es clase A
    print ("Tu ip es clase A    Con 16,777,214 posibles hosts")
else:
    ip_max = 3221225471 #(formato int)3221225471 = (formato ip)191.255.255.255
    if int(ipaddress.IPv4Address(ip)) <= ip_max: #determina si es clase B
        print ("Tu ip es clase:B    Con 65,534 posibles hosts")      
    else:
        ip_max = 3758096383 #(formato int)3758096383 = (formato ip)223.255.255.255
        if int(ipaddress.IPv4Address(ip)) <= ip_max:  #determina si es clase C
            print ("Tu ip es clase:C    Con 254 posibles hosts")