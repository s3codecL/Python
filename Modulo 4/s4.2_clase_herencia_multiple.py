class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def movimiento(self):
        print(f"{self.nombre} está caminando.")

class Maratonista(Persona):
    def movimiento(self):
        print(f"{self.nombre} está trotando.")

class Ciclista(Persona):
    def movimiento(self):
        print(f"{self.nombre} está rodando.")

# Ejemplo:
persona = Persona("Juan")
maratonista = Maratonista("Pedro")
ciclista = Ciclista("Ana")

persona.movimiento()
maratonista.movimiento()
ciclista.movimiento()

# Salida
# "Juan está caminando."
# "Pedro está trotando."
# "Ana está rodando."