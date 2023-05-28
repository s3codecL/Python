def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def operaciones(a,b):
    suma = sumar(a,b)
    resta = restar(a,b)
    mult = multiplicar(a,b)
    div = dividir(a,b)
    resultado = {"Suma": suma, "Resta": resta, "Multiplicación": mult, "División": div}
    return resultado

print(operaciones(4,2)) #{"Suma": 6, "Resta": 2, "Multiplicación": 8, "División": 2}