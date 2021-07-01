# clase 11 mayo
#Leer un número de 4 dígitos, mostrar el dígito mayor e informar si es par o impar.

#x=int(input("Ingrese un numero de 4 cifras"))

# a=input("ingrese un numero de 4 digitos: ")
# if len(a)==4:
#     datos=list(a)
#     print("El numero mayor es:",max(datos))
#     num=int(a)
#     if num % 2 == 0:
#         print('El número', a, 'es par.')
#     else:
#         print('El número', a, 'es impar.')

# Ejercicio desarrollado por la profesora

#Primer ejercicio
# num = int(input("Digite el numero de 4 cifras: "))
# if len(str(num)) == 4: 
    
#     v4 = num%10 
#     v3 = (num//10)%10 
#     v2 = (num//100)%10 
#     v1 = (num//1000)%10 
             
#     if v4 >= v3 and v4 >= v2 and v4 >= v1:
#         mayor = v4
#         print("el numero mayor es: ",mayor)
#     elif v3 >= v2 and v3 >= v4 and v3 >= v1:
#         mayor = v3
#         print("el numero mayor es: ",mayor)
#     elif v2 >= v3 and v2 >= v4 and v2 >= v1:
#         mayor = v2
#         print("el numero mayor es: ",mayor)
#     else:
#         mayor = v1
#         print("el numero mayor es: ",mayor)
      
        
#     if mayor%2==0:
#         print("Numero par")
#     else:
#         print("Numero impar")

##Ejercicio de tarea
#Generar numero de 1 a 10 o 20
# libreria random...import random
#Generar un numero aleatorio
#Con condiciones
# comparara el numero si 
#Juguemos al juego de adivinar el número, generaremos un número entre 1 y 100. 
# Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado. 
# También poner el número de intentos requeridos.

import random

print("El rango es de 1 a 5")
v1=random.randrange(1,5)
v2=int(input("Ingresa el número: ")) 
if v1>v2:
    print("El número es mayor que: ",v2)
else:
    if v1<v2:
        print("El número es menor que:",v2)

    else:
        v1==v2

        print("Número correcto")