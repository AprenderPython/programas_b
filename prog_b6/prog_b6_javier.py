# prog_b6_javier.py

from socket import gethostbyname, create_connection, error
import socket
#https://docs.python.org/es/3/library/socket.html


# url base para llamar
url = "google.com"

# datos del dispositivo
host = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())

def chequear_conexion():
    try:
        # con conexión a internet
        gethostbyname(url)
        connexion = create_connection((url, 80), 1)
        connexion.close()
        return True
    except error:
        # sin  conexión a internet
        return False


print(
    f"Este dispositvo: {host} (IP: {ip}) tiene la conexion a internet en: {chequear_conexion()}")