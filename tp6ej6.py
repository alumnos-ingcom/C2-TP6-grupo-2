################
# GRUPO 2
#Ejercicio 6- Etiquetas HTML
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def hace_etiqueta(contenido, etiqueta):
    return '<%s>%s</%s>' %(etiqueta, contenido, etiqueta)
    
  
def hace_comenta(contenido):
    return '<!-- %s -->' %(contenido) 
    

def crear_archivo(nombre, contenido):
    archivo = open('%s.html'%(nombre), 'w')
    archivo.write(contenido)
    archivo.close()
  
    
def abrir_archivo(nombre):
    archivo = open('%s.html'%(nombre), 'r')
    print(archivo.read())
    archivo.close()
    
def principal():
    
    nombre =  str(input("Ingrese el nombre del archivo: "))
    encabezado = hace_etiqueta('Hola HTML', 'h1')
    parrafo = hace_etiqueta('Párrafo', 'p')
    comenta = hace_comenta('Probando comentario')
    estructura = '<html>\n<body>\n%s\n%s\n%s\n</body>\n</html>' %(encabezado, parrafo, comenta)
  
    crear_archivo(nombre, estructura)
    abrir_archivo(nombre)
    

if __name__ == "__main__":
    principal()

