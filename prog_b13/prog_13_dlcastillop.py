# --------------------------------------------
#
# Propósito: Mantenimiento a una PC con Windows
#
#
# Fecha: 27/11/2020
# --------------------------------------------
# Autor: Daniel Castillo
# 
# Página web: https://certificadocisco.blogspot.com
#
# Redes sociales:
# https://linkedin.com/in/dlcastillop
# https://twitter.com/dlcastillop
# https://github.com/dlcastillop
# --------------------------------------------

import os
from sys import argv, exit

# Función para comprobar si se está ejecutando en Windows
def solo_windows():
    a = os.system('ver > temp.txt')
    os.remove('temp.txt')
    if a != 0:
        print('Este programa es solo para correr en Windows.')
        exit(0)

# --------------------------------------------
# COMIENZA EL PROGRAMA
# --------------------------------------------

# Mostrar opciones
if argv[1] == '?':
    solo_windows()
    print()
    print('python prog_13_dlcastillop.py [OPCIONES...]')
    print('  Mantenimiento a una PC con Windows.')
    print('    Opciones:')
    print('      -p                                 Vaciar papelera de reciclaje')
    print('      -i                                 Información del software del sistema')
    print('      -c                                 Borrar caché DNS')
    print('      -t                                 Borrar archivos temporales')
    print()
    print('  Nota: cuando se vaya a vacia la papelera de reciclaje, tienes que introducir')
    print('        tu nombre de usuario y contraseña. Luego se abrirá una ventana donde')
    print('        tienes que introducir S.')
    exit(0)

# Opción de vaciar la papelera de reciclaje
if argv[1] == '-p':
    solo_windows()

    '''
    Crear un archivo .bat que contiene el comando para vaciar la papelera de reciclaje
    Luego se edita para que contenga el comando que vacía la papelera
    '''
    bat = open('papelera.bat', 'w')
    bat.write('rd /s %systemdrive%\$Recycle.bin')
    bat.close()

    # Pedir nombre de usuario, pues es necesario para formar el comando
    username = input('Introduce tu nombre de usuario: ')

    #Formar comando. El comando ejecuta el archivo .bat creado como administrador
    comando = 'runas /profile /env /user:mydomain\\' + username + ' "papelera.bat"'

    #Ejecutar comando
    os.system(comando)

    exit(0)

# Opción de información del software
if argv[1] == '-i':
    solo_windows()

    # Guardar información del sistema en un archivo de texto
    os.system('systeminfo > temp.txt')

    archivo = open('temp.txt', 'r')

    for linea in archivo:
        if linea.find('Nombre del sistema operativo:') != -1:
            sistema_operativo = linea[43:]
        elif linea.find('Versi¢n del sistema operativo:') != -1:
            version_windows = linea[43:]
        elif linea.find('Versi¢n del BIOS:') != -1:
            version_bios = linea[43:]
    
    print('Información del software')
    print('------------------------')
    print('Sistema operativo:', sistema_operativo)
    print('Versión del sistema operativo:', version_windows)
    print('Versión del BIOS:', version_bios)
 
    archivo.close()

    os.remove('temp.txt')
    exit(0)

# Opción de borrar caché DNS
if argv[1] == '-c':
    solo_windows()
    os.system('ipconfig/flushdns > temp.txt')
    os.remove('temp.txt')
    exit(0)

# Opción de borrar archivos temporales
if argv[1] == '-t':
    solo_windows()
    os.system('del "%tmp%" /s /q > temp.txt')
    os.remove('temp.txt')
    exit(0)