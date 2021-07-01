#Ejercicos del 19, 20, 21, 22 o 23

#20. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran
# tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son
# menos de tres camisas un descuento del 10%
suma=0
i=1
numeroCamisas = int(input("Ingrese el total de Camisas a comprar: "))
valor = int(input("Ingrese el valor por unidad "))
if numeroCamisas >=3:
    valorCompra = numeroCamisas * valor
    descuento = (valorCompra * 0.2) // 100
    valorDescuento = valorCompra - descuento
    print(f"El Valor total a pagar incluido el descuento del 20% es:  {valorDescuento}")
else:
    valorCompra = numeroCamisas * valor
    descuento = (valorCompra * 0.1) // 100
    valorDescuento = valorCompra - descuento
    print(f"El Valor total a pagar incluido el descuento del 10% es:  {valorDescuento}")

# 21. Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y
# 5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó
# o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro
# del rango permitido.

# suma=0
# i=1
# nombreAlumno = str(input("Ingrese el nombre del estudiante: "))
# for x in range(1,4) :
   
#     Nota = float(input(f"Nota materia {i}: "))
#     if Nota >=0 and Nota <= 5:
#         i+=1
#         suma = suma + Nota
#     else:
#         print("Nota fuera de Rango")
#         quit()
#     prom = suma / 3
# if prom >= 3:
#     print(f"El estudiante {nombreAlumno} Aprobo la materia con un promedio de = {prom}")
# else:
#     print(f"El estudiante {nombreAlumno} No aprobo la materia con un promedio de = {prom}")
