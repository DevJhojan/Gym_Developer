elements = [2,3,5,6,7,8,4,2,4]
reverse = []
aux = 0
for element in elements:
    aux += element

print(f"La suma de la lista {elements} es igual a {aux}")

aux = 0

for element in elements:
    if element % 2 == 0:
        aux += element

print(f"La suma de los pares es: {aux}")


for i in range(len(elements)-1,-1,-1):
    reverse.append(elements[i])

print(f"La lista al reverso es: {reverse}")

maximun = elements[0]
minimun = elements[0]

for i in elements:
    if i > maximun:
        maximun = i
    if i < minimun:
        minimun = i

print(f"El numero mayor de los elementos es: {maximun}\nEl numero menor de los elementos es: {minimun}")

elements_no_repeat = []
count = 0
elements_repeat = [];
for i in elements:
    if i not in elements_no_repeat:
        print(f"El numero {i} aparece {elements.count(i)} veces")
        elements_no_repeat.append(i)
        if elements.count(i) > count:
            elements_repeat = [i]
            count = elements.count(i)
        if elements.count(i) == count :
            if i not in elements_repeat:
                elements_repeat.append(i)


print(f"Los elementos que mas se repiten son {elements_repeat} que se repiten {count} veces")
