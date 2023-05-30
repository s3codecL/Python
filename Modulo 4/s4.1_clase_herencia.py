# Definir la clase
class Libro:
    def __init__(self, autor, titulo, ann_de_publicacion=None):
        self.autor = autor
        self.titulo = titulo
        self.ann_de_publicacion = ann_de_publicacion

# Crear las dos instancias
libro_1 = Libro('Dan Brown', 'Infierno')
libro_2 = Libro('Dan Brown', 'El Código Da Vinci', 2003)

# Asignar atributos de instancia a cada objeto
libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Infierno'
libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Código Da Vinci'
libro_2.ann_de_publicacion = 2003

# Imprimir el valor del atributo __dict__ de cada objeto
print(libro_1.__dict__)
print(libro_2.__dict__)
# Salida
# {'autor': 'Dan Brown', 'titulo': 'Infierno'}
# {'autor': 'Dan Brown', 'titulo': 'El Código Da Vinci', 'ann_de_publicacion': 2003}