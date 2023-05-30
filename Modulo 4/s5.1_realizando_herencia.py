class A:
    def __init__(self):
        print("Pertenezco a la clase A")

    def metodo_a(self):
        print("Método heredado de A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")


class C(B,A):
    def __init__(self):
        super().__init__()  # llamada a los constructores de A y B
        print("Clase C")

    def metodo_c(self):
        print("Método es de C")

obj_c = C()
obj_c.metodo_a()
obj_c.metodo_b()
obj_c.metodo_c()


