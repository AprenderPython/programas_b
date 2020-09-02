#Codigo PAR O IMPAR - Sin librerias externas 
print("Bienvenido a los numeros PARES e IMPARES") #Titulo del programa
print("Si deseas salir escribe 'exit'")
print("Created by ~Outis") #Autor del codigo

print("Introduce tu nombre: ") #Identidad del usuario
name = input() #codigo para entrada de datos 

respuesta = "exit" #variable trampa para el bucle
num = 0 #Variable para la condición, neutro

while respuesta == "exit": #Bucle: Hasta que no salga en el programa "exit" no se detiene el bucle
	num = int(input("Introduce un numero entero: ")) #Instruccion para ingresar el dato en este caso es un numero entero

	if num%2 == 0:
		print("El numero ", num, " es PAR") #La variable num le sacamos el residuo "%" de 2 para comparar si el numero del usuario es par y asi imprimir el valor 

	else:
		print("El numero ", num, " es IMPAR") #Si no cumple en sacar el residuo "%" de 2 nos va a botar el resultado de IMPAR

input() #Entrada de datos 

