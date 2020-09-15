
# Create by: @BlackShinigami00
# Follow us in http://t.me/aprenderpython

numeros = []

cont = 0

def orden():
    numeros.sort() # Funcion que permite ordenar la lista
    return numeros

print("Ingresa numeros para conformar tu lista de 5 numeros")

while cont < 5:

    cont += 1

    n = input(">>> ")
    try:
        if type(n) == str: # se separanlos strings de los enteros y los flotanntes
            n = float(n)
            if int(n) == n: # se el flotante es  = 0 se convierte a entero
                n = int(n)

        numeros.append(n)

    except ValueError:
        '''
        Si el usuario ingresa un string se volvera a pedir el numero
        y retrocede el contador del bucle para asegurar que la lista siempre sea de
        5 numeros
        '''
        print("Numero invalido")
        print("Vuelve a introducir el numero")
        cont -= 1




print("Esta es la lista original -> ",numeros)
print("")
print("Esta es la lista ordenada -> ",orden())

