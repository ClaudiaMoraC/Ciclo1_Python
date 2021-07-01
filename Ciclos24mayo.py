# 1- primer ejercicio
# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Despegue!')

# 2- los numeros inpares desde el 1 hasta el 20 elevado al cuadrado

# i = 1

# while i <= 20:
#     print(i*i)
#     i += 2#Contador, va sumando i mas 2, de dos en dos 1,3,5....

#3- Leer un numero entero y mostrar todos los pares hasta el numero leido
# num = int(input("Digite numero: "))
# i = 0
# while i <= num:
#     print(i)
#     i+=2
#4-  Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205

# i = 25
# while(i < 205):
#     x = i % 10
#     if (x == 6):
#         print (i)
#     i+=1

#5- Mostrar en pantalla los primeros N múltiplos de 3 Ej: n-> 4    3, 6 , 9 , 12 ... N

num = int(input("Digite número: "))

i=1
while i <= num:
    
    print(i * 3)
    i += 1