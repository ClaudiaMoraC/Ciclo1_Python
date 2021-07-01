# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# Longitud de lita
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

#tipo
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

#Acceder a un elemento de la lista
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1]) # posicion 1

#La ultima posicion
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

#Rango
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5]) # Toma de la posicion 2 a la 5

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])#Imprime hasta la posicion 4

#Comprobar si existe
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

#Ordenar
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

#Muestra los valores de la lista que contengan a
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

#Elimiar  srt
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

#Eliminar int
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)#Posicion 1
# print(thislist)

#Agregar Datos a la lista
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

#Insertar 
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

#Agregar una lista a otra
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#Unir lista1 + lista2 conformando lista3
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

#count() Número de veces que se repite a

# list1 = ["a", "b", "c","a"]
# list2 = ["2","4","2","4","6","2"]
# print("a-> ",list1.count ("a"))
# print("2-> ",list2.count ("2"))