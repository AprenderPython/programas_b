'''
Usuario: Raúl @spleyades (en Telegram)

Proyecto: Crea un programa que imprima las tablas de multiplicar,
del 1 hasta el numero introducido por el usuario, ej:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
1 x 11 = 11
1 x 12 = 12
Nota: La tabla de cada numero termina en la multiplicacion del numero 12
'''

# Uso math únicamente para verificar que si se ingresa un número flotante
# con parte decimal .0 se lo considere número natural (Ejemplo: 4.0 = 4)
import math

def ingresar_numero_natural():
    '''
    Ingreso un valor y verifico que lo ingresado sea un número natural mayor
    a cero. En caso contrario, itero y sigo pidiendo ingresar un número válido
    '''
    # Itero indefinidamente hasta ingresar un numero natural mayor a cero 
    while True:
        try:   
            # Ingreso un valor y trato de convertirlo a float para ver si
            # es número
            valor = float(input("Ingrese un número natural mayor a cero: "))
        except ValueError:
            # Si hay un error es porque no es número
            print("Error. No ha ingresado un número válido\n")
        else:
            parte_decimal, parte_entera = math.modf(valor)
            # Verifico que sea un número positivo y no tenga decimales
            if valor > 0 and parte_decimal == 0:
                # Hago la conversión a número entero a fines de eliminar el ".0"
                return int(valor)
            else:
                print("Error. El número debe ser natural mayor a cero\n")        
    
def mostrar_tabla(nro):
    ''' Muestro en pantalla la tabla de multiplicar de un número ingresado '''
    for y in range(12):
        print(f"{nro} x {y+1} = {(nro) * (y+1)}")

# Ingreso un número verificando que sea un entero mayor a 0
nro_ingresado = ingresar_numero_natural()

# Itero para mostrar la tabla de multiplicar de cada número desde el 1 hasta
# número ingresado
for x in range(nro_ingresado):
    print()
    mostrar_tabla(x+1)   
