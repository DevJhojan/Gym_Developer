elements = [2,3,4,2,3,2,5,6,7,8,9]
reverse = []

for i in range(len(elements)-1,-1,-1):
    reverse.append(elements[i])

print(reverse)
