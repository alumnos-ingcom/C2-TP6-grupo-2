################
#Grupo 2
#Ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# COPIADORA

def copiadora(archivo_entrada, archivo_salida):
    archivo_entrada = open('archivo_entrada','r',encoding = 'UTF-8')
    texto = archivo_entrada.read()
    archivo_entrada.close()
    
    archivo_salida = open('archivo_salida', 'w')
    archivo_salida.write(texto)
    
def prueba():  
    archivo_e = input("Ingrese el nombre del archivo a copiar: ")
    archivo_s = input("Ingrese el archivo de destino: ")

    copiadora(archivo_e, archivo_s)

if __name__ == "__main__":
    prueba()
    

    
    
    
    
    
