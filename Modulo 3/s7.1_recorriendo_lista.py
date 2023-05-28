lista_numeros = [2, 5, 0, 7, 8, 11, 12, -3, 1, 6]

for n in lista_numeros:
    if n == 0:
        print("El número es cero")
    elif n % 2 == 0:
        print("El número", n, "es par")
    else:
        print("El número", n, "es impar")