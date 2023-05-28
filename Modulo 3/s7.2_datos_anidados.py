lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for sl in lista:
    if sl[0] == 0:
        continue  # omite la impresión de la sublista (sl) completa si el primer elemento es 0
    for elemento in sl:
        if elemento == 0:
            continue  # omite los elementos individuales si son 0
        print(elemento)  # imprime solo los elementos que no sean 0


for y,x in enumerate(lista):
    if 0 == x[0]:
        continue
    elif 0 in x:
        x.pop(x.index(0))
        
    print(x)