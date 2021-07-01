# clase 5 de mayo 
# Tablas de multiplicar

# def tabla(n):
    
#     print(str(n)+' * 1'+ ' = '+ str(1*n))
#     print(str(n)+' * 2'+ ' = '+ str(2*n))
#     print(str(n)+' * 3'+ ' = '+str(n*3))
#     print(str(n)+' * 4'+ ' = '+str(n*4))
#     print(str(n)+' * 5'+ ' = '+str(n*5))
#     print(str(n)+' * 6'+ ' = '+str(n*6))
#     print(str(n)+' * 7'+ ' = '+str(n*7))
#     print(str(n)+' * 8'+ ' = '+str(n*8))
#     print(str(n)+' * 9'+ ' = '+str(n*9))
#     print(str(n)+' * 10'+ ' = '+str(n*10))

# a=int (input('Ingrese que tabla desea consultar: '))
# tabla(a)

#Calcular Temperatura

# def temperatura(dia1,dia2,dia3): 
#     dia1 = float(input("Ingrese la temperatura del día uno:"))
#     dia2 = float(input("Ingrese la tempreratura del día dos:"))
#     dia3 = float(input("Ingrese la temperatura del día tres:"))
#     promedio = (d1+d2+d3)//3
#     print("El promedio de la temperatura de los tres días es: ", promedio, "grados centigrados")
#     return promedio

# temperatura(dia1,dia2,dia3)

# def promedio(t1,t2,t3): #definir funcion 
#     resultado=(t1+t2+t3)/3 #realiza el calculo
#     print("el promedio termico es:",resultado,"°C")#imprimimos temperatura promedio
# T1=float(input('ingrese temperatura 1: '))#ingresamos tem dia1
# T2=float(input('ingrese temperatura 2: '))#ingresamos tem dia2
# T3=float(input('ingrese temperatura 3: '))#ingresamos tem dia3

# promedio(T1,T2,T3)#llamamos la funcion con las comas

# De metros a kilometros

# def convertir(k):
#     #k=input("Ingresa la distancia en Kilometros ")
#     resultado=(k/100)
#     return resultado

# kilometros = float(input("Ingrese la distancia en Km: "))
# metros_convertir = convertir(kilometros)
# print("La recorrido en metros es = ", metros_convertir," m")

#Capacidad maxima de la sala de cines

# def cine():
#     capacidad=int(input("Ingrese la capacidad del cine: "))
#     personas=capacidad*0.3
#     return(personas)
# print("La cantidad de personas que pueden asistir a la reapertura es de",cine(),"personas")

#Colocar iva a productos

# def producto1():
#     #producto1=int(input("Ingrese el valor del primer Producto: "))
#     #producto2=int(input("Ingrese el valor del Segundo Producto: "))
#     valor1=producto1*0.19
#     return(valor1)

# def producto2():
#     valor2=producto2*0.19
#     return(valor2)

# producto1=int(input("Ingrese el valor del primer Producto: "))
# producto2=int(input("Ingrese el valor del Segundo Producto: "))
# print("El valor del primer producto sin iva es: ",producto1)
# print("El valor del segundo producto sin iva es: ",producto2)
# print("El valor del primer producto con iva de 19% es: "+str(producto1()))
# print("El valor del segundo producto con iva de 19%es: "+str(producto2()))
#Ejercicio 2
# def valor_de_articulos(v):
#     resultado = v + ((v * 30) / 100)
#     return resultado


# valor_sin_iva = int(input("Ingrese el valor sin IVA: "))
# valor_con_iva = valor_de_articulos(valor_sin_iva)
# print("El valor sin IVA es = ", valor_sin_iva)
# print("El valor sin IVA es = ", valor_con_iva)
# el segundo print es con IVA*
#ejercicio 2
def iva(art1,art2):
    a1=art1*1.19
    a2=art2*1.19    
    return(a1,a2)
    

ar1=int (input('Ingrese el valor del articulo 1 sin iva: '))
ar2=int (input('Ingrese el valor del articulo 2 sin iva: '))
(a1,a2)=iva(ar1,ar2)
print("El valor del articulo 1 sin iva es:",int(ar1)," y el valor con iva del 19% es:",a1)
print("El valor del articulo 2 sin iva es:",int(ar2)," y el valor con iva del 19% es:",a2)

