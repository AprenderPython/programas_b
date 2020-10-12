import os
#Hecho por: Stary Dark Telegram:@dark_zly
#Este script solo funciona en windows
response = os.popen("ping -n 2 -w 200 8.8.8.8").read(140) #ping a 8.8.8.8
if "bytes=32" in response: #determina si hay conexion a internet si el ping llego
    print("Hay conexion a internet")
