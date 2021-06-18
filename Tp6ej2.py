################
# GRUPO 2
# TP 6 Ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import Tp6ej1 as anagramas

def procesar_archivo(nombre):
    #with open('%s'%(nombre),encoding='UTF-8') as archivo:
    #    lineas = [line.rstrip() for line in archivo]
    with open('%s'%(nombre),encoding='UTF-8') as archivo:
        lineas = archivo.read().splitlines()
    archivo.close()
    return lineas
    
def separar_palabras(palabras_juntas):
    palabra_actual= 1
    palabra1 = list()
    palabra2 = list()
    for i in palabras_juntas:
        if i == "–":
            palabra_actual=2
        else:
            if palabra_actual == 1:
                palabra1.append(i)
            else:
                palabra2.append(i)
    return (palabra1,palabra2)


def principal():
    lista_palabras = procesar_archivo('anagramas.txt')
    for i in lista_palabras:
        palabras = separar_palabras(i)
        palabra1 = ''.join(palabras[0])
        palabra2 = ''.join(palabras[1])
        son_anagramas = anagramas.anagrama(palabra1,palabra2)
        if son_anagramas:
            print(f"{palabra1} y {palabra2} son anagramas")
        else:
            print(f"{palabra1} y {palabra2} NO son anagramas")

if __name__ == "__main__":
    principal()

