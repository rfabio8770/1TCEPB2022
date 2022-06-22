def identificacion():
    print("Ricardo Fabio")

#DECLARACION DE VARIABLES
n: int # cantidad de datos
num: int # valor de la lista
c: int # contador
mayor: int # mayor valor

identificacion()
c = 0
n = int(input("ingrese la cantidad de datos "))
while c < n:
    num = int(input("ingrese un numero "))
    c = c + 1
    if c == 1:
        mayor = num
    if num > mayor:
        mayor = num
print("el mayor valor es ", mayor)
