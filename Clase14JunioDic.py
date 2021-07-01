
# Keys claves
# Values valores
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# 
# print(thisdict)

#Imprimir el valor de brand

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict["brand"])

# #Obtener el valor de la clave model
# x = thisdict.get("model")
# print(x)

#Obtener Keys()

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()#Obtiene todas las key del dic car

# print(x) #before the change
# car["color"] = "white" #Agregar un nuevo keys
# print(x) #after the change

#Obtener valores values()
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

#Eliminar elemnto del diccionario
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

#Elimina ultimo elemento insertado
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

#Imprimir todo los nombres de clave del diccionario
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
  #print(x)

#Imprima los valores del diciconarios
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)

#Recorrer claves y valores
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)

#Copiar diccionario

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

#Diccionarios anidados
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily)

#3 diccionarios y otro con el valor de todos
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)

#Metodos
# clear () Elimina todos los elementos del diccionario
# copy () Devuelve una copia del diccionario
# fromkeys () Devuelve un diccionario con las claves y el valor especificados
# get () Devuelve el valor de la clave especificada
# items () Devuelve una lista que contiene una tupla para cada par clave-valor
# keys () Devuelve una lista que contiene las claves del diccionario.
# pop () Elimina el elemento con la clave especificada
# popitem () Elimina el último par clave-valor insertado
# setdefault () Devuelve el valor de la clave especificada. Si la clave no existe: inserte la clave, con el valor especificado
# update () Actualiza el diccionario con los pares clave-valor especificados
# valores () Devuelve una lista de todos los valores del diccionario.




