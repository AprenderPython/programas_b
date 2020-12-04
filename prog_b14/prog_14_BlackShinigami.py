import sys

"""
Cada Funcion Es para cambiar el color y formato al texto ASCII segun su nombre
El scrip funciona mediante el codigo ANSI
"""


def tachado(): 
    try:
        color = int(input("Escoge el color que deseas utilizar\n1-azul\n2-rojo\n3-verde\n4-morado\n5-blanco\n>>> "))
    except ValueError:
        print("Error opcion incorrecta")
        sys.exit()
        
    if color > 5:
        print("Error, la opcion escogida no existe")
        sys.exit()

    text = input("Escribe lo que deseas imprimir\n>>> ")
    if color == 1:
        print(chr(27)+"[7;34m"+text)
    
    elif color == 2:
        print(chr(27)+"[7;31m"+text)

    elif color == 3:
        print(chr(27)+"[7;32m"+text)

    elif color == 4:
        print(chr(27)+"[7;35m"+text)

    elif color == 5:
        print(chr(27)+"[7;37m"+text)

def cursiva():
    try:
        color = int(input("Escoge el color que deseas utilizar\n1-azul\n2-rojo\n3-verde\n4-morado\n5-blanco\n>>> "))
    except ValueError:
        print("Error opcion incorrecta")
        sys.exit()

    if color > 5:
        print("Error, la opcion escogida no existe")
        sys.exit()
    
    text = input("Escribe lo que deseas imprimir\n>>> ")

    if color == 1:
        print(chr(27)+"[3;34m"+text)
    
    elif color == 2:
        print(chr(27)+"[3;31m"+text)

    elif color == 3:
        print(chr(27)+"[3;32m"+text)

    elif color == 4:
        print(chr(27)+"[3;35m"+text)

    elif color == 5:
        print(chr(27)+"[3;37m"+text)

def negrita():

    try:
        color = int(input("Escoge el color que deseas utilizar\n1-azul\n2-rojo\n3-verde\n4-morado\n5-blanco\n>>> "))
    except ValueError:
        print("Error opcion incorrecta")
        sys.exit()

    if color > 5:
        print("Error, la opcion escogida no existe")
        sys.exit()
    
    text = input("Escribe lo que deseas imprimir\n>>> ")

   
    if color == 1:
        print(chr(27)+"[1;34m"+text)
    
    elif color == 2:
        print(chr(27)+"[1;31m"+text)

    elif color == 3:
        print(chr(27)+"[1;32m"+text)

    elif color == 4:
        print(chr(27)+"[1;35m"+text)

    elif color == 5:
        print(chr(27)+"[1;37m"+text)


def subrayado():

    try:
       color = int(input("Escoge el color que deseas utilizar\n1-azul\n2-rojo\n3-verde\n4-morado\n5-blanco\n>>> "))
    except ValueError:
        print("Error opcion incorrecta")
        sys.exit()

    if color > 5:
        print("Error, la opcion escogida no existe")
        sys.exit()
    
    text = input("Escribe lo que deseas imprimir\n>>> ")

    if color == 1:
        print(chr(27)+"[4;34m"+text)
    
    elif color == 2:
        print(chr(27)+"[4;31m"+text)

    elif color == 3:
        print(chr(27)+"[4;32m"+text)

    elif color == 4:
        print(chr(27)+"[4;35m"+text)

    elif color == 5:
        print(chr(27)+"[4;37m"+text)

    
def debil():
    
    try:
        color = int(input("Escoge el color que deseas utilizar\n1-azul\n2-rojo\n3-verde\n4-morado\n5-blanco\n>>> "))
    except ValueError:
        print("Error opcion incorrecta")
        sys.exit()

    if color > 5:
        print("Error, la opcion escogida no existe")
        sys.exit()
    
    text = input("Escribe lo que deseas imprimir\n>>> ")

    if color == 1:
        print(chr(27)+"[2;34m"+text)
    
    elif color == 2:
        print(chr(27)+"[2;31m"+text)

    elif color == 3:
        print(chr(27)+"[2;32m"+text)

    elif color == 4:
        print(chr(27)+"[2;35m"+text)

    elif color == 5:
        print(chr(27)+"[2;37m"+text)
  

print("==================================================================")
print("=            Prog_14_BlackShinigami                              =")
print("=          Dar formato a texto ASCII                             =")
print("==================================================================")
    
print("Selecciona el estilo que quieres usar")

print(chr(27)+"[7;37m 1-Tachado"+chr(27)+"[0;37m")

print(chr(27)+"[3;37m 2-Cursiva"+chr(27)+"[0;37m")

print(chr(27)+"[1;37m 3-Negrita"+chr(27)+"[0;37m")

print(chr(27)+"[4;37m 4-Subrayado"+chr(27)+"[0;37m")

print(chr(27)+"[2;37m 5-Debil"+chr(27)+"[0;37m")

start = input(">>> ")

if start == "1":
    tachado()

elif start == "2":
    cursiva()

elif start == "3":
    negrita()

elif start == "4":
    subrayado()

elif start == "5":
    debil()
else:
    print("Error, la opcion seleccionada no existe")



