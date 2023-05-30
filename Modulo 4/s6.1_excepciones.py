suma = 3000
contador = 0

try:
    resultado = suma / contador
    print(resultado)
except ZeroDivisionError:
    print('División por cero.')
# salida: División por cero

suma = 5000
contador = 5

try:
    resultado = suma / contador
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("División por cero.")
# salida: El resultado de la división es: 1000.0