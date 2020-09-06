## Programa python para ordenar 5 # introducidos
## Permite numeros con decimales.
## Controla el tipo de caracteres validos
## tg python - week-36
## Usuario @keito99
## No es necesario uso de librerias externas

## Declaro la lista para almacenar
lnum=[]
numero=float(0)
## Solicito los numeros y valido la entrada.
for x in range(5):
    while (type(numero) != "float"):
        try:
            numero=float(input("Introduce un número:"))
            if ( numero % 1 == 0):
                numero=int(numero)
            break
        except ValueError:
            print("Has introducido un caracter no valido.")
    lnum.append(numero)

## Ahora ordenamos la lista e imprimimos
lnum.sort()
print ("La lista ordenada es:", lnum)