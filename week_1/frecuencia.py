def frecuencia_numeros(lista):
    conteo = {}
    for num in lista:
        conteo[num] = conteo.get(num, 0) + 1
    return conteo

print(frecuencia_numeros([1, 2, 4, 5, 5, 6, 7]))

def frecuencia_palabras(frase):
    conteo = {}
    for palabra in frase.split():
        palabra = palabra.lower()
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

print(frecuencia_palabras("Hola python y Hola mundos"))

def agrupar_por_categoria(productos):
    grupos = {}
    for nombre, categoria in productos:
        if categoria not in grupos:
            grupos[categoria] = []
        grupos[categoria].append(nombre)
    return grupos

productos = [
        ("Manzana", "Frutos"),
        ("Pera", "Fruta"),
        ("Lechuga", "Verdura"),
        ("Tomate", "Verdura")
    ]
print(agrupar_por_categoria(productos))

def analizador_texto(frase):
    frase = frase.lower()
    for signo in [".",",","!","?",";",":"]:
        frase = frase.replace(signo, "")
    palabras = frase.split()

    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

texto="Hola mundo, Hola python, python es genial!"
print(analizador_texto(texto))

