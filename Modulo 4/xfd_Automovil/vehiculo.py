# implementamos las clases Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta:
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

# creamos para probar las clases e instancias:
from vehiculo import Automovil

if __name__ == '__main__':

    # Parte 1
    cantidad = int(input("Cuantos Vehiculos desea insertar: "))
    vehiculos = []
    for i in range(cantidad):
        print(f"Datos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = input("Inserte la velocidad en km/h: ")
        cilindrada = input("Inserte el cilindraje en cc: ")
        vehiculo = Automovil(marca, modelo, ruedas, velocidad, cilindrada)
        vehiculos.append(vehiculo)
    print("Imprimiendo por pantalla los Vehículos:")
    for vehiculo in vehiculos:
        print(f"Marca {vehiculo.marca}, Modelo {vehiculo.modelo}, {vehiculo.nro_ruedas} ruedas {vehiculo.velocidad} Km/h, {vehiculo.cilindrada} cc")

    # Parte 2
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
    print(f"Marca {particular.marca}, Modelo {particular.modelo}, {particular.nro_ruedas} ruedas {particular.velocidad} Km/h, {particular.cilindrada} cc Puestos: {particular.nro_puestos}")
    print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.nro_ruedas} ruedas {carga.velocidad} Km/h, {carga.cilindrada} cc Carga: {carga.carga} Kg")
    print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.nro_ruedas} ruedas Tipo: {bicicleta.tipo}")
    print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.nro_ruedas} ruedas Tipo: {motocicleta.tipo} Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")
    print("Verificar la relación que existe de la instancia motocicleta con: Vehículo, Automóvil, Particular, Carga, Bicicleta y Motocicleta.")
    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
    print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

    # Parte 3
    nombres_clases = {
        Vehiculo: "Vehículo",
        Automovil: "Automovil",
        Particular: "Particular",
        Carga: "Carga",
        Bicicleta: "Bicicleta",
        Motocicleta: "Motocicleta"
    }

    def guardar_datos_csv(vehiculos):
        with open('vehiculos.csv', 'w') as archivo:
            for vehiculo in vehiculos:
                datos = [str(type(vehiculo)), str(vehiculo.__dict__)]
                datos = ",".join(datos)
                archivo.write(datos + "\n")

    def leer_datos_csv():
        vehiculos = {
            "Particular": [],
            "Carga": [],
            "Bicicleta": [],
            "Motocicleta": []
        }
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
        return vehiculos

    print("\nGuardando datos en archivo vehiculos.csv...")
    guardar_datos_csv([particular, carga, bicicleta, motocicleta])
    print("Datos guardados correctamente.")
    print("\nLeyendo datos desde archivo vehiculos.csv...")
    vehiculos_csv = leer_datos_csv()
    for clase, lista in vehiculos_csv.items():
        print(f"\nLista de Vehiculos {clase}")
        for vehiculo in lista:
            print(vehiculo)


# ejecutamos el archivo `main.py` y el resultado:

"""
Cuantos Vehiculos desea insertar: 3
Datos del automóvil 1
Inserte la marca del automóvil: Toyota
Inserte el modelo: Yaris
Inserte el número de ruedas: 4
Inserte la velocidad en km/h: 120
Inserte el cilindraje en cc: 800
Datos del automóvil 2
Inserte la marca del automóvil: Fiat
Inserte el modelo: Palio
Inserte el número de ruedas: 4
Inserte la velocidad en km/h: 95
Inserte el cilindraje en cc: 1200
Datos del automóvil 3
Inserte la marca del automóvil: Ford
Inserte el modelo: Fiesta
Inserte el número de ruedas: 4
Inserte la velocidad en km/h: 180
Inserte el cilindraje en cc: 500
"""