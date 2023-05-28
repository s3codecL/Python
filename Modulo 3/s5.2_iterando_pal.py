palabra = "paralelepípedo"
consonantes = ""
for i in range(len(palabra)):
    if palabra[i] not in "aeiouáéíóú":
        consonantes += palabra[i]
        print(palabra[i] + ": posición", i)
        
print("Consonantes: ", consonantes)