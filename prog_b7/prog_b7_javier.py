# prog_b7_javier.py
# javier
# semana 40


import ipaddress

paso = True


# pedimos la ip
while paso == True:
    ip_para_analizar = input("Escribe la ip que quieres analizar: ")
    try:
        ip_para_analizar = ipaddress.ip_address(ip_para_analizar)
    except:
        print("Eso no es una IP. ", end="")
        paso = True
    else:
        paso = False


# separamos la ip en secciones
partes_ip = str(ip_para_analizar).split(".")

# pasamos las 4 secciones a int
for numero in range(4):
    partes_ip[numero] = int(partes_ip[numero])

# analizamos cada sección
if partes_ip[0] in range(0,128): # rango va hasta el número anterior 
    print("Clase A. Número de hosts: 16.777.214")

if partes_ip[0] in range(128,192):
    print("Clase B. Número de hosts: 65.534")

if partes_ip[0] in range(192,224):
    print("Clase C. Número de hosts: 254")

if partes_ip[0] in range(224,240):
    print("Clase D. Número de hosts: No tienen")

if partes_ip[0] in range(240,248):
    print("Clase E. Número de hosts: No tienen")

