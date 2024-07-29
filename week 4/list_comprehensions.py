numbers = []
for i in range(5):
    numbers.append(i**2)

print(numbers)

myList = [i**2 for i in range(5)]
print(myList)

# [expression for item in iterable]

names = ["deji", "taiwo", "precious", "hannah"]
new_name_list = []

for name in names:
    new_name_list.append(name.upper())

print(new_name_list)

new_list_by_comprehension = [name.upper() for name in names]
print(new_list_by_comprehension)