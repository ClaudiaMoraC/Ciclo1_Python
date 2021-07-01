import pandas as pd
import csv
# def EstaCiudad(ruta_archivo:str,Ciudad : str):
#     dataFrame = pd.read_csv(ruta_archivo, header=None, index_col=False,names=['Id_Ciudad', "Ciudad","Codigo_Ciudad","Habitantes"])
#     suma= dataFrame[dataFrame['Codigo_Ciudad'==Ciudad]['Habitantes'].sort_values().sum()
#     dic = dict()
#     dic[Ciudad] = suma
#     return dic


# #nombreArchivo= 'titanic3.csv'
# print(EstaCiudad('https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv','Bogota01'))
def ejemploReto5 (nombreArchivo:str) -> dict:
    import pandas as pd
    dataFrame = pd.read_csv(nombreArchivo)
    # print (dataFrame)
    # dataFrame.info()
    nombres = list ( dataFrame ['name'] )
    # print (nombres)
    mayorEdad = max ( dataFrame['age'])
    # print (mayorEdad)
    menorEdad = min ( dataFrame ['age'])
    # print (menorEdad)
    tarifaPromedio =  round ( (dataFrame['fare'].mean()), 2)
    
    diccionario = dict()
    diccionario ['nombres'] = nombres
    diccionario ['edadMayor'] = mayorEdad
    diccionario ['edadMenor'] = menorEdad
    diccionario ['tarifaPromedio'] = tarifaPromedio
    
    return diccionario
    # pass

#nombre = 'titanic3.csv'
print (ejemploReto5('https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv'))