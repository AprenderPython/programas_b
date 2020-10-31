
print("Alias de telegram Rumivi")
print("__________________")

#Librerías adicionales
import re
import requests
import json

nombre_usuario=input("Ingrese el usuario de instagram que desea buscar: ")
print("Buscando...")
print("__________________")

#Corrijo el formato introducido a uno correcto y elimino espacios y @
nombre_usuario=re.sub('^a-zA-Z \n]', ' ',nombre_usuario).replace('@', '')
nombre_usuario=" ".join(nombre_usuario.split())

#Busco el usuario introducido en instagram
web = requests.get(f"https://www.instagram.com/{nombre_usuario}", timeout=15)

#Si obtiene resultado, procedo con la función
if web.status_code == 200:

    # Utilizo el siguiente script para sacar la informacion de la web
    info_obtenida = re.search(r'window._sharedData = (\{.+?});</script>', web.text).group(1)

    #Si obtengo resultado
    if info_obtenida:

        #Busco los datos en la web convirtiéndolo a formato json
        perfil= json.loads(info_obtenida)['entry_data']['ProfilePage'][0]['graphql']['user']
        
        #Asigno los valores a cada variable
        username=perfil['username']
        full_name=perfil['full_name']
        followers=perfil['edge_followed_by']['count']
        followings=perfil['edge_follow']['count']
        publications=perfil['edge_owner_to_timeline_media']['count']
        if (perfil['is_private'])==True:
            tipocuenta="privada"
        else:
            tipocuenta="publica"

        #Imprimo los datos en pantalla
        print("Nombre de usuario: " + str(username))
        print("Nombre: " + str(full_name))
        print("Numero de seguidores: " + str(followers))
        print("Numero de seguidos: " + str(followings))
        print("Numero de publicaciones: " +str(publications))
        print("La cuenta es " + tipocuenta)


#Si no obtiene resultado
else:
    print("No he encontrado nada para el usuario " + nombre_usuario + \
        ". Compruebe que los datos introducidos sean correctos.")
