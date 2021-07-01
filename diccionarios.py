#diccionarios
# los diccionarios permite guardar mas informacion
# guadar mas variables

# persona={
#     'nombre': 'Juan',#nombre es clave, juan es el valor
#     'direccion':'mz 28b # 12',
#     'edad':24
# }
# print(persona)
# print(persona.keys())#imprime las claves
# print(persona.values())#Imprime los valores

# #Key llave
# #Como se puede tomar un valor del dicionario
# nombre=persona['nombre']#Se toma el valor de la clave nombre
# print(nombre)
# direccion=persona['direccion']#Se toma el valor de la clave nombre
# print(direccion)

#Reporte Notas
def reportarPromedio(dicReporte):
    return dicReporte["estudiante"]+ " = "+str(dicReporte["promedio"])
def generarReporteNotas(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas["nota1"]
    sumatoria += dicNotas["nota2"]
    sumatoria += dicNotas["nota3"]
    sumatoria += dicNotas["nota4"]
    promedio=round(sumatoria/4,2)
    reporteNotas={
        "promedio":promedio,
        "estudiante":dicNotas["estudiante"]
    }
    return reporteNotas
dicNotas={
    "estudiante":"Beneficiario Rodriguez",
    "nota1":3.0,
    "nota2":2.1,
    "nota3":5.0,
    "nota4":4.7
}
print(reportarPromedio(generarReporteNotas(dicNotas)))


