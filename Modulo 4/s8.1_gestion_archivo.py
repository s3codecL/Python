#crear un archivo si no existe y reflejar un mensaje si ya existe
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

