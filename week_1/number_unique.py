def numbers_unique(list_numbers):
    numbers_unique = []
    for num in list_numbers:
        if num not in numbers_unique:
            numbers_unique.append(num)
    return numbers_unique

print(numbers_unique([1,2,2,2,3,5,3,6,7]))

