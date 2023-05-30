"""
Diagrama de clases para persona y estudiante:
- Clase Persona: 
    - Atributos: número de identificación, nombre, apellido.
    - Métodos: 
    - ObtenerDatos(): retorna los atributos de la persona.
- Clase Estudiante:
    - Atributos: número de identificación, nombre, apellido, código del alumno, matrícula.
    - Métodos: 
    - ObtenerDatos(): retorna los atributos del estudiante.
"""
# Clase Persona
class Persona:
    def __init__(self, identificacion, nombre, apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    
    def ObtenerDatos(self):
        return {"identificacion": self.identificacion, "nombre": self.nombre, "apellido": self.apellido}

# Clase Estudiante
class Estudiante(Persona):
    def __init__(self, identificacion, nombre, apellido, codigo, matricula):
            super().__init__(identificacion, nombre, apellido)
            self.codigo = codigo
            self.matricula = matricula
    
    def ObtenerDatos(self):
        datos_persona = super().ObtenerDatos()
        datos_persona.update({"codigo": self.codigo, "matricula": self.matricula})
        return datos_persona
    
# Ejemplo
persona1 = Persona(123456, "Elon", "Musk")
print(persona1.ObtenerDatos()) 
# salida: {"identificacion": 123456, "nombre": "Elon", "apellido": "Musk"}

estudiante1 = Estudiante(789012, "Bill", "Gates", "54321", 123)
print(estudiante1.ObtenerDatos()) 
# salida: {"identificacion": 789012, "nombre": "Bill", "apellido": "Gates", "codigo": "54321", "matricula": 123}