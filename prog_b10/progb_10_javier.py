import requests
import re
import os
from bs4 import BeautifulSoup


os.system('clear')

print("Algunas cuentas: huertoencasamadrid juanpedro jabaselga")
print()

nombre = ''
paso = True


# pedimos el dato y bajamos la página es existe
while paso == True:
    try:
        nombre = input("¿Qué cuenta de Instagram quieres analizar? ")
        url = "https://www.instagram.com/" + nombre.strip()
        html = requests.get(url, timeout=20)
        html = str(html.text)
    except:
        print(f"La cuenta '{nombre}' no existe. ", end="")
        paso = True
    else:
        paso = False

print("")

print(f"Información de: {nombre}")
print("----------------" + "-" * len(nombre))


# nombre de usuario
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
posicion = soup.title.string.find(" (@")
nombre_usuario = soup.title.string[0:posicion]
# print(soup.title.string)
# print(nombre_usuario)



# tipo de cuenta
if html.count("Esta cuenta es privada") == 1:
    print("cuenta privada")

busqueda = re.findall(r'<meta content=".*?@', html)
busqueda = re.findall(r'".*?Posts', str(busqueda))

busqueda = str(busqueda).split()

# limpiamos el primer elemento
busqueda[0] = busqueda[0].lstrip("[\'")
busqueda[0] = busqueda[0].lstrip('"')

# quitamos , y ponemos . para sistema metrico decima
for x in range(0, len(busqueda)):
    busqueda[x] = busqueda[x].replace(",", ".")

# volcamos la información:
print()

print(f"Nombre: {nombre_usuario}")
print(f"Nombre de usuario: {nombre}")
print(f"Cantidad de seguidores: {busqueda[0]}")
print(f"Cantidad de seguidos: {busqueda[2]}")
print(f"Cantidad de publicaciones: {busqueda[4]}")
print(f"Tipo de cuenta: ")
