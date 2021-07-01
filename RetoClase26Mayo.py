# 26.Leer un número entero y determinar cuál es el mayor de sus dígitos.
# Ejemplo: 456, mayor el 6

# numMayor = 0
# num = int(input("Digite un número entero: "))
# aux = num
# while num >= 1:
#   aux = num % 10
#   if aux > numMayor:
#     num = aux
#   num = num/ 10
# print ("Digito mayor ", numMayor)


# 27. Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos.
# Ejemplo 1->235 2-> 24233, número 2

# num1 = int(input("Digite primer número entero: "))
# num2 = int(input("Digite segundo número entero: "))
# aux1 = num1
# aux2 = num2
# contadorNum1 = 0
# contadorNum2 = 0
# while aux1 != 0:
#     aux1 = aux1 / 10
#     contadorNum1 += 1

# while aux2 != 0:
#     aux2 = aux2 / 10
#     contadorNum2 += 1

# if contadorNum1 > contadorNum2:
#     print("El número 1 tiene mas digitos que el número 2")

# else:
#     if contadorNum1 < contadorNum2:
#         print("El número 2 tiene mas digitos que el número 1")
#     else: 
#         print("Los dos números tienen la misma cantidad de digitos")


# 28. Leer 2 números enteros y determinar cual de los dos tiene mayor cantidad de dígitos primos.

# num1 = int(input("Digite primer número entero: "))
# num2 = int(input("Digite segundo número entero: "))
# aux1 = num1
# aux2 = num2
# contadorNum1 = 0
# contadorNum2 = 0

# if aux1 >= 10 and aux1 <= 99:
#     if aux1 % 2 == 0 or aux1 % 3 == 0 or aux1 % 5 == 0 or aux1 % 7 == 0 :
#         while aux1 != 0:
#           aux1 = aux1 / 10
#           contadorNum1 += 1
# if aux2 >= 10 and aux2 <= 99:
#     if aux2 % 2 == 0 or aux2 % 3 == 0 or aux2 % 5 == 0 or aux2 % 7 == 0 :
#         while aux2 != 0:
#           aux2 = aux2 / 10
#           contadorNum2 += 1

# if contadorNum1 < contadorNum2:
#     print("El número 1 tiene mas digitos primos que el número 2")

# else:
#     if contadorNum1 > contadorNum2:
#         print("El número 2 tiene mas digitos primos que el número 1")
#     else: 
#         print("Los dos números tienen la misma cantidad de digitos primos")


# 29. Leer un número entero y determinar a cuánto es igual el primero de sus dígitos.

num = int(input("Ingrese un número entero de 2 digitos: "))
aux=0
aux=num
Reci = 0
Coci = 0
#while aux >= 0:
if aux >= 10 and aux <= 99 :
    Resi1 = aux % 10
    Coci1 = aux // 10
    # if aux >= 100 and aux <= 999 :
    #     Resi1 = aux % 10
    #     Coci1 = aux // 10
    #     Resi2 = Resi1 % 10
    #     Coci2 = Coci1 //10

print ("El primer digito del número", num, " es: ",Coci1)

# 30. Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para quienes el sea un múltiplo.

