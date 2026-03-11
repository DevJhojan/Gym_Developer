elements = [1,3,4,5,6]
aux = 0
for i in elements:
    aux += i

print("Suma de todos los elementos")
print(f"Total sum of list: {aux}")


aux=0

for i in elements:
    if i % 2 == 0:
        aux += i

print("Suma de solo los elementos pares")
print(f"El total de la suma de los elementos pares es: {aux}")




