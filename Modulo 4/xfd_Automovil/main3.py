# Parte 3
from vehiculo import Particular, Carga, Bicicleta, Motocicleta, Vehiculo, Automovil

nombres_clases = {
    Vehiculo: "Vehículo",
    Automovil: "Automovil",
    Particular: "Particular",
    Carga: "Carga",
    Bicicleta: "Bicicleta",
    Motocicleta: "Motocicleta"
}


def guardar_datos_csv(vehiculos):
    try:
        with open('vehiculos.csv', 'w') as archivo:
            for vehiculo in vehiculos:
                datos = [str(type(vehiculo)), str(vehiculo.__dict__)]
                datos = ",".join(datos)
                archivo.write(datos + "\n")
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo: {str(e)}")


def leer_datos_csv():
    vehiculos = {
        "Particular": [],
        "Carga": [],
        "Bicicleta": [],
        "Motocicleta": []
    }
    try:
        with open('vehiculos.csv', 'r') as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                linea = linea.strip()
                clase, datos = linea.split(",")
                datos = eval(datos)
                clase = clase.replace("<class '", "").replace("'>", "")
                clase = nombres_clases[eval(clase)]
                vehiculo = eval(clase)(**datos)
                vehiculos[clase].append(vehiculo.__dict__)
    except FileNotFoundError:
        print("El archivo vehiculos.csv no existe.")
    except Exception as e:
        print(f"Error al leer los datos del archivo: {str(e)}")
    return vehiculos


# crear instancias
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta(
    "BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# guardar csv
print("\nGuardando datos en archivo vehiculos.csv...")
guardar_datos_csv([particular, carga, bicicleta, motocicleta])
print("Datos guardados correctamente.")

# leer csv
print("\nLeyendo datos desde archivo vehiculos.csv...")
vehiculos_csv = leer_datos_csv()
for clase, lista in vehiculos_csv.items():
    print(f"\nLista de Vehiculos {clase}")
    for vehiculo in lista:
        print(vehiculo)
