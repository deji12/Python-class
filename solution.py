"""

Task 3: List Comprehensions: Use list comprehension to create a list of squares of numbers from 1 to 10.

Given the list 
    names = ["alice", "bob", "charlie", "dave"], 
    
    use list comprehension to create a new list with each name capitalized using the .capitalize() string method.

"""

# [expression for item in iterable]

squares = [number**2 for number in range(1, 11)]

print(squares)

names = ["alice", "bob", "charlie", "dave", 56.7, 9]

new_list = []

for i in names:
    if isinstance(i, str):
        new_list.append(i.capitalize())

# [expression for item in iterable condition]

capitalized_names = [name.capitalize() for name in names if isinstance(name, str)]

print(capitalized_names)