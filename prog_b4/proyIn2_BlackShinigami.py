import random
from datetime import datetime
import locale
import sys

# Create by: @BlackShinigami00
# Follow us in http://t.me/aprenderpython

name = input("Ingresa tu nombre por favor:\n>>> ")

locale.setlocale(locale.LC_ALL,'es_ES') #Cambia el formato a español

actual_hour = datetime.now() # Obtiene la hora actual

get_hour = actual_hour.strftime("%H") # Obtiene la hora actual en formato de 24 H
get_hour = int(get_hour)

show_anwser = random.randint(1,3) # Genera el numero de la respuesta que sera mostrada al usuario

print("Hoy es:",actual_hour.strftime("%A, %d de %B del %Y")) # Imprime la fecha actual

if get_hour >= 0 and get_hour < 6:

    print("La hora actual es:",actual_hour.strftime("%I:%M AM")) # Imprime la hora actual segun si es AM o PM
                                                                # Se aplica para todas las demas repeticiones
    if get_hour ==0:

        anwser_1 = "Hola " + name + ", es medianoche ahora, deberias prepararte para ir a la cama"
        anwser_2 = "Hola " + name + ", ya es medianoche descansa que mañana es un nuevo dia"
        anwser_3 = "Hola " + name + ", es hora de ir a la cama ya, que tengas dulces sueños"

        if show_anwser == 1:
            print(anwser_1)
        elif show_anwser == 2:
            print(anwser_2)
        elif show_anwser == 3:
            print(anwser_3)
        sys.exit()
    else:

        anwser_1 = "Hola "+name+", es de madrugada deberias ir a la cama!!!"
        anwser_2 = "Hola "+name+", que descances hasta mañana!!!"
        anwser_3 = "Hola "+name+", no te agotes de mas, ve a la cama ya por favor!!!"

        if show_anwser == 1:
            print(anwser_1)
        elif show_anwser == 2:
            print(anwser_2)
        elif show_anwser == 3:
            print(anwser_3)

elif get_hour >= 6 and get_hour < 12:
    print("La hora actual es:", actual_hour.strftime("%I:%M AM"))

    anwser_1 = "Hola "+name+", muy buenos dias!!!"
    anwser_2 = "Hola "+name+", que tengas un hermoso dia hoy!!!"
    anwser_3 = "Hola "+name+", hace un lindo dia hoy!!!"

    if show_anwser == 1:
        print(anwser_1)
    elif show_anwser == 2:
        print(anwser_2)
    elif show_anwser == 3:
        print(anwser_3)

elif get_hour >= 12 and get_hour <= 18:

    print("La hora actual es:", actual_hour.strftime("%I:%M PM"))

    anwser_1 = "Hola "+name+", buenas tardes!!!"
    anwser_2 = "Hola "+name+", bonita tarde para tomar un paseo!!!"
    anwser_3 = "Hola "+name+", disfruta de tu tarde de hoy!!!"

    if show_anwser == 1:
        print(anwser_1)
    elif show_anwser == 2:
        print(anwser_2)
    elif show_anwser == 3:
        print(anwser_3)

elif get_hour > 18 and get_hour <= 24:

    print("La hora actual es:", actual_hour.strftime("%I:%M PM"))

    anwser_1 = "Hola "+name+", muy buenas noches!!!"
    anwser_2 = "Hola "+name+", hace una hermosa noche para ver las estrellas!!!"
    anwser_3 = "Hola "+name+", bonita noche, disfrutala!!!"

    if show_anwser == 1:
        print(anwser_1)
    elif show_anwser == 2:
        print(anwser_2)
    elif show_anwser == 3:
        print(anwser_3)


