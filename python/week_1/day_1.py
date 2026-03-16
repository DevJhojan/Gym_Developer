elements = [3,5,3,5,7,1,3,4,5,6,4,3,5,6,6,7,2,4,6,8,9,7,9,0,4,1]

def sum_array_numbers(numbers_list)->int:
    aux = 0
    for number in numbers_list:
        aux += number
    return aux

def sum_pares_numbers(numbers) -> int:
    aux = 0
    for number in numbers:
        if number % 2 == 0:
            aux += number
    return aux

def list_reverse(numbers):
    reverse = []
    for number in range(len(numbers)-1, -1, -1):
        reverse.append(numbers[number])
    return reverse

def counter_number_array(number_list, number):
    return number_list.count(number)

def found_menor_and_mayor(numbers)->str:
    menor = numbers[0]
    mayor = numbers[0]
    for number in numbers:
        if number > mayor:
            mayor = number
        if number < menor:
            menor = number
    return f"El numero menor es {menor} y el numero mayor es {mayor}"

def numbers_reapest(numbers):
    numbers_no_repeat = []
    count = 0
    elements_repeat = []
    for number in numbers:
        if number not in numbers_no_repeat:
            numbers_no_repeat.append(number)
        if numbers.count(number) > count:
            elements_repeat=[number]
            count = numbers.count(number)
        if numbers.count(number) == count:
            if number not in elements_repeat:
                elements_repeat.append(number)
    print(f"Los elementos que mas se repiten son {elements_repeat} que se repiten {count} veces")

print(f"Lista: {elements}")
print(f"Lista invertida: {list_reverse(elements)}")
print(numbers_reapest(elements))
print(f"La suma de todos los numeros de la lista es: {sum_array_numbers(elements)}")
print(f"La suma de todos sus numeros pares es: {sum_pares_numbers(elements)}")
print(f"El numero 3 aparece en la lista {counter_number_array(elements, 3)} veces")
print(found_menor_and_mayor(elements))

