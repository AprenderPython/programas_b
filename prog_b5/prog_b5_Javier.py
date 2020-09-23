# w38_tabla_multiplicar_javier.py


print("Mostrar tablas de multiplicar")
print("-----------------------------")
print("")


profundidad = 12
paso = True

# pedimos el dato
while paso == True:
    try:
        tablas = int(input("¿Cuantas tablas quieres mostar? "))
    except ValueError:
        print("Error: No es un número. Intentalo otra vez. ", end="")
        paso = True
    else:
        paso = False

print("")

# desarrollamos las tablas
for x in range(tablas):
    x +=1
    for i in range(profundidad):
        i += 1
        print(f'{x:>2} x {i*1:>2} = {i*x:>4}')

    print("")
