
#Realizar una función que lea n números y determine el promedio de los números impares
#y retornar su resultado en string
#Realizar una funcion, que Leea N numeros y determinar el promedio de los numeros impares
#y retornar su resultado{string}
# def PromInpar(N : int) -> str :
#     i = 0
#     sum = 0
#     ContIn = 0
#     while i < N :
#         num = int(input("Digite numero  "))
#         if num % 2 != 0 :
#             sum = sum + num  #Acumulador    
#             ContIn+=1    
#         i+=1  # contador
#         print(i)
    
#     Mensaje = f"El promedio es  = {sum/ContIn}"
    
#     return(Mensaje) # Un return solamente debe ser ejecutado 1 vez
    


# print(PromInpar(4))

#Realizar una función que lea n numeros y que determine cuantos números estan en el rango de 
# 10 y 100 y cuantos son inpares y el promedio de los números pares
# Debe retornar el promedio de los números pares
#Ejemplo : N = 4     3 , 20 , 40 , 9   rango = 2  CanInpar = 2  CanPares = 2
#Retornar (20 + 40)/ 2

def PromPar(N : int) -> str :
    i = 0
    sum = 0
    ContIn = 0
    while i < N :
        num = int(input("Digite numero  "))
        if num >= 10 and num <= 100:
            if num % 2 == 0 :
                sum = sum + num  #Acumulador    
                ContIn+=1    
        i+=1  # contador
        print(i)
    
    Mensaje = f"El promedio es  = {sum/ContIn}"
    
    return(Mensaje) # Un return solamente debe ser ejecutado 1 vez

print(PromPar(4))