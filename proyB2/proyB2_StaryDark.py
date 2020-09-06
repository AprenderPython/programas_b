#creado por: StaryDark Telegram:@dark_zly
print("Escribe 5 numeros y te los imprimire ordenados ascendentemente")

def ordenar(nums):#Guardara los numeros en una lista segun su tipo y los ordenara ascendentemente
    for num in nums:#determinar numeros enteros y decimales y añadirlos a la lista result
        if "." in num:
            result.append(float(num))
        else:
            result.append(int(num))
    if len(result) == 5:#si se introdujeron 5 numeros, imprimirlos en orden ascendente
        print (str(sorted(result))[1:-1])
    else:
        print("Solo escribe 5 numeros...")

while True: #bucle infinito hasta que se introduzcan 5 numeros
    nums = list(map(str, input("\nIntroduce 5 numeros separados por coma: ").split(",")))
    #separar lo introducido por el usuario por cada coma, y con ello hacer una lista
    result = [] #crear y resetear la variable result
    try:
        ordenar(nums)
    except ValueError: #error por si se escriben caracteres no numericos, a exepcion del .
        print("Solo se permiten numeros...")
        continue
    if len(nums) == 5:#terminar el bucle si se introdujeron 5 numeros
        break