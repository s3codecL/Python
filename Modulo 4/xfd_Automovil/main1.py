from vehiculo import Automovil

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