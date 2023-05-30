class Animal:
    
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
def main():
    caballo = Animal("Zeus", "Pura sangre", "5 años", "450 kg")
    leon = Animal("Boulder", "Atlas","10 años", "130 kg")

    print("El caballo", caballo.nombre, "es de raza", caballo.raza, "y tiene", caballo.edad, "y pesa", caballo.peso)
    print("El león", leon.nombre, "es de raza", leon.raza, "y tiene", leon.edad, "y pesa", leon.peso)

main()
