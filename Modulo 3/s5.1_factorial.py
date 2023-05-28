num = input("Ingrese numero: ") # número del que queremos obtener factorial
factorial = 1 # variable para almacenar el resultado

for i in range(1, int(num)+1):
    factorial *= i

print(factorial) # imprime el resultado del factorial