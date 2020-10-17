#create by: StaryDark Telegram:@dark_zly
import requests
import re

name = input("Nombre: ")
print("Cargando...\n")

#cargar codigo html del resultado de busqueda del pokemon
url = ("https://pokemon.fandom.com/es/wiki/" + name)
html = requests.get(url, timeout=10)
html = str(html.text)

#extraer el tipo de pokemon usando expreciones regulares para extraer texto
busqueda = re.findall(r'es un Pokémon.*?int', html)

#determinar si el pokemon existe si la frase dada existe
if "es un Pokémon" in str(busqueda):
    busqueda = str(busqueda[1]) #eliminar caracteres inservibles
    busqueda = busqueda.replace("int", "") #eliminar caracteres inservibles
    print ("Pokemon encontrado:",name, busqueda)
else:
    print("Pokemon no encontrado...")