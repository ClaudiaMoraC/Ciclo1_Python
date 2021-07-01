
import pandas as pd
import csv

def EstaCiudad(ruta_archivo:str,Ciudad : str):
    suma= ruta_archivo[ruta_archivo["Codigo_Ciudad"]==Ciudad]['Habitantes'].sort_values().sum()
    codigo = ruta_archivo['Codigo_Ciudad']
    habitantes = ruta_archivo['Habitantes']
    diccionario = dict()
    diccionario[Ciudad] = suma
    return diccionario
ruta_archivo = pd.read_csv("https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv",header=None, index_col=False,names=['Id_Ciudad', "Ciudad","Codigo_Ciudad","Habitantes"])

Ciudad="Bogota01"
print(EstaCiudad(ruta_archivo,Ciudad))


import pandas as pd
import csv
def EstaCiudad (ruta_archivo:str, Ciudad : str) ->dict:
    dataFrame = pd.read_csv(ruta_archivo, header=None, index_col=False,names=['Id_Ciudad', "Ciudad","Codigo_Ciudad","Habitantes"])
    #suma= dataFrame[dataFrame['Codigo_Ciudad'==Ciudad]['Habitantes'].sort_values().sum()
    diccionario = dict()
    diccionario ['nombres'] = nombres
    #dic[Ciudad] = suma
    return dic
    # pass

#nombreArchivo= 'titanic3.csv'
print(EstaCiudad('https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv','Bogota01'))



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

nombre = 'titanic3.csv'
print (ejemploReto5(nombre))


import pandas as pd
import csv
def EstaCiudad(ruta_archivo:str,Ciudad : str):
    dataFrame = pd.read_csv(ruta_archivo, header=None, 
    index_col=False,names=['Id_Ciudad', 
    "Ciudad","Codigo_Ciudad","Habitantes"])
    suma= dataFrame[dataFrame['Codigo_Ciudad'==Ciudad]
    ['Habitantes'].sort_values().sum()
   return suma

print(EstaCiudad('https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv','Bogota01'))

import pandas as pd
import csv
def EstaCiudad(ruta_archivo:str,Ciudad : str):
    dataFrame = pd.read_csv(ruta_archivo, header=None, index_col=False,names=['Id_Ciudad','Ciudad','Codigo_Ciudad','Habitantes'])
    suma = str[dataFrame[dataFrame['Codigo_Ciudad'== Ciudad]['Habitantes'].sort_values().sum()]
    diccionario = dict()
    diccionario[Ciudad] = suma
    return Ciudad
    # pass

#nombreArchivo= 'titanic3.csv'
print(EstaCiudad('https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv','Bogota01'))



import pandas as pd
import csv

def EstaCiudad(ruta_archivo:str,Ciudad : str):
    datos=pd.read_csv(ruta_archivo)
    suma= datos[datos["Codigo_Ciudad"]==Ciudad]['Habitantes'].sort_values().sum()
    codigo = ruta_archivo['Codigo_Ciudad']
    habitantes = ruta_archivo['Habitantes']
    diccionario = dict()
    diccionario[Ciudad] = suma
    return diccionario
#ruta_archivo = pd.read_csv("https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv",header=None, index_col=False,names=['Id_Ciudad', "Ciudad","Codigo_Ciudad","Habitantes"])
#Ciudad="Bogota01"
print(EstaCiudad('https://raw.githubusercontent.com/ebustosc/ebustosc/main/Ciudades.csv','Bogota01'))