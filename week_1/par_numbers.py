def filter_pars(list_numbers):
    numbers_filters = []
    for num in list_numbers:
        if num % 2 == 0:
            numbers_filters.append(num)
    return numbers_filters

numbers = [1,23,4,5,63,24,6,8,5,2,6,7,8,9,20]

print(filter_pars(numbers))

            
