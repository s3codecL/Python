lista_nombres = ['Harry Houdini', 'David Blaine', 'Teller', 'Newton', 'Hawking', 'Einstein', 'Gandhi', 'Shakespeare', 'Mozart']

magos = []
cientificos = [] 
otros = []

def hacer_grandioso():
    global magos
    magos = ['El gran ' + nombre for nombre in magos]

def imprimir_nombres():
    print('Magos: ', magos)
    print('Cientificos: ', cientificos)
    print('Otros: ', otros)

for nombre in lista_nombres: 
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

print('Lista de nombres completa:')
imprimir_nombres()

hacer_grandioso()

print('Magos grandiosos:')
imprimir_nombres()

print('Cientificos:')
imprimir_nombres()

print('Otros:')
imprimir_nombres()
