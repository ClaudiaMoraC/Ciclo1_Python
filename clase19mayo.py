# num=20

# if num > 0:
#     print("Es positivo")
# if num < 0:
#     print("Es negativo")
# if (num % 2 == 0):
#     print("Es Par")
# else:
#     print("Es Impar")

# Triangulo
#& es igual que and
#| es igual que or
# l1 = 1
# l2 = 1
# l3 = 3
# #Equilatero: todos los lados iguales
# #Escaleno dos iguales, 1 diferente
# #Isósceles todos diferentes
# if (l1 == l2 and l3 == l1):#Si todo los lados son iguales
#     print("Equilatero")
# elif l1 != l2 and l2 != l3 and l3 != l1: #Elif negacion del if, Si no son iguales
#     print("Isósceles")
# else:
#     print("Escaleno")

#Cada lado debe ser menor a la suma longitud de los otros 
# dos lados ej: 5 7 3 => si se puede armar triangulo
# Ej : 10 2 5 => no se puede armar triangulo
l1 = 10
l2 = 2
l3 = 5

if (l1+l2)>l3 and (l2+l3)>l1 and (l1+l3)>l2:
    print("Se puede realizar un triangulo")
else:
    print("No se puede ")

