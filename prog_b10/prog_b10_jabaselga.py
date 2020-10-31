""" 
Detalles:

Extraccion de datos de cuentas de instagram

Requerimientos:

Crea un programa que a partir de un nombre de usuario de instagram ingresada por el usuario determine si la cuenta existe.

Si existe debe mostrar los siguientes datos de forma ordenada:

°Nombre de usuario
°Nombre
°Cantidad de seguidores
°Cantidad de seguidos
°Cantidad de publicaciones
°Si la cuenta es privada o publica


Programas completados:

code: progb_10_tuuser.py
@aprenderpython
#webscraping

LIBRERIAS ADICIONALES

pip install gazpacho
pip install selenium
chrome & chromedriver to use selenium

"""

from gazpacho import get, Soup
import re
import json

# para usar selenium
try:
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options
    sl=True
except:
    print ('Sin selenium va a ser dificil sacar el tipo de cuenta ...')
    sl=False


url='https://www.instagram.com/'

def pedir_usuario():
    nok = True
    while nok:
        usuario=input('Introduzca un usuario para comprobar: ')
        pattern=re.compile(r'^([0-9a-zA-Z\._]){1,30}$')
        usuario=pattern.fullmatch(usuario.strip())
        if usuario:
            nok=False
 
    return usuario.string

def paser_selenium (page):
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    try:
        browser=Chrome(options=chrome_options)
    except:
        return 'NOMBRE', 'Me fatltan componetes de chrome para sacar el tipo de cuenta.'
    
    browser.get(page)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()

    try:
        tipo=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div/h2')
        tipo=tipo.text
    except:
        tipo='Esta cuenta es pública'
    
    page=browser.page_source
    html_g=Soup(page)
    try:
        nombre=html_g.find('h1', attrs={'class':'rhpdm'})
        nombre=nombre.text
    except:
        nombre='usuario sin nombre'

    return nombre, tipo

def comprobar_estado_json(page, user):
    patron=re.compile(r"window._sharedData\s+=\s+(\{.*?});</script>")
    p=patron.search(page)
    data=json.loads(p.group(1))
    nombre = data['entry_data']['ProfilePage'][0]['graphql']['user']['full_name']
    seguidores = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
    seguidores = f'{seguidores} seguidores'
    seguidos = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count'] 
    seguidos = f'{seguidos} seguidos'
    publicaciones = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count'] 
    publicaciones = f'{publicaciones} publicaciones'
    if data['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']:
        tipo="Esta cuenta es privada"
    else:
        tipo="Esta cuenta es pública"

    user=f'@{user}'

    return user, nombre, seguidores, seguidos, publicaciones, tipo


def existe_usuario(usuario):
    url_user=url+usuario+'/?hl=es'
    try:
        html=get(url_user)
    except:
        return None
    
    return html

def comprobar_estado_sl(html, user, sl):

    html_s=Soup(html)
    a=html_s.find('meta', attrs={'property':'og:description'})
    dic=a.attrs
    n=dic['content'].replace('-',',')
    # arreglar el problema de las ',' en los números
    new_n=n[0]
    for i in range(1,len(n)):
        if n[i-1].isdigit() and n[i]==',' and n[i+1].isdigit():
            new_n += '.'
        else:
            new_n += n[i]
    n=new_n
    n=n.split(',')
    data=(x.strip() for x in n)
    # ('431 Followers', '872 Following', '294 Posts', 'See Instagram photos and videos from JP (@juanpedro)')

    seguidores, seguidos, publicaciones, usuario = data
    *_, usuario = usuario.split(' ')
    # '@juanpedro'
    if '(' in usuario:
        usuario = usuario[1:-1]

    if sl:
        url_user=url+usuario+'/?hl=es'
        nombre, tipo=paser_selenium(url_user)
    else:
        nombre, tipo='¿nombre?','No tienes selenium instaldo, imposible sacar el tipo cuenta...'


    return usuario, nombre, seguidores, seguidos, publicaciones, tipo

def imprimir_datos(usuario, nombre, seguidores, seguidos, publicaciones, tipo):
    print (f'{usuario}'.center(40,"*"))
    print (nombre)
    print (seguidores)
    print (seguidos)
    print (publicaciones)
    print (tipo)

if __name__ == "__main__":
    
    user=pedir_usuario()
    page=existe_usuario(user)
    if page:
        
        usuario, nombre, seguidores, seguidos, publicaciones, tipo = comprobar_estado_sl(page, user, sl)
        imprimir_datos(usuario, nombre, seguidores, seguidos, publicaciones, tipo)

        print('\n\nAhora con json:')
        usuario, nombre, seguidores, seguidos, publicaciones, tipo = comprobar_estado_json(page, user)
        imprimir_datos(usuario, nombre, seguidores, seguidos, publicaciones, tipo)
            
        
    else:
        print ("El usuario no existe..")
        
    print ("Fin del juego".center(40, "*"))