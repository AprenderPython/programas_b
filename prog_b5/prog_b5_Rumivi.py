
print('Alias de telegram: Rumivi')

nInsertado = int (input('Inserte un numero positivo'))

if nInsertado > 0:

	#Bucle para el primer numero de la tabla, del 1 al numero insertado
	for i in range (1,nInsertado+1):

		#Bucle para que el segundo numero acabe en el 12
		for n in range (1,13):

			print(f'{i} x {n} = {i*n}')


else:
	print('El numero no es positivo, pruebe de nuevo')
