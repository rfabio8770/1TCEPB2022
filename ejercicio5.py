"""
5.	Leer el número de un empleado, el precio básico por hora y el número de horas trabajadas 
durante una semana.  Calcular el salario neto, 
teniendo en cuenta si el número de horas trabajadas durante una semana es mayor de 48, 
esas horas extras valen 35% más del precio básico.  
Imprimir el número de empleado, el número de horas trabajadas y el salario neto
"""

def identificacion():
    print("Ricardo Fabio")

# DECLARACION DE VARIABLES
num_empleado: int
precio_basico: int
num_horas: int
salario_neto: int
horas_extras: int

identificacion()
num_empleado = int(input("ingrese el numero de empleado "))
precio_basico = int(input("ingrese el precio basico por hora "))
num_horas = int(input("ingrese el numero de horas trabajadas "))
if num_horas > 48:
    horas_extras = num_horas - 48
    salario_neto = (precio_basico * 48) + (precio_basico * horas_extras * 135 // 100)
else:
    salario_neto = precio_basico * num_horas
print("El salario neto del empleado ", num_empleado, " es ", salario_neto)
print("El numero de horas trabajadas es ", num_horas)	