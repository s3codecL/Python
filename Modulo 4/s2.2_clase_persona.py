class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellidos(self):
        return self.apellidos

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_estatura(self):
        return self.estatura

    def set_estatura(self, estatura):
        self.estatura = estatura

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

# Crear las dos personas
Persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
Persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

# Modificar la edad de la Persona_1 y el apellido de la Persona_2
Persona_1.set_edad(21)
Persona_2.set_apellidos("Santiago")

# Mostrar los datos actualizados de ambas personas
print("La edad de {} {} es {} años".format(Persona_1.get_nombre(), Persona_1.get_apellidos(), Persona_1.get_edad()))
print("El apellido de {} es {}".format(Persona_2.get_nombre(), Persona_2.get_apellidos()))