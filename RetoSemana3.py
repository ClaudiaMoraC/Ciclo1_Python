def CalculoNomina(Empleados: dict) -> float:
    sueldo = 0
    for codigo in Empleados:
        valorHora = Empleados[codigo][1]
        hora = Empleados[codigo][0]
        if hora <= 20:
            tarifa = hora * valorHora
            Empleados[codigo]=(hora,valorHora,tarifa)
            if tarifa > sueldo:
                sueldo = tarifa
        else:
            if hora > 20 and hora <= 40:
                tarifa = (20 * valorHora) + (hora -20) * (2 * valorHora)
                Empleados[codigo] = (hora,valorHora,tarifa)
                if tarifa > sueldo:
                    sueldo = tarifa
            else:
                tarifa = (valorHora * 20) + (20 * (valorHora * 2) + (hora - 40) * (3 * valorHora))
                Empleados[codigo] = (hora,valorHora,tarifa)
                if tarifa > sueldo:
                    sueldo = tarifa
    return sueldo
# Modifica el diccionario Empleados para agregar el valor dela nomina
#float -> Retorna mejor sueldo
   

def imprimir(Empleados: dict):
    print("Codigo   Horas   Valor hora  Valor a pagar")

    for codigo in Empleados:
        print("{:}{:10}{:15,}{:15,}".format(codigo,Empleados[codigo][0],Empleados[codigo][1],Empleados[codigo][2]))
    #Imprimir de cada empleado el Codigo, Horas trabajadas, Valor hora, Valor a pagar.
    
#Empleados[Código trabajador ] = (Horas semanales, Valor hora a pagar, Total a pagar)


Empleados={}
Empleados[111]=(10,10000,0)
Empleados[222]=(22,10000,0)
Empleados[333]=(52,10000,0)
Sueldo = CalculoNomina(Empleados)
imprimir(Empleados)
CalculoNomina(Empleados)
print('El mejor sueldo es ${:5,}'.format(CalculoNomina(Empleados)))

