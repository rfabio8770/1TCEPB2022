"""
Diseñar un algoritmo que permita calcular el monto total correspondiente a una compra de
un artículo determinado del que se adquiere una o más unidades a un determinado precio. El
IVA que se debe aplicar en cada caso es del 10 % si el monto de la compra es menor a 500.000
Gs y en caso contrario 12 %. Además, se debe aplicar un descuento fijo del 1% a todas las
compras sin excepción.
"""


def identificacion():
    print("Ricardo Fabio")

# DECLARACION DE VARIABLES
cp: int # cantidad de producto comprada
pu: int # precio unitario
monto_bruto: int # monto bruto = cantidad de producto X precio unitario
iva: int # iva 10 o 12 %
desc: int   # 1%
monto_total: int # monto total de la compra.

identificacion()
cp = int(input("ingrese la cantdidad de producto comprada "))
pu = int(input('ingrese el precio unitario '))
monto_bruto = cp * pu
if monto_bruto < 500000:
    iva = monto_bruto * 10 // 100
else:
    iva = monto_bruto * 12 // 100
desc = (monto_bruto + iva) // 100
monto_total = monto_bruto + iva - desc
print("Monto total a pagar es ", monto_total)