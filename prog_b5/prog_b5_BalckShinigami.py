print('===========================================================')
print('= Generador de tablas de multiplicar                      =')
print('=       Escrito en Python 3 por BlackShinigami            =')
print('=           Telegram BlackShinigami00                     =')
print('===========================================================\n')
print('Para usar la opcion por defecto introduce el numero 0')
print('Las tablas se generaran entonces desde la tabla del 1 hasta la tabla del 12\n')

while True:
    
    try:
        num = int(input('Ingresa hasta que numero se generaran las tablas de multiplicacion:\n >>> '))
        break

    except ValueError:
        print('Solo numeros enteros por favor vuelve a intentar')

if num == 0:
    for i in range(1,13):
        print('\nTabla del',i,':')
        print('_____________')

        for j in range(13):

            print(i,'x',j,'=',i*j)

else:

     for i in range(1,num+1):
        print('\nTabla del',i,':')
        print('_____________')

        for j in range(13):

            print(i,'x',j,'=',i)

print('\nTablas generadas con exito!!!')
