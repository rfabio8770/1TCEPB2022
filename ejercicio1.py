"""
Los empleados de una fábrica trabajan en dos turnos, diurno y nocturno. Se desea calcular el
jornal diario de acuerdo con la siguiente tarifa: La tarifa diurna es 40.000 Gs. la hora; la
nocturna es 50.000 Gs. la hora y los domingos, la tarifa diurna es el doble de la normal y para
la nocturna el triple. Realizar un algoritmo que lea la cantidad de horas trabajadas por el
empleado, el turno en el que trabajo y si es domingo o no.
"""
def identificacion():
    print("Ricardo Fabio")

# DECLARACION DE VARIABLES
ht: int # horas trabajadas
tarifa_dia: int # tarifa diurna
tarifa_noche: int # tarifa nocturna
dia: str  # nombre del día
tp: int # total a pagar
turno: int # 1 = mañana 2 = noche

identificacion()
ht = int(input('ingrese las horas trabajadas '))
turno = int(input('ingrese el turno 1 = mañana 2 = noche '))
dia = input('ingrese el nombre del dia ')
tarifa_dia = 40000
tarifa_noche = 50000
if turno == 1:  # es mañana
    if dia == "domingo" :
        tp = ht * tarifa_dia * 2
    else:
        tp = ht * tarifa_dia
else:
    if dia == "domingo":
        tp = ht * tarifa_noche * 3
    else:
        tp = ht * tarifa_noche
print("el total a pagar es ", tp)