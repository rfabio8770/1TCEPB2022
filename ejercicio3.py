def identificacion():
    print("Ricardo Fabio")

# DECLARACION DE VARIABLES
a: int # lado del triangulo
b: int # lado del triangulo
c: int # lado del triangulo

identificacion()
a = int(input("ingrese el primer numero "))
b= int(input("ingrese el segundo numero "))
c= int(input("ingrese el tercer numero "))
if (a + b >= c) and (a + c >= b) and(b + c >= a):    
    print("Los numeros forman un triángulo")
else:
    print("Los numeros no forman un triángulo")	