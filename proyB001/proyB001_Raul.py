# Proyecto: Determinar si un número ingresado es par o impar 
# Usuario: Raul @spleyades (en Telegram)

def numero_par (x):
    ''' Si el resto de dividir a un número por 2 es igual a 0 entonces
    dicho número es par '''
    return (x % 2) == 0

# Itero hasta que el número ingresado sea válido
while True:
    try:
        # Pido ingresar un número y lo convierto a número entero        
        num = int(input("Ingrese un número entero: "))
    except:
        # Si no es número válido, se trata como un error y vuelvo a iterar hasta ingresar un número
        print("Error. No ha ingresado un número entero")
    else:
        # Si el número ingresado es entero, uso una función para detectar si es par o impar
        if numero_par(num):
            print("El número %d es par" % num)
        else:
            print("El número %d es impar" % num)
        break    # salgo del bucle while
