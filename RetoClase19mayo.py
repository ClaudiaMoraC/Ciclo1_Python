# 1. Leer un número entero y determinar si es un número terminado en 4.

# entero=input("Escribe un número entero de 4 digitos: ")
# #print(list(entero)) Lista el numero ingresado
# a=int(entero[3])# toma la ultima posicion del numero de 4 digitos
# if a==4:
#     print("El número ",entero," termina en 4")
# else:
#     print("El número ",entero," no termina en 4")

# 2. Leer un número entero y determinar si tiene 3 dígitos.

# num=input("Escribe un numero entero ")

# #print(list(num))
# if len(num)==3:#Deterina si la longitud del numero num es igual a 3 cifras
#     print("El número",num," es de 3 cifras")
# else:
#     print("El número ",num," no es de 3 cifras ")

# 3. Leer un número entero y determinar si es negativo.

# num = int(input("Escribe un número entero "))

# if num < 0:
#     print("El número es negativo")
# else:
#     print("El número es positivo ")

# 4. Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.

# enterosdos=input("Ingresa un número de 2 cifras: ")
# a=int(enterosdos[0])#Tomar la posicion 1
# b=int(enterosdos[1])#tomar la posicion 2
# suma = a+b
# print("La suma de los dos digitos es: " ,suma)


num = int(input("Digite numero entero positivos y negativos  "))
Resi = 0
Coci = 0
if num >= -99 and num <= -10 :
    num =  num * (-1)
    Resi = num % 10
    Coci = num // 10
    print (Resi+Coci)
else :
    if num >= 10 and num <= 99 :
        Resi = num % 10
        Coci = num // 10
        print (Resi+Coci)
    else :
        print ("Fuera del rango ")

# 5. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

# enterosdos=input("Ingresa un número de 2 cifras: ")
# b=int(enterosdos[0])#Tomar la posicion 1
# c=int(enterosdos[1])#tomar la posicion 2

# if int(b/2)*2==b and int(c/2)*2==c:#determinar si b y c son pares
#     print("Los dos digitos son pares: ",enterosdos)
# else:
#     print("Los dos digitos son impares: ",enterosdos)

# 6. Leer un número entero de dos dígitos menor que 20 y determinar si es primo.

# num = int(input("Ingrese un número entero "))

# if num >= 10 and num <= 99:
#     if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 :
#         print("No es Primo")
#     else:
#         print("si es primo")
# else:
#     print("Fuera de rango")


# 7. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
# 8. Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.
# 9. Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.

#multiplo = int(input("Ingrese un número entero de dos cifras"))


# 10. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
# enterosdos=input("Ingresa un número de 2 cifras: ")
# b=int(enterosdos[0])#Tomar la posicion 1
# c=int(enterosdos[1])#tomar la posicion 2

# if b==c:#determinar si b y c son pares
#     print("Los dos digitos son iguales: ",enterosdos)
# else:
#     print("Los dos digitos no son iguales: ",enterosdos)