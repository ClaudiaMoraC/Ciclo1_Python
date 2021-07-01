#Ciclos anidados

# Tablas de Multiplicar

# num = 1
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i * j} ")

#Ejercicio 1

for i in range(1,11):
    for j in range(1, i + 1):
        print(f"{i} * {j} = {i * j} ")