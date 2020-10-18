#Programa creado por RUMIVI
#Librerias necesesarias: beautifulsoup4, lxml

from bs4 import BeautifulSoup
from requests import get
import sys

print ("Alias de telegram: Rumivi")
nombre=input('Introduce el pokemon que deseas buscar:')

#Busco el pokemon en la web y compruebo si existe
def busca_pokemon (pokemon):

    busqueda = 'https://www.pokemon.com/es/pokedex/' + pokemon
    tipo = []
    resultadobusqueda=get(busqueda)
    if resultadobusqueda.status_code != 200:
        return False, None      #No se encuentra el pokemon

    else:
    	#Obtengo el html	
        soup=BeautifulSoup(resultadobusqueda.text, "lxml")
        for etiqueta in soup.find_all('a'):
            if 'type=' in etiqueta.get('href'): 
                tipo.append(etiqueta.text)                          
        tipo=list(tipo)
 		#Busco la etiqueta y devuelvo el tipo
    return True, tipo

#Imprimo por pantalla el resultado
def imprimir_datos(tipo):

    print ('Resultado de la búsqueda: \n')
    if not tipo:
        print (f'No se ha encontrado a {pokemon}')

    else:
        print (f'{pokemon} es de tipo {tipo[0]}')

#Cálculo principal
if __name__ == "__main__":
    arguments_count=len(sys.argv)
    
    if arguments_count >= 2:
        pokemon=sys.argv[1]
    else:
        pokemon=nombre

    es_pokemon, tipo = busca_pokemon(pokemon)
    imprimir_datos (tipo)


