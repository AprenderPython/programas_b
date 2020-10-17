# semana 41


# usamos esta libreria:
# https://pypi.org/project/gazpacho/
# https://gazpacho.xyz/#dir
from gazpacho import get, Soup
import os
import re


def peticion(objetos):
    """
    Hacemos una petición. Pasamos una lista con código html para limpiar
    """
    # limpiamos de html
    try:
        # aqui si hay mas de uno
        for i in range(len(objetos)):
            filtro = re.compile('<.*?>')
            objetos_limpio = re.sub(filtro, '', str(objetos[i]))
            objetos[i] = objetos_limpio
            objetos[i] = objetos_limpio.strip()
        # eliminamos duplicados
        objetos_sin_duplicados = set(objetos)
        # ordenamos la lista
        objetos_sin_duplicados = sorted(list(objetos_sin_duplicados))
        for i in range(len(objetos_sin_duplicados)):
            if i == len(objetos_sin_duplicados)-1:
                print(f"y {objetos_sin_duplicados[i]}.")
            elif i == len(objetos_sin_duplicados)-2:
                print(f"{objetos_sin_duplicados[i]} ", end="")
            else:
                print(f"{objetos_sin_duplicados[i]}, ", end="")

    except:
        # y por aquí si solo hay hay un elemento
        filtro = re.compile('<.*?>')
        objetos_limpio = re.sub(filtro, '', str(objetos))
        objetos = objetos_limpio.strip()
        print(f"{objetos}.")





os.system('clear')

print("Algunos nombres de Pokémons: Ivysaur, Charmander, Venusaur, etc.")

paso = True
nombre = ''

# pedimos el dato y bajamos la página es existe
while paso == True:
    try:
        nombre = input("¿Qué Pokémon estas buscando? ")
        url = "www.pokemon.com/es/pokedex/" + nombre
        html = get(url)
        gazpacho_soup = Soup(html)
    except:
        print(
            f"Tu Pokémon '{nombre}' no ha sido encontrado o no existe. ", end="")
        paso = True
    else:
        paso = False

print("")


print(nombre)
print("-"*len(nombre))

# tipos
print("Tipos: ", end="")
tipos = gazpacho_soup.find('a', attrs={'href': '/es/pokedex/?type='})
peticion(tipos)

print("")

# debilidades
print("Debilidades: ", end="")
debilidades = gazpacho_soup.find('a', attrs={'href': '/es/pokedex/?weakness='})
peticion(debilidades)

print("")



