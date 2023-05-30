class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario

trabajador = Trabajador("Brendan", "Eich", 2005, "Ingeniería de software", "IS", 20000)

print(trabajador.__dict__)

print("Es trabajador instancia de Persona:", isinstance(trabajador, Persona))
print("Es trabajador instancia de Departamento:", isinstance(trabajador, Departamento))
print("Es trabajador instancia de Trabajador:", isinstance(trabajador, Trabajador))
