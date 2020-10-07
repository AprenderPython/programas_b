'''
Usuario: Raúl @spleyades (en Telegram)

Requerimientos: Crea un programa que lea una ip y determine su clase según su rango,
la información que debe mostrar debe ser la siguiente:
    °Clase de ip (clase a, b o c)
    °Cuantos host pueden haber en esa subred 
Ej: en una clase c pueden haber 254 host por cada red, por lo tanto
imprimiría 254 por la red actual)
'''

# Uso este módulo para verificar la IP ingresada
import re

# Patrón de búsqueda que verifica que se ingrese un número IP válido
patron_IP = re.compile(r'''^([01]?\d\d?|2[0-4]\d|25[0-5])\.
    ([01]?\d\d?|2[0-4]\d|25[0-5])\.
    ([01]?\d\d?|2[0-4]\d|25[0-5])\.
    ([01]?\d\d?|2[0-4]\d|25[0-5])$
    ''', re.VERBOSE)

# Uso un diccionario para asignar una cadena de información a cada clase de IP
datos_IP = {
    "A": "Clase A. Esta clase es para las redes muy grandes (Hay 128 redes de "
         "la clase A con 16.777.214 posibles hosts).",    
    "B": "Clase B. Se utiliza para las redes de tamaño mediano (Hay 16.384 "
         "redes de la clase B con 65.534 posibles hosts).",
    "C": "Clase C. Se utiliza para las redes de tamaño pequeño (Hay 2.097.152 "
         "redes de la clase C con 254 posibles hosts).",
    "D": "Clase D. Utilizado para los multicast.",
    "E": "Clase E. Se utiliza para propósitos experimentales solamente."    
}

while True:

    # Ingreso una IP y elimino espacios a izquierda y derecha antes de validar
    ingreso_IP = input("Ingrese un número de IP: ").strip()
    
    # Uso expresiones regulares para verificar que sea válida la IP
    ingreso_valido = re.findall(patron_IP, ingreso_IP)

    if bool(ingreso_valido):
        # Si es válido me quedo con el primer octeto y de acuerdo al rango
        # determino a qué clase pertenece el IP y muestro información acorde
        primer_octeto = int(ingreso_valido[0][0])
        
        if primer_octeto <= 127:
            print(datos_IP["A"], end = " ")

            # En caso de ser una dirección IP especial doy información extra.
            # Uso expresiones regulares para considerar todas las combinaciones
            # con 0 (Ej: 00.00.00.0; 0.0.0.0; 000.000.000.000; 0.00.000.0; etc)
            if re.search(r"^0{1,3}\.0{1,3}\.0{1,3}\.0{1,3}$", ingreso_IP):
                print("La dirección ingresada IP 0.0.0.0 se utiliza para "
                      "la red por defecto.")
            elif primer_octeto == 127:
                print("El intervalo 127.0.0.0 a 127.255.255.255 está reservado "
                      "como dirección loopback y no se utiliza.")
        elif primer_octeto in range(128,192):
            print(datos_IP["B"])
        elif primer_octeto in range(192,224):
            print(datos_IP["C"])
        elif primer_octeto in range(224,240):
            print(datos_IP["D"])
        else:
            print(datos_IP["E"], end = " "),

            # En caso de ser una dirección IP especial doy información extra
            if ingreso_IP == "255.255.255.255":
                print("Broadcast: los mensajes que se dirigen a todas las "
                      "computadoras en una red se envían como broadcast. "
                      "Estos mensajes utilizan siempre la dirección IP "
                      "255.255.255.255."),
        break
    else:
    	print ("Error. No es un número IP válido (entre 0.0.0.0 y "
               "255.255.255.255)\n")
