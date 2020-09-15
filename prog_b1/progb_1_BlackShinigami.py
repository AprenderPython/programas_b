'''
Escrito por "BlackShinigami"
Analisis de numeros pares
'''

def pares(num):

    par = num % 2

    if par == 0:
        print(f"El numero {num} es par")

    else:
        print(f"El nuemro {num} no es par")

try:
    number  = int(input("Ingresa un numero para revisar si es par >>> "))
    pares(number)
except ValueError:
    print("Error solo se pueden usar numeros enteros")

