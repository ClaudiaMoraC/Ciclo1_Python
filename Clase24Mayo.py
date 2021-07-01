#Ejercicios de la clase
#Leer un numero entero de 4 cifras y determinar cuantas cifras son pares
#Funciones con parametros
#Funciones, con parametros

# def MayorValor(x :int, y:int) -> int :
#     if x > y :
#         return(x)
#     else :
#         return(y)


# num1 = int(input("Digite numero 1 "))
# num2 = int(input("Digite numero 2 "))

# print(MayorValor(num1,num2))
#Funciones, con parametros
#Hacer un funcion que Lea un número entero de cuatro dígitos(+) y que la funcion retorne
#cuántos dígitos pares tiene.
# def ContarPares(num :int) -> int :
#     r1 = r2 = r3 = c1 = c2 = c3 = 0
#     ContP = 0
#     if num >= 1000 and num <= 9999 :
#         r1 = num % 10
#         c1 = num // 10
#         r2 = c1 % 10
#         c2 = c1 // 10
#         r3  = c2 % 10
#         c3 = c2 // 10
#         if r1 % 2 == 0 : 
#             ContP = ContP +  1
#         if r2 % 2 == 0 : 
#             ContP = ContP +  1
#         if r3 % 2 == 0 : 
#             ContP = ContP +  1
#         if c3 % 2 == 0 : 
#             ContP = ContP +  1
#     else :
#         print ("Fuera rango")      

#     return(ContP)

# #num1 = int(input("Digite numero 1 "))
# num = int(input("Digite numero  "))

# print("Cantidad de digitos pares = " ,ContarPares(num))

#Reto Clase
#Hacer un funcion que Lea dos número enteros de dos digitos(+) y que la funcion retorne
#la suma de los digitos pares.
#Ej : #1 -> 25 #2 -> 46  ..debe retornar 2 + 4 + 6  = 12 "

def sumaPares (num1 = int, num2 = int)-> int:
    suma = 0
    r1 = r2 = c1 = c2= 0
    if (num1 >= 10 and num1 <= 99) and (num2 >= 10 and num2 <= 99)  :
        r1 = num1 % 10
        c1 = num1 // 10
        r2 = num2 % 10
        c2 = num2 // 10

        if r1 % 2 == 0 : #Acomulador, cada vez que encuentre un numero par lo suma y lo guarda en suma
            print(r1)
            suma = suma + r1
        if r2 % 2 == 0 : 
            print(r2)
            suma = suma + r2
        if c1 % 2 == 0 :
            print(c1) 
            suma = suma + c1
        if c2 % 2 == 0 :
            print(c2) 
            suma = suma + c2
        else:
            print("No hay números pares")        
    else:
        print("Fuera de rango")

    return(suma)

num1 = int(input("Digite el primer número:  "))
num2 = int(input("Digite el segundo número:  "))

print("La suma de los números pares es: ",sumaPares(num1,num2))
