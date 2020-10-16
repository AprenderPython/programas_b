""" 
Detalles:

Determina si un pokemon existe

Requerimientos:

Crea un programa que verifique si existe un Pokémon, el usuario debe ingresar el nombre de algún Pokémon y luego usando webscraping verificaras si existe un Pokémon con ese nombre en una de las paginas proporcionadas u otras, si existe: Debe imprimirle en pantalla que existe el Pokémon, el nombre del Pokémon y el tipo de Pokémon que es, sino imprimir en pantalla 

Ej:Hemos encontrado tu Pokémon: 
   Nombre:Pikachu Tipo:Electrico
 Sino:
Tu Pokémon no ha sido encontrado o no existe

Webs donde pueden sacar informacion:
Link 1 (https://www.pokemon.com/es/pokedex/) 
Link 2 (https://pokemon.fandom.com/es/wiki/Lista_de_Pokémon) 

Nota: No es obligatorio solo limitarse a esas webs, pueden buscar otras, pero estas las pueden usar.


LIBRERIAS ADICIONALES

pip install beautifulsoup4
pip install lxml

"""
from requests import get
from bs4 import BeautifulSoup
import sys

def pedir_nombre ():
    nombre=input('Introduce el nombre de pokemon a verificar:')
    return nombre


def chequear_pokemon (pokemon):
    """ 
        Busca si 'pokemon' existe enla web https://www.pokemon.com/es/pokedex/
        Devuelve True o False, segun si lo ha encontrado o no, y la lista
        de tipos a los que pertenece dicho pokemon
    """
    pokemon_com = 'https://www.pokemon.com/es/pokedex/' + pokemon
    tipo = []
    pokemonpage=get(pokemon_com)
    if pokemonpage.status_code != 200:
        return False, None      # El pokemon no existe o no funciona la web
    else:
        soup=BeautifulSoup(pokemonpage.text, "lxml")    # generar el objeto bs4
        for link in soup.find_all('a'):
            if 'type' in link.get('href'):  # busca la cadena que nos da el tipo
                tipo.append(link.text)      # junto todos los tipos en una lista
        tipo=set(tipo)                      # elimino los duplicados
        tipo=list(tipo)
    return True, tipo

def chequear_fandom (pokemon):
    pokemonpage=get('https://pokemon.fandom.com/es/wiki/Lista_de_Pokémon')
    if pokemonpage.status_code != 200:
        return False, None      # No funciona la web
    else:
        tabla_pk = []
        pika = []
        pokemon=pokemon.title()     # nombre del Pokemon escrito correcto
        dicc = {"title": pokemon}   # generamos un diccionario para buscar el pokemon
        soup=BeautifulSoup(pokemonpage.text, 'lxml')
        tablas=soup.find_all('table', { "class" : "tabpokemon sortable mergetable"})
        # Buscamos todas las tablas de esa clase que son los que contienen los pokemon y tipos            
        for t in tablas:
            if t.find_all('a', dicc):   # busca el pokemon en la tabla
                tabla_pk=t              # nos quedamos con la fila donde aparece el pokemon
        
        if not tabla_pk:                # si no esta en ninguna tabla el pokemon no existe
            return False, None
        
        #tabla_pk.find_all('a', dicc)
        filas=tabla_pk.find_all('tr')   # troceamos la tabla en filas
        for f in filas:
            if f.find_all('a', dicc):
                pika = f                # nos quedamos con la fila donde esta el pokemon
        last=pika.find_all('a')         # guardamos la fila
        la=[]
        for a in last:
            #print (a.attrs)
            if 'Tipo' in a.attrs['title']:  # Guardamos las celdas donde aparece el texto 'Tipo'
                la.append(a.attrs['title'])
        
        for i,l in enumerate(la):           # eliminar la cadena 'Tipo '
            _, la[i] = l.split(' ')
        la = list (map (lambda n: n.title(), la)) # formateamos mayuscula la primera letra del tipo
        
        return True, la                    # Devolvemos la lista de tipos

def imprimir_datos(web, tipo):
    # imprimir la inforación de la primera web.
    print ("________________________________________________________________________________")
    print ('Información buscada en:')
    print (web)
  
    if not tipo:
        print (f'El pokemón {pokemon} no existe o esta caida la web.')
    # Como mucho un pokemon puede ser de dos tipos:
    elif len(tipo)==1:
        print (f'El pokemon {pokemon} es del tipo: {tipo[0]}.')
    else:
        tipo.sort()
        print (f'El pokemon {pokemon} es del tipo: {tipo[0]} y {tipo[1]}.')
    print ("________________________________________________________________________________")

# programa PRINCIPAL
if __name__ == "__main__":
    arguments_count=len(sys.argv)
    
    print ("________________________________________________________________________________")
    print ('Ejercicio b8. Determina si un determinado pokemon existe y de que tipo es.')
    print ('@jabaselga')
    print ("________________________________________________________________________________")

    if arguments_count > 2:
        print ('Para ejecutar el comando:')
        print (f'{sys.argv[0]} [pokemon_name]')

    elif arguments_count == 2:
        pokemon=sys.argv[1]
    else:   #hay que pedir el nombre del pokemon
        pokemon=pedir_nombre()

    es_pokemon, tipo = chequear_pokemon(pokemon)
    imprimir_datos ('https://www.pokemon.com/es/pokedex/', tipo)
    
    es_pokemon, tipo = chequear_fandom(pokemon)
    imprimir_datos ('https://pokemon.fandom.com/es/wiki/Lista_de_Pokémon', tipo)
    