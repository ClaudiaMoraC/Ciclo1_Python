# Reto Semana 1
# Determinar la velocidad en caída libre de un cuerpo

import math #Libreria de matematicas

def velocidad_caida_libre(altura: int,masa: int)->str: #Declaración de la función
    gravedad = float(9.807) #Gravedad de la tierra 9,807 m/s^2
    x = int (2 * altura) #Se multiplica 2 por la altura ingresada, se guarda en la variable x
    y = x * gravedad    #Se multiplica el valor de x por la gravedad, se guarda en la variable y
    z = (y)**0.5
    velocidadRedondeado= round(z,2) #Round redondea el valor decimal a dos cifras, math.sqrt da la raiz cuadrada de y
    velocidad=str(velocidadRedondeado)
    return f"La velocidad con la que el cuerpo de {masa}kg en caida libre desde una altura de {altura}m impacta en suelo es de: {velocidad}m/s"

print(velocidad_caida_libre(10,85))


# altura = int (input('Ingrese el valor de la altura en metros: '))
# masa = int (input('Ingrese el valor de la masa en kg: '))
# (vel)=velocidad_caida_libre(altura,masa)
# print("La velocidad con la que el cuerpo de ",str(masa),"kg en caida libre desde una altura de ",str(altura),"m impacta en suelo es de: ",str(vel),"m/s")

