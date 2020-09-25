print(
    "======================================================================================================================\n"
    "= Compruevador de existencia de conexion a internet!                                                                 =\n"
    "=          Escrito en Python 3                                                                                       =\n"
    "=                Por 'BlackShinigami'                                                                                =\n"
    "=     Telegram -> @BlackShinigami00                                                                                  =\n"
    "=                                                                                                                    =\n"
    "======================================================================================================================\n")

import sys
import os
array = ["ww.google.com", "8.8.8.8"]

def looking_for_internet():
    print("Detectando si tienes conexion a internet...")

    internet = False
    
    for i in range(len(array)):
    
        response = os.popen("ping "+array[i])
    
        for line in response.readlines():
    
            if ("ttl" in line.lower()):
    
                internet = True
    
                break
    
    if internet == True:
        print("La conexion a internet funciona correctamente")
    else:
        print("Algo esta fallando, no hay conexion a internet!!!")

looking_for_internet()

while True:
    pross = input("Deseas repetir el proceso Y/N\n>>> ")

    if pross.capitalize() == "Y":
        looking_for_internet()

    elif pross.capitalize() == "N":
        print("El programa se ha cerrado\nHasta la proxima")
        sys.exit()
    else:
        print("Opcion no valida intentalo otra ves\n")
        









