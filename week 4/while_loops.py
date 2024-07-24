number = 1

while number < 5:
    print(number)
    number += 1

# myList = []

# while len(myList) < 5:
#     name = input("Enter a name: ")
#     myList.append(name)

# print(myList)

names = ['Tobi', 'Ayo', 'Deji', 'Taiwo', 'Femi']
#          0       1       2       3        4

names[0]

# Deji
for name in names:
    if name == "Deji":
        print('Found name')

index = 0
while index < len(names):
    if names[index] == "Deji":
        print(f'Found name at index {index}')
        break
    else:
        index += 1