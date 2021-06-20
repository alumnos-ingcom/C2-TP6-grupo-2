################
# GRUPO 2
#Ejercicio 6- Descodificador
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp5ej8 import des_cifrado_cesar
from Tp6ej2 import procesar_archivo

def decodificar_archivo(nombre, rotacion):

    lineas = procesar_archivo(nombre)
   
    for i in range(len(lineas)):
        lineas[i] = des_cifrado_cesar(''.join(lineas[i]), rotacion)
    
    archivonuevo = open('%s.decode'%(nombre), 'w')
    archivonuevo.writelines(lineas)
    archivonuevo.close()

    return lineas
    


def principal():
   
    nombre = str(input("Ingrese el nombre del archivo a descodificar(con extension.cesar)"))
    rotaciones = int(input("Ingrese la cantidad de rotaciones que necesita para decodificarlo"))
    decodificado = decodificar_archivo(nombre, rotaciones)
    print("el archivo quedo guardado con el .decode al final, y su resultado sera:")
    for i in decodificado:
        print(i)
    

if __name__ == "__main__":
    principal()
