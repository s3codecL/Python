class Seleccion:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def concentrarse(self):
        print(f"{self.nombre} {self.apellidos} está concentrado.")
    
    def viajar(self):
        print(f"{self.nombre} {self.apellidos} está viajando.")
    

class Futbolista(Seleccion):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
    
    def jugarPartido(self):
        print(f"{self.nombre} {self.apellidos} está jugando.")
    
    def entrenar(self):
        print(f"{self.nombre} {self.apellidos} está entrenando.")
    

class Entrenador(Seleccion):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacion = idFederacion
    
    def dirigirPartido(self):
        print(f"{self.nombre} {self.apellidos} está dirigiendo el partido.")
    
    def dirigirEntrenamiento(self):
        print(f"{self.nombre} {self.apellidos} está dirigiendo el entrenamiento.")
    

class Masajista(Seleccion):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annosExperiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annosExperiencia = annosExperiencia
    
    def darMasajes(self):
        print(f"{self.nombre} {self.apellidos} está dando masajes.")

# ejemplo
futbolista1 = Futbolista(1, "Sergio", "Ramos", 35, 4, "defensa")
futbolista1.concentrarse()
futbolista1.entrenar()
futbolista1.jugarPartido()

entrenador1 = Entrenador(2, "Luis", "Enrique", 51, "RFEF")
entrenador1.concentrarse()
entrenador1.dirigirEntrenamiento()
entrenador1.dirigirPartido()

masajista1 = Masajista(3, "Alfonso", "Núñez", 35, "Quiromasaje", 10)
masajista1.concentrarse()
masajista1.darMasajes()
masajista1.entrenar()