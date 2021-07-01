## estudiantes con codigo
#3 materias fisica, matematicas, quimica
#Estudiante con mejor promedio, imprimir codigo y nota
#el promedio por estudiante de las 3 materias
#La mejor materia por estudiante, imprima materia y nota
#ebustosc@gmail.com
#Ejercicos del 19, 20, 21, 22 o 23
for i in range(1,4) :
    codi = input("Digite codigo estudiante: ")
    MayorProm = 0
    MateriGana = 0
    EstudianteGanador = 0
    PromedioCurso=0
    for j in range(1,4) :
        Materia = int(input("Digite codigo materia: "))
        suma = 0
        for x in range(1,4) :
            Nota = float(input("Nota materia: "))
            suma = suma + Nota
        prom = suma / 3
        print(f"El promedio de la materia {Materia} es = {prom}")
        if prom > MayorProm : 
            MayorProm = prom
            MateriGana = Materia
            EstudianteGanador = codi
        
        
    print(f"El mayor promedio es =  {MayorProm} y la materia fue {MateriGana} ")

print(f"El estudiante con mejor promedio es: {EstudianteGanador}, con un promedio de = {MayorProm}, de la materia {MateriGana}")

