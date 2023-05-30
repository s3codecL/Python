#clase de excepción personalizada "RangoSalarioError"
class RangoSalarioError(Exception):
    def __init__(self, salario):
        mensaje = "{} -> Salario no está definido en el rango (1000 a 2000)".format(salario)
        super().__init__(mensaje)

#solicitar el valor del salario al usuario y manejar la excepción
while True:
    try:
        salario = int(input("Ingrese el salario: "))
        if salario < 1000 or salario > 2000:
            raise RangoSalarioError(salario)
        break
    except RangoSalarioError as rse:
        print(rse)
    except ValueError:
        print("Debe ingresar un número válido.")

print("El salario ingresado es:", salario)

# ejemplo
#Ingrese el salario: 5000
#5000 -> Salario no está definido en el rango (1000 a 2000)
#Ingrese el salario: 1500
#El salario ingresado es: 1500
