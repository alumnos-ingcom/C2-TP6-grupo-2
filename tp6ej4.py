
################
# Grupo 2
#Ejercicio 4
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej8 import cifrado_cesar

def codificador_archivo(archivo_entrada, texto_nuevo = None, accion = None):

    if accion == 'w' and texto_nuevo != None:
            
        archivo_entrada = open(archivo_entrada+'.cesar', "w")
        archivo_entrada.write(texto_nuevo)
        archivo_entrada.close()

    else:

        try:

            archivo_entrada = open(archivo_entrada, encoding='utf8')
            texto = archivo_entrada.read()
            archivo_entrada.close()

            return texto

        except FileNotFoundError:

            raise FileNotFoundError('No se encuentra el archivo!', archivo_entrada)


def prueba():
    
    a_entrada = input("Ingrese el nombre del archivo de entrada:  ")
    cant_rotacion = input("Ingrese la cantidad de rotaciones que desea realizar: ")
    
    texto = codificador_archivo(a_entrada)
    
    texto_codificado = cifrado_cesar(texto, cant_rotacion)

    a_salida = codificador_archivo(a_entrada, texto_codificado, "w")

if __name__ == "__main__":
    prueba()