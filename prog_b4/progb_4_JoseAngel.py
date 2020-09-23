"""

Proyecto Intermedio:

Crear un programa que detecte la hora actual del dispositivo, y 
en base a eso determine si es de día, tarde o noche, Luego debe pedirle 
al usuario que ingrese su nombre y saludar al usuario con la informacion 
ya obtenida, por ejemplo:

"Buenas tardes stary"

Opcional:

Dependiendo si es de dia, tarde o noche, el programa tiene que luego del 
saludo decirle una frase escogida aleatoriamente, por ejemplo:

"Buenas noches stary, ya es hora de dormir", 
"Buenas noches stary, hasta mañana"

nota:investigar cuando es de dia, tarde o noche para realizar este programa
code:#proyIn002

jose angel - @jabaselga
v0.1 020920 estructura del programa
v0.2 020920 el programa cumple con las especificaciones
v0.3 030920 saber cuando sale el sol y cuando se pone, no hay control de errores
PENDIENTE CONTROL DE ERRORES
v0.4 040920 version final, mas frases y cometnarios

LIBRERIAS 
pip install requests

"""
from datetime import time, datetime
import random
import requests         # es necesario instalarla

saludo = [ "Buenos días", "Buenas tardes", "Buenas noches"]
#Puedo poner tantas frases como quiera, luego controlaré la logitud para elegir una al azar
# frases -> [   [mañana], 
#               [tarde], 
#               [noche]
#           ]
frases = [  ["Que pases un buen día", "Que te sea leve", "Divierte", "Hoy estas radiante", 
                "Otro día para ser felices", "Nada como un café para comenzar el día"],                 # frases mañana
            ["Que duermas bien la siesta", "Sal a pasear", "No estes mucho rato en el bar", 
                "Disfruta de las cosas simples", "Disfruta de la puesta de sol"],                       # frases tarde
            ["Pronto a dormir", "No te quedes mucho rato viendo la TV", "Que sueñes con los angelitos", 
                "Que la luz te acompañe", "Que duermas bien", "Que las estrellas te acompañen"]         # frases noche
        ]

# Se usa del servicio ipgeolocation para saber cuando sale el sol (sunrise) y cuando se pone (sunset)
API_KEY = 'f2833266890f4c94a1be8f5af7157cb6'
# por la IP de la WAN voy a saber más o menos donde estoy

# Definimos la hora de saludo por si no hay conexión a internet
manana = time (hour=7, minute=0, second=0)        # a partir de esta hora es mañana
tarde = time (hour=14, minute=0, second=0)        # a partir de esta hora es tarde
noche = time (hour=21, minute=0, second=0)        # a partir de esta hora es noche

# Detectar la hora actual del dispositivo
hora = datetime.now().time()
# Pasar hora del sistema a segundos
seg_s = hora.second + hora.minute*60 + hora.hour*60*60

# lanzamos todo en un try por si no hay conexión a internet y no nos puede geolocalizar
try:
    # Miro mi IP de la WAN
    ip_r = requests.get('https://ifconfig.me/ip/')
    IP = ip_r.text  
    LANG = 'sp'
    # y con la IP la geoposiciono y con ello saco la salida y puesta del sol
    URL = 'https://api.ipgeolocation.io/astronomy?apiKey=' + API_KEY + '&ip=' + IP + '&lang=' + LANG
    r = requests.get(URL)
    data = r.json()

    # convierto los valores a time para poder hacer las comparaciones
    h_m, m_m = data["sunrise"].split(":")                           # saco la hora y minutos de la salida de sol
    h_n, m_n = data["sunset"].split(":")                            # saco la hora y minutos de la puesta de sol
    manana = time (hour=int(h_m), minute=int(m_m), second=0)        # a partir de esta hora es mañana
    noche = time (hour=int(h_n), minute=int(m_n), second=0)         # a partir de esta hora es noche

    print ('Hora de salida de sol: {}'.format (manana))
    print ('Hora de puesta de sol: {}'.format (noche))

    # hora en formato string
    hora_inet_s = data["current_time"]
    h_i, m_i, s_i_d = hora_inet_s.split(':')
    s_i, s_id = s_i_d.split('.')
    # Pasar hora de internet a segundos
    seg_i = 60*60*int(h_i) + 60*int(m_i) + int(s_i)

    # hora en formato time para luego poder realizar las comparaciones
    hora_inet = time(hour=int(h_i), minute=int(m_i), second=int(s_i), microsecond=int(s_id)* 1000)

    print ('Hora sistema:  {}'. format (hora))
    print ('Hora internet: {}'. format (hora_inet))
    # Control de errores: hora del sistema no coincide con la de internet
    # si hay una diferencia de más de 1000 seg. avisamos al usuario
    if (abs(seg_s - seg_i) > 1000):
        print ('Es posible que tengas mal la hora del sistema')

    print ('Usted tiene pinta de estar en {}'. format (data ["location"] ["country_name"]))
except:
    pass

if (hora >= manana) and (hora < tarde):
    estado = 0                                  #   Es por la mañana
elif (hora >= tarde) and (hora < noche):
    estado = 1                                  #   Es por la tarde
else:
    estado = 2                                  #   Es por la noche

# Bucle para coger el nombre y asegurarnos que no se ha equivocado
nok = True
while nok:
    nombre = input ("¿Cual es tu nombre? ")
    valor = input ('¿es correcto? S/N: ')
    while (valor != 'n') and (valor != 'N') and (valor != 's') and (valor != 'S'): 
        valor = input ('¿esta seguro? S/N: ')
    if valor == "S" or valor == 's':
        nok = False

# Imprimir el resultado de lo que nos pide el programa
print ('----------------------------------------')
print ("{} {}".format (saludo [estado], nombre))
print (frases[estado] [random.randint(0,len(frases[estado])-1)])

