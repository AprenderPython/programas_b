'''
Usuario: Raúl @spleyades (en Telegram)

Requerimientos: Crea un programa que verifique si existe un Pokémon, el usuario
debe ingresar el nombre de algún Pokémon y luego usando webscraping verificaras
si existe un Pokémon con ese nombre en una de las paginas proporcionadas
u otras, si existe: Debe imprimirle en pantalla que existe el Pokémon, el nombre
del Pokémon y el tipo de Pokémon que es, sino imprimir en pantalla 

Ej:Hemos encontrado tu Pokémon: 
   Nombre:Pikachu Tipo:Electrico
 Sino:
Tu Pokémon no ha sido encontrado o no existe

Webs donde pueden sacar informacion:
Link 1 (https://www.pokemon.com/es/pokedex/) 
Link 2 (https://pokemon.fandom.com/es/wiki/Lista_de_Pok%C3%A9mon) 

Nota: No es obligatorio solo limitarse a esas webs, pueden buscar otras, pero
      estas las pueden usar.
'''

import re
import requests
from bs4 import BeautifulSoup

# Uso esta página que almacena información de todos los pokémones a través de
# distintas tablas
URL_BUSQUEDA = "https://pokemon.fandom.com/es/wiki/Lista_de_Pok%C3%A9mon"

def patron_con_tildes(texto):
    '''
    Dada una cadena de texto devuelve una expresión regular que considera todas
    las combinaciones posibles de tildes. Esto es, si ingresa el nombre de un
    pokemon colocando mal una tilde, ejemplo "Pikáchu", lo encuentra igual.
    Así también hay un pokemon llamado "Código cero" que lo encuentra con o
    sin tilde.
    '''

    cadena = "^"
    for x in texto:
        if x in "aàáAÀÁ":
            cadena += "[aàáAÀÁ]"
        elif x in "eéèEÈÉ":
            cadena += "[eéèEÈÉ]"
        elif x in "iíìIÌÍ":
            cadena += "[iìíIÌÍ]"
        elif x in "oóòOÒÓ":
            cadena += "[oòóOÒÓ]"
        elif x in "uùúUÙÚ":
            cadena += "[uùúUÙÚ]"
        elif x == " ":
            cadena += "\s"
        else:     
            cadena += x
    return cadena + "$"


def busco_pokemon(tablas, texto_a_buscar):
    '''
    Busco en las tablas (que son objeto de tipo BeautifoulSoup) si existe
    el pokemon ingresado y muestro información al respecto.    
    '''

    # Creo una expresión regular con el pokemon a buscar permitiendo
    # mayúsculas o minúsculas en forma indistinta
    texto_compilado = re.compile(patron_con_tildes(texto_a_buscar), re.I)
    
    # Creo una expresión regular para rastrear en las columnas de la tabla
    # el tipo del pokemon y quedarme sólo con el tipo sin la palabra "Tipo"    
    tipo_compilado = re.compile('^Tipo\s(.*?)$', re.I)

    # Recorro cada tabla (porque hay 8 en la página)
    for tabla in tablas:

        # Uso findall porque un pokemon puede figurar hasta 2 veces en una misma
        # fila y rastreo por el título del tag <A>
        resultados = tabla.find_all('a', title=texto_compilado)

        if resultados:
            print('Hemos encontrado tu Pokémon!!')

            # Me quedo con la última opción encontrada porque es la que tiene
            # el string con el nombre (la otra hace referencia a una imagen)
            ocurrencia = resultados[len(resultados)-1]
            print(f'Nombre: {ocurrencia.string.upper()}')

            # Avanzo al siguiente tag <A> que es el elemento que contiene
            # el Tipo 1 del pokemon encontrado y busco usando la expresión
            # regular para quedarme con el tipo en cuestión solamente
            tipo_1 = ocurrencia.find_next('a')
            aux = tipo_compilado.search(tipo_1['title'])
            if aux:
                # Si encuentro el tipo lo almaceno en una variable auxiliar
                tipo_pokemon = aux[1].capitalize()

                # Avanzo al siguiente tag <A> que es el elemento que contiene
                # el Tipo 2 del pokemon (que puede no existir)
                tipo_2 = tipo_1.find_next('a')
                aux2 = tipo_compilado.search(tipo_2['title'])

                if aux2:
                    # Si tiene un Tipo 2 lo anexo con "," a la variable auxiliar
                    tipo_pokemon += f", {aux2[1].capitalize()}"
                    
                print(f"Tipo: {tipo_pokemon}")
            break        
    else:
        print('Tu Pokemon no ha sido encontrado o no existe')




print("Espere uno segundos mientras se carga la base de datos de Pokemones...")

# Realizo la petición a la página web
pagina = requests.get(URL_BUSQUEDA)

# Si el status code = 200 implica que la página web existe
if pagina.status_code == 200:

    # Creo un objeto BeautifoulSoup para poder mapear la página web y facilitar
    # la búsqueda de la información. Intento usar el parser lxml que es más
    # eficiente. Si da error, uso el parser nativo que viene con Python
    try:
        sopa = BeautifulSoup(pagina.text, "lxml")
    except:
        sopa = BeautifulSoup(pagina.text, "html.parser")
        
    # Localizo todas las tablas de la página y las guardo en una colección
    tablas = sopa.find_all('table', class_=re.compile(r'^tabpokemon\ssortable\smergetable.*$', re.I))

    while True:
        ingreso = input("\nIngrese nombre de pokemon a buscar (o pulse 0 "
                        "para salir): ").strip()

        # Si ingreso 0, termino la ejecución
        if ingreso == '0':
            break
        
        # Si se pulsa Enter sin ingresar nada no se sale
        if len(ingreso) == 0:
            continue

        busco_pokemon(tablas, ingreso)
else:
    print("No se puede encontrar la página para buscar los pokemones")
