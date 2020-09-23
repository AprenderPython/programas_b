# Usuario: Raúl @spleyades (en Telegram)

# Proyecto Intermedio: Crear un programa que detecte la hora actual del
# dispositivo, y en base a eso determine si es de día, tarde o noche.
# Luego debe pedirle al usuario que ingrese su nombre y saludar al usuario
# con la informacion ya obtenida, por ejemplo: "Buenas tardes stary"
#
# Opcional: Dependiendo si es de dia, tarde o noche, el programa tiene que
# luego del saludo decirle una frase escogida aleatoriamente, por ejemplo:
# "Buenas noches stary, ya es hora de dormir", "Buenas noches stary,
# hasta mañana"

# Importo esta función para obtener la hora actual del sistema
from datetime import datetime

# Importo esta función para obtener un valor al azar en una lista
from random import choice

# Asigno valores a 3 listas con saludos dependiendo la hora del día
lista_saludos_dia = ["qué tengas una hermosa mañana",
                     "ojalá hayas dormido bien",
                     "qué todo vaya bien en el trabajo",
                     "espero te guste el desayuno que preparé"]
lista_saludos_tarde = ["vayamos a merendar a algún bar",
                       "vamos a pasear por el parque antes de anochezca",
                       "acompañame a comprar unas cosas",
                       "qué gusto volver a verte"]
lista_saludos_noche = ["ya es hora de dormir",
                       "hasta mañana",
                       "qué tengas lindos sueños",
                       "ojalá mañana sea un día mejor"]

# Pido ingresar un nombre hasta que la respuesta no sea una cadena vacía
while True:
    nombre = str(input("Ingrese su nombre: ")).strip()
    if len(nombre):
        break

# Ontengo la hora actual
hora_actual = datetime.now().hour

# Considero lo siguiente para saludar:
# Si la hora actual está entre las 6 am y las 12 del mediodía -> Buenos días
# Si la hora actual está entre las 12 del mediodía y las 18 hs -> Buenos tardes
# En cualquier otro rango horario -> Buenas noches
# Imprimo un saludo personalizado de acuerdo a dicha hora obteniendo un valor
# al azar de la lista que corresponda
if 6 <= hora_actual <= 12:
    print("Buenos días {0}, {1}".format(nombre, choice(lista_saludos_dia)))
elif 12 < hora_actual < 18: 
    print("Buenas tardes {0}, {1}".format(nombre, choice(lista_saludos_tarde)))
else:
    print("Buenas noches {0}, {1}".format(nombre, choice(lista_saludos_noche)))



    
