#While ..... FOR

#LimiIn = 0
#LimiSupe = 10
#Contador = 1
#for i in range(LimiIn,LimiSupe +  1,Contador) :
#    print(i)

# datos = range(1,21,2)
# for dat in datos :
#    print(dat)

# for j in range(20,-1,-1) :
#    print(f"vamos para atras {j}")

#j = 0
#while j <= 20 :
#    print(j)
#   j+=2  => j = j + 2

#Realizar una función que eleve un número de base a un exponente
#Ejemplo 2^3
# = 2*2*2=8

def Potencia (base:int, exponente: int)->int:
    potencia = 1
    for  i in range(0, exponente):
        potencia = potencia * base # Acomulador
        
    return(potencia)

# # base = int(input("Digite la base: "))
# # exponente = int(input("Digite el exponente: "))
print("La potencia es: ", Potencia(5,5))

# Factorial de un número

# def factorial(num:int)->int:
#     fac = 1
#     for i in range(num, 0, -1) :
#         #print(j)
#         fac = fac*i
#     return(fac)

# num = int(input("Digite número: "))
# print("El factorial es: ",factorial(num))

#Sumatoria
# def sumatoria (n:int)->float:
#     sumatoria=0.0
#     for i in range (1, n + 1):#
#         sumatoria =sumatoria + (Potencia(i,i)/factorial(i))

#     return(sumatoria)

# num = int(input("Digite limite: "))
# print("La sumatoria es: ",sumatoria(num))

# def Potencia(b : int,e : int ) -> int :
#     Pot = 1
#     for i in range(0, e) :
#         Pot = Pot * b  #Acumulador
#     return(Pot)

# print("La potencia es: ", Potencia(5,5))

# def factorial(num : int ) -> int :
#     fac = 1
#     for i in range(num, 0,-1) :
#         fac = fac * i  #Acumulador
#         print(fac)
#     return(fac)


# def SumaToria(n : int) -> float :
#     suma = 0.0
#     for i in range(1, n + 1) :
#         suma = suma + (Potencia(i,i) / factorial(i))

#     return(suma)



# N = int(input("Digite N "))

# print(f"la sumatoria es = {SumaToria(N)}")

#realizar una funcion que digite número de un digito, la función debe retornar el número armado
#ejemplo: si digitas 4 6 8, la función debe retornarte el 468

# def unionNumeros(num:int)->int:
    
#     digito=1
#     for i in range(1,num+1):
#         digito=int(input("ingrese le digito: "))
        
#         if digito>=0 and digito<=9:
#             if i == 1:
#                 numeroU=digito
#             else:
#                 numeroU=numeroU*10+digito
        
#     return(numeroU)

# num=int(input("Cuantos numeros desea ingresar:"))

# print(f"El numero armado es: {unionNumeros(num)}")

# def ArmaEntero() -> int :
#     x = 'n'
#     Entero = 0
#     while x != 's' : 
#         x = input("Digito ")
#         if x >= '0'  and x <= '9' :
#             Entero =  (Entero * 10) + int(x) #Cast
#         else :
#             print("No se recibe numero")
#     return(Entero)

# print(f"Entero armado = {ArmaEntero()}")

#Realizar una función que digite número(1 digito) , 4 6 8. 5 4 6  ‘s’ , debe retornar el número armado
# # el número Real armado.  Ej   4 7 9 2 . 3 4 retornar(4792.34)