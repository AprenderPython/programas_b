## Programa que imprime las tablas de multiplicar del 1 al 12 
## Creado por @keito99 para #Python y #Almacen de programas
##
##
###########################################################
while True:
	try:
		nummax=int(input("Introduce el limite de tablas a imprimir:"))
		break
	except:
		print ("El número introducido no es un entero")

## Dirty Fix for range function from 0 to n-1
nummax=(nummax+1)
for num in range (1, nummax ):
	print ("#######################")
	print ("Imprimo la tabla del:",num)
	print ("#######################")
	for x in range (1, 13 ):
		resultado=(num*x)
		print (num,"x",x,"=",resultado )