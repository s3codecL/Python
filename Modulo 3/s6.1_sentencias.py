num = float(input("Ingrese un número: "))

if num == 0:
    print("El número es cero.")
else:
    if num > 0:
        print("El número es positivo", end="")
    else:
        print("El número es negativo", end="")
    
    if num % 2 == 0:
        print(" y es par.")
    else:
        print(" y es impar.")