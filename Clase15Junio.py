#Funcion Anidada
# def crear_funcion(operador):
#     if operador == '+':
#         def suma(val1=0, val2=0):
#             return val1 + val2
#         return suma
    
#     if operador == '-':
#         def resta(val1=0, val2=0):
#             return val1 - val2
#         return resta
    
#     if operador == '*':
#         def producto(val1=0, val2=0):
#             return val1 * val2
#         return producto
    
# def operacion(funcion, val1=0, val2=0):
#     return funcion(val1, val2)

# funcion_suma = crear_funcion('+')
# funcion_resta = crear_funcion('-')
# funcion_producto = crear_funcion('*')

# resultado1 = operacion(funcion_suma, 10, 20)
# resultado2 = operacion(funcion_resta, 10, 20)
# resultado3 = operacion(funcion_producto, 10, 20)

# print('Los números ingresados son ', 10 ,'y', 20 )
# print('La suma es = ', resultado1)
# print('La resta es = ', resultado2)    
# print('El producto es = ', resultado3) 

#Lambda
# suma=lambda val1=0, val2=0: val1+val2
# operacion = lambda operacion, val1=0, val2=0 : operacion(val1, val2)
# resultado1 = operacion(suma, 10, 20)

# resta=lambda val1=0, val2=0: val1-val2
# resultado2 = operacion(resta, 10, 20)

# multiplicacion=lambda val1=0, val2=0: val1*val2
# resultado3 = operacion(multiplicacion, 10, 20)

# print('La suma es = ', resultado1)
# print('La resta es = ', resultado2)    
# print('El producto es = ', resultado3)

#Map

# def cuadrado(ele=0):
#     return ele * ele
# lista =[1,2,3,4,5,6,7,8,9]
# resultado = list(map(cuadrado, lista))
# print(resultado)

# lista=[1,2,3,4,5,6,7,8,9,10]
# resultado=list(map(lambda elemento=0: elemento*elemento,lista))
# print(resultado)
#
# lista = [x for x in range(1,11)] 
# resultado = list(map(lambda x :  (x * x),lista))
# print(resultado)

#Filter-filtros
# lista = [x for x in range(3,101)]

# tupla = tuple(filter(lambda x:  50 < x < 70 and x % 2 != 0 , lista) )
# print(tupla)

#Ejemplo Reduce
# tupla = (5,2,6,7,8,10)
# def funcion_numero(numero1=0, numero2=0):
#     return numero1 - numero2
# resultado= reduce(funcion_numero, tupla) 
# print(resultado)  
# #Ejemplo zip
# lista_a = [1, 2, 3, 4, 5]
# lista_b = ['uno', 'dos', 'tres']
# resultado = zip(lista_a, lista_b)
# print(tuple(resultado))

#################################

# lista_c = ['a1', 'b2', 'c3']
# resultado = zip(*lista_c)
# print(tuple(resultado))
#Reto 3
# Estudiante={}
# Estudiante[10]=(0,0,0) 
# Estudiante[11]=(0,0,0) 
# Estudiante[12]=(0,0,0)
# x = 1
# y = 2
# z = 3
# for codigo in Estudiante :
#     Estudiante[codigo] =  (x,y,z)
#     x+=1
#     y+=1
#     z+=1

# print(Estudiante)

#Numpy
import numpy  as np
import random

b = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
#print(b)

#print(b[0,2])  

#matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
#print(matriz)

e = np.random.random((3,3))  # Crear una matriz llena de valores aleatorios
print(e)                     # Podría imprimir "[[ 0.91940167  0.08143941]
for f in range(0,3):
    for c in range(0,3):
        b[f,c] = random.randrange(20)

print(b)