# usuario: Javier
# semana 36. proyecto básico


lista =[]

# preguntamos, chequemos y añadimos a la lista si es un número
print("Introduce 5 números enteros o decimales (con punto .):")

for i in range(5):
    paso = True
    print(f"Número {i+1}: ", end="")
    while paso == True:
        try:
            numero = float(input())
        except ValueError:
            print("Error: No es un número. Intentalo otra vez: ", end="")
            paso = True
        else:
            lista.append(numero)
            paso = False

# ordenamos la lista
lista = sorted(lista)

# mostramos resultados, los 4 primeros llevan una coma despues
print("Los 5 números ordenados son: ")
for i in range(4):
    if (abs(lista[i]) - abs(int(lista[i]))) == 0:
        print(f"{int(lista[i])}, ", end="")
    else:
        print(f"{lista[i]}, ", end="")
# pero el 5 no
i = 4
if (abs(lista[i]) - abs(int(lista[i]))) == 0:
    print(f"{int(lista[i])} ")
else:
    print(f"{lista[i]} ")



