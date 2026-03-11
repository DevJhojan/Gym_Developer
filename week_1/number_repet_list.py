elements = [2,1,4,5,3,4,5,7,7,6,6,4,4,4,4,3,3,3,3,3,3,1,1,1,1,3,3,3]
aux = 0
count = 0
element = 0
print (elements)
for i in elements:
    print(f"El elemento { i } se repite {elements.count(i)} veces")
    count = elements.count(i)
    if count > aux:
        print(f"Se verifica que el elemento { i } \n se repite mas veces que e elemento actual \n por ende se hace actualizacion..")
        aux = elements.count(i)
        element = i
    else:
        print(f"El elemento que mas se repite hasta el momento es el { element }")
