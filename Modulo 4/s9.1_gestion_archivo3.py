# 1 crear un archivo si no existe y reflejar un mensaje si ya existe
nombre_archivo = "informacion.dat"

try:
    # Intenta abrir el archivo en modo lectura para verificar si existe
    with open(nombre_archivo, "r") as archivo:
        # Si el archivo existe, muestra un mensaje
        print("El archivo ya ha sido creado previamente.")
except FileNotFoundError:
    # Si el archivo no existe, lo crea y escribe los datos de información
    with open(nombre_archivo, "w") as archivo:
        datos_informacion = [
            "Datos de información en la línea 1",
            "Datos de información en la línea 2",
            "Datos de información en la línea 3",
            "Datos de información en la línea 4",
            "Datos de información en la línea 5"
        ]
        archivo.write("\n".join(datos_informacion))
        print("El archivo se ha creado exitosamente.")

# 2 lectura archivo creado previamente
def lectura_archivo():
    archivo = open("informacion.dat", "r")
    contenido = archivo.read()
    archivo.close()
    print(contenido)

lectura_archivo()

# 3 agregar datos a un archivo
def agregar_contenido_archivo():
    nombre_archivo = "informacion.dat"

    agregar_contenido = """Hola Mundo
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada"""

    try:
        with open(nombre_archivo, "a") as archivo:
            archivo.write("\n" + agregar_contenido)
        print("Contenido agregado correctamente al archivo.")
    except IOError:
        print("Error al abrir o escribir en el archivo.")

