################
# GRUPO 2
# TP 6 Ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def reemplazar_caracteres(cadena,caracter_busca,reemplazo):
    cadena_reemplazada = list()
    for i in range(len(cadena)):
        cadena_reemplazada.append(cadena[i])
        if cadena[i] == caracter_busca:
            cadena_reemplazada[i]=reemplazo
    return ''.join(cadena_reemplazada)

def anagrama(palabra1,palabra2):
    encontrados1 = 0
    encontrados2 = 0
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    palabra1 = reemplazar_caracteres(palabra1," ","")
    palabra2 = reemplazar_caracteres(palabra2," ","")
    for i in palabra1:
        if i in palabra2:
            encontrados1 = encontrados1 + 1
    for i in palabra2:
        if i in palabra1:
            encontrados2 = encontrados2 + 1
    return encontrados1 == encontrados2 and encontrados1 == len(palabra1) and encontrados2 == len(palabra2)

def principal():
    """Toda la interacción con el usuario va acá"""
    es_anagrama=anagrama('marta sergio','trama riesgo')
    print(es_anagrama)
    pass

if __name__ == "__main__":
    principal()

