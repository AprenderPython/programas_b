#Determinar por la hora del Host DIA/NOCHE - sin librerias externas
print("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█                             █
█        SMART-CLOCK          █
█            V.1.0            █
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

\nCreated by ~Outis\n""") #Autor 

import datetime # Importamos la fecha y hora

name = input("Ingresa tu nombre: ") #Entrada de texto, el usuario
name_user = name #Variable para guardar el usuario

#Variables

tiempo = datetime.datetime.now() #Variable para el le fecha y hora actual 
 
saludo = tiempo.strftime('%H:%M:%S') #Variable para guardar solo la hora, minutos y segundos

hora = tiempo.strftime('%H') #Variable para la condicion solo otorga el valor de la hora

#Condicion para p.m y a.m

if saludo >= '12:00:00' and saludo < '23:59:59':
	print("\nLa hora es: ", tiempo.strftime('%H:%M:%S'), "p.m.")
 
if saludo >= '00:00:00' and saludo < '11:59:59':
	print("\nLa hora es: ", tiempo.strftime('%H:%M:%S'), "a.m.")

#Condicion para saludo

if hora >= '06' and hora < '12':
	print("\nBuenos dias", name_user)
else:
	print(" ")

	if hora >= '12' and hora < '18':
		print("Buenas tardes", name_user)
	else:
		print("Buenas noches", name_user)

#Lista de frases aleatorias
import random

frasd=["\nEs hora de comer", "\nQue tengas lindo día", "\nAdelante! que hace un excelente día"] #Frases para el dia
if hora >= '06' and hora < '12':
	print(random.choice(frasd), name_user)
else:
	print(" ")

	frast=["Hace bonita tarde para caminar", "Que tengas una excelente tarde", "Nunca es mala hora para un lunch"] #Frases para la tarde
	if hora >= '12' and hora < '18':
		print(random.choice(frast), name_user)
	else:
		frasen=["Deberias descansar pronto", "Que tengas linda noche", "Hoy ha sido un día duro, ha descansar"] #Frases para la noche
		print(random.choice(frasen), name_user)


# Salir del programa

print("\nPara salir presiona enter..")

input()