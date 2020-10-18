print("usuario: M1nc#0")

#inicializmos la variable num
num = 0

#declarmos como entrada donde nos pide teclar x numero
num = int(input("Indique un número: "))

#con la comdicion if dentro de ella hara una division entre 2 si el residuo es 0 entnces procede a imprimir es par caso contrario iria a un else
if (num % 2) == 0:
  print(num, " es par")
else:
  print(num, " es impar")