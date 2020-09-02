## Alias: @xXxAIHDxXx
## No se usaron librerias externas

## Codigo:

## Primero se solicita el numero a evaluar
n = int(float(input("Por favor, indique el numero a evaluar(se ignorara la parte decimal): ")))

## Despues, se comprueba si 2 es factor del numero en cuestion, determinando si es par o impar y posteriormente mostrando en la pantalla el resultado
if n%2 == 0 :
    print("El numero " + str(n) + " es par")
else:
    print("El numero " + str(n) + " es impar")