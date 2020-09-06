# Usuario: Raúl @spleyades (en Telegram)

# Proyecto: Crear un programa que guarde 5 números y luego los imprima en
# pantalla ordenados ascendentemente. El programa debe poder aceptar números
# enteros y decimales. Si se ha introducido un dato erroneo, decidle al usuario
# que solo se aceptan numeros y volver a pedir que introduzca los numeros.


# Necesito importar math para poder usar la función que devuelve la parte
# decimal de un número ingresado
import math

lista = []
x = 0
# Itero hasta lograr 5 números ingresados válidos 
while x < 5:
    try:
        num = float(input("Ingrese un número: "))        
    except:
        # Si al convertir lo ingresado a float se genera un error es porque
        # no se ingresó un número
        print("Error. Solo se aceptan números")
    else:
        # Uso la función modf para quedarme con la parte decimal
        parte_decimal, parte_entera = math.modf(num)
        # Si la parte decimal es 0 es un número entero
        if parte_decimal == 0:
            # Hago la conversión a número entero a fines de eliminar el ".0"
            num = int(num)
        lista.append(num)
        x += 1        
# Al tener los números enteros y flotantes en la lista, uso la función sorted
# para ordenar los elementos de menor a mayor e imprimo
print("Lista ordenada de los 5 números ingresados: ", sorted(lista))

    
