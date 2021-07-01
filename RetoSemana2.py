def Promedio_Notas(codigo1: str, Exa1: float, nota1: float, codigo2: str, Exa2: float, nota2: float, codigo3: str, Exa3:float, nota3 : float) -> str :
    if codigo1 == "111":
        mat = (Exa1 * 0.9) + (nota1 * 0.1)
    else:
        #mensaje="CODIGO DE MATEMATCA NO EXISTE"
        print("CODIGO MATEMATCA NO EXISTE")
        mat = 0
        #return mensaje
    if codigo2 == "222":
         fis = (Exa2 * 0.8) + (nota2 * 0.2)
    else:
        #mensaje = "CODIGO DE FISICA NO EXISTE"
        print("CODIGO FISICA NO EXISTE")
        fis = 0
        #return mensaje
    if codigo3 == "333":
        qui = (Exa3 * 0.85) + (nota3 * 0.15)
    else:
        #mensaje="CODIGO DE QUIMICA NO EXISTE"
        print("CODIGO QUÍMICA NO EXISTE")
        qui = 0
        #return mensaje
    #print(mat,fis,qui)
    promedio=(mat+fis+qui)/3
    promTotal = round(promedio, 2)
    if promTotal >= 3.0:
        mensaje= f"Paso el promedio con {promTotal}"
    else:
        mensaje= f"No paso el promedio con {promTotal}"

    return mensaje
     #f"El promedio Total ajustado del estudiante es: {promTotal}"

codigo1 = str(input("Ingrese codigo de matematicas: "))
codigo2 = str(input("Ingrese codigo de Fisica: "))
codigo3 = str(input("Ingrese codigo de Quimica: "))
Exa1=float(input("Ingrese nota de examen de matemticas: "))
nota1=float(input("Ingrese nota de trabajos de matemticas: "))
Exa2=float(input("Ingrese nota de examen de FISICA: "))
nota2=float(input("Ingrese nota de trabajos de FISICA: "))
Exa3=float(input("Ingrese nota de examen de QUÍMICA: "))
nota3=float(input("Ingrese nota de trabajos de QUÍMICA: "))
print(Promedio_Notas(codigo1,Exa1,nota1,codigo2,Exa2,nota2,codigo3,Exa3,nota3))