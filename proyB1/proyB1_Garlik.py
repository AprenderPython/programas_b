#Create by: Garlik
ciclo = 'si'
while ciclo:
    def par_impar(num):
        return num%2==0
    num = int(input("Ingresa un numero entero para comprobar si es par o impar.\n "))
    if num < 0:
        print('{num} es un numero negativo')
        
    if(par_impar(num)):
        print(f"El numero {num} es par.")
    else:
        print(f"El numero {num} es impar. ")        
    
    resp = input('Si desea continuar ingrese "si" o "no". \n')

    if resp == 'si':
        print('comenzemos de nuevo.')
    elif resp == 'no':
        break
    else:
        print('Error!')
        break
print('Gracias por su colaboracion.')        

    
    