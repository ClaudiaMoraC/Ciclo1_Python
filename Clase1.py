#Ejercicio cuadrado

#Ingreso de datos por consola
# l=(int(input("Ingrese el valor del lado del cuadrado en metros: ")))
# perimetro=4*l
# area=l*l
# print("Lado del cuadrado" , l)
# print("El area del cuadrado es: " ,area)
# print("El Perimetro del cuadrado es: " , perimetro)

#Funciones maximo y minimo

# var1 = 10
# var2 = 30
# var3 = 120 
# var4 = 500

# maximo = max(var1, var2, var3, var4)
# print(maximo)

# minimo = min(var1, var2, var3, var4)
# print(minimo)

#Suma de variables

# var1 = 10
# var2 = 30
# var3 = 120 
# var4 = 500

# Vars=[var1,var2,var3,var4]
# t= sum(Vars)

#Rango

# x = range(7,18) #DEVUELVE LOS NUMERO DEL 0 AL 4 
# #7 valor inicial y 18 valor final menos una unidad
# print(list(x))

#LLONGITUD

# x = range(0,5) 
# print(list(x))

# len(x) #Esto tendria un tamaño de 4 numeros {0, 1, 2, 3, 4}
# print(len(x))#numero de datos 

# PROMEDIO

# var1 = 10
# var2 = 30
# var3 = 120 
# var4 = 500

# Vars=[var1,var2,var3,var4]
# t= sum(Vars)
# promedio=(sum(Vars))/(len(Vars))
# print("El promedio es:" +str(promedio))
# # str concatena y une el texto con el valor de promedio. cadena

#FUNCIONES

# def imprime_Cosas(a):
#     a=input("Dime tu nombre ")
#     print("Hola ",a)   #Se debe explicar de la indentacion de python y de como se ejecutan las instrucciones
#     print('Python es lo maximo')

# #y=input("Dime tu  nombre ")#se ingresa el dato por teclado
# #imprime_Cosas(y)#Toma el dato y lo retorna a la funcion Imprime_Cosas

# def repetir_funciones():
#     imprime_Cosas()
#     imprime_Cosas()
    
# repetir_funciones()

# funcion de prosesos matematicos
 def operaciones(a,b,c,d,e):
     m=a*b*c*d*e
     print(m)
     s=a+b+c+d+e
     print(s)
     return m,s

v1=1
v2=3
v3=5
v4=56
v5=4
[resultado1,resultado2]=operaciones(v1,v2,v3,v4,v5)#resultado1 variable de multiplicacion, resultado2 variable de suma
operaciones(v1,v2,v3,v4,v5)
d=resultado1/2
print(d)

# 5 retos, cada reto son 80% nota
# 