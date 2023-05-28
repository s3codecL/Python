def suma_resta(num_list):
    resultado_suma = sum(num_list)
    resultado_resta = num_list[0] - num_list[1] - num_list[2]
    return (resultado_suma, resultado_resta)

numeros = [3, 5, 2]
resultado = suma_resta(numeros)
print(resultado)