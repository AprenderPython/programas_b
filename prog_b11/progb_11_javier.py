# /
"""
progb_11_javier.py


Requerimientos:
°Imprimir en pantalla numero de lineas del archivo de texto
°Imprimir el nombre del archivo antes.
°Mostrar con algo de estetica el resultado.



"""




from tkinter import filedialog as FileDialog
import os
import pathlib
import docx

def test(): 
    fichero = FileDialog.askopenfilename(title="Abrir un fichero SOLO .txt, doc, docx",filetypes = (("Ficheros txt","*.txt"),("Ficheros docx","*.docx"),("Ficeros rtf", "*.rtf"),("all files","*.*")))
    #print(fichero)
    return fichero


os.system('clear')


paso = True
nombre = ''
fichero =''


# pedimos fichero
fichero = test()

# separamos nombre y ruta
fichero = pathlib.PurePosixPath(fichero)

print('-' * len((fichero.name)))
print(fichero.name)
print('-' * len((fichero.name)))
print(f'Nombre:\t\t{fichero.name}')
print(f'Extensión:\t{fichero.suffix}')
print(f'Path:\t\t{fichero}')
print("")


# abrimos fichero
if fichero.suffix == '.txt':
    print("Es un fichero de texto plano.")
    lectura = open(fichero, 'r')
    contenido = lectura.readlines()
    lectura.close()
    print(f'El fichero tiene {len(contenido)} líneas.')


if fichero.suffix == '.docx':
    print("Es un fichero de MS Word, del tipo DOCX.")
    doc = docx.Document(fichero)
    contenido = doc.paragraphs
    print(f'El fichero tiene {len(contenido)} líneas.')


if fichero.suffix == '.rtf':
    print("Es un fichero de Rich Text Format (RTF).")
    lectura = open(fichero, 'r')
    contenido = lectura.readlines()
    lectura.close()
    print(f'El fichero tiene {len(contenido)} líneas.')


print("")


