def promedio(list_number):
    return sum(list_number) / len(list_number)

def numeros_unicos(list_number):
    numeros_unicos=[]
    for num in list_number:
        if num not in numeros_unicos:
            numeros_unicos.append(num)
    return numeros_unicos

def numero_mayor(list_number):
    mayor = list_number[0]
    for num in list_number:
        if num > mayor:
            mayor = num 
    return mayor
def numero_menor(list_numbers):
    menor = list_numbers[0]
    for num in list_numbers:
        if num < menor:
            menor = num
    return menor

def palindromo(number):
    number = str(number)
    number = number.replace(" ","").lower()
    inicio = 0
    fin = len(number)-1
    while inicio < fin:
        if number[inicio] != number[fin]:
            return False
        inicio += 1
        fin -= 1
    return True


def analizar_lista(lista):
    lista_unica = numeros_unicos(lista)
    print("Números únicos:", lista_unica)
    print("Promedio:", promedio(lista_unica))
    print("Máximo:", numero_mayor(lista_unica))
    print("Mínimo:", numero_menor(lista_unica))
    
    palindromos = [n for n in lista_unica if palindromo(n)]
    print("Palíndromos encontrados:", palindromos)

numbers = [223,313,433,542,616,636,700]

analizar_lista(numbers)
