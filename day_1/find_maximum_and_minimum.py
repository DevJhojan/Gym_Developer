elements = [4,3,5,6,2,1,3,4]

mayor = elements[0]
menor = elements[0]

for i in elements:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i

print("Mayor:", mayor)
print("Menor:", menor)
