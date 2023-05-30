while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Ingrese su edad nuevamente")

if edad >= 18:
    print("Es un adulto")
else:
    print("No es un adulto")

#Ejemplo:

#Ingrese su edad: 25
#Es un adulto

#Ingrese su edad: 17
#No es un adulto

#Ingrese su edad: "abc"
#Ingrese su edad nuevamente: 20
#Es un adulto