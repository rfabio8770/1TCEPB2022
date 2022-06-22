def identificacion():
    print("Ricardo Fabio")

# DECLARACION DE VARIABLES
nombre:str
edad: int
sexo: int
ec: int

identificacion()
nombre = input("ingrese su nombre ")
edad = int(input("ingrese su edad "))
sexo = int(input("ingrese su sexo 1 masc 2 fem"))
ec = int(input("ingrese su estado civil 1 soltero 2 casado 3 divorciado"))
if sexo == 1 and ec == 2:
    print(nombre, " es un hombre casado")
if sexo == 2:
    print(nombre, " es una mujer")
    print(nombre, " tiene ", edad, " años")
    print(ec," es su estado civil")
