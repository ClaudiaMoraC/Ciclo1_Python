#Leer 5 digitos enteros, y esta debe retornar el numero armado, eje: 2 3 -> 23

con =0

def numeroArmado (cantidad = int)-> int:
    num1=int(input("NUMERO 1 "))
    if cantidad == 1 and (num1 >=1 and num1 <=9) :
        con=num1
    else:
        num1=int(input("NUMERO 1 "))
        num2=int(input("NUMERO 2 ")) 
        if cantidad == 2 and ((num1 >=1 and num1 <=9) and (num2 >=0 and num2 <=9)):
            
            con = (num1 * 10) + num2
            print(con)
        else:
            num1=int(input("NUMERO 1 "))
            num2=int(input("NUMERO 2 ")) 
            num3=int(input("NUMERO 3 "))
            if cantidad == 3 and ((num1 >=1 and num1 <=9) and (num2 >=0 and num2 <=9) and (num3 >=0 and num3 <=9)):
                con = (((num1 * 10) + num2) * 10 + num3)
                print(con)
            else:
                num1=int(input("NUMERO 1 "))
                num2=int(input("NUMERO 2 ")) 
                num3=int(input("NUMERO 3 "))
                num4=int(input("NUMERO 4 "))
                if cantidad == 4 and ((num1 >=1 and num1 <=9) and (num2 >=0 and num2 <=9) and (num3 >=0 and num3 <=9) and (num4 >=0 and num4 <=9)):
                   
                    con = (((num1 * 10) + num2) * 10 + num3) * 10 + num4
                    print(con)
                else:
                    num1=int(input("NUMERO 1 "))
                    num2=int(input("NUMERO 2 ")) 
                    num3=int(input("NUMERO 3 "))
                    num4=int(input("NUMERO 4 "))
                    num5=int(input("NUMERO 5 "))
                
                    (num1 >=1 and num1 <=9)and (num2 >=0 and num2 <=9) and (num3 >=0 and num3 <=9) and (num4 >=0 and num4 <=9) and (num5 >=0 and num5 <=9)
                
                    con=(((((num1 * 10) + num2) * 10 + num3) * 10 + num4) * 10 + num5)
                    print(con)

    return(numeroArmado(cantidad))

cantidad = int(input("Ingrese la cantidad de números del 1 al 5: "))
print(numeroArmado(cantidad))
# 20. Leer tres números enteros y mostrarlos ascendentemente.La Esencia de la Lógica de Programación – Omar Ivan Trejos Buriticá 139

# def acendente (num = int)-> int:

#     return(0)

# 21. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra 
# el mayor dígito.
# 22. Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último.
# 23. Leer un número entero de tres dígitos y determinar cuántos dígitos primos tiene.
# 24. Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene.
# 25. Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la suma de los otros dos.
# 26. Leer un número entero de cuatro dígitos y determinar a cuanto es igual la suma de sus dígitos.
# 27. Leer un número entero de cuatro dígitos y determinar cuántos dígitos pares tiene.
# 28. Leer un número entero menor que 50 y positivo y determinar si es un número primo.
# 29. Leer un número entero de cinco dígitos y determinar si es un número capicúo. Ej. 15651, 59895.
# 30. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.
# 31. Leer un número entero y determina si es igual a 10.
# 32. Leer un número entero y determinar si es múltiplo de 7.
# 33. Leer un número entero y determinar si termina en 7.
# 34. Leer un número entero menor que mil y determinar cuántos dígitos tiene.
# 35. Leer un número entero de dos dígitos, guardar cada dígito en una variable diferente y luego mostrarlas en pantalla.
# 36. Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.
# 37. Leer dos números enteros y determinar cuál es múltiplo de cuál.
# 38. Leer tres números enteros y determinar si el último dígito de los tres números es igual.
# 39. Leer tres números enteros y determina si el penúltimo dígito de los tres números es igual.
# 40. Leer dos números enteros y si la diferencia entre los dos es menor o igual a 10 entonces
# mostrar en pantalla todos los enteros comprendidos entre el menor y el mayor de los números leídos.
