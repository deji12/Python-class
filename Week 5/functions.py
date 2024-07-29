def add_numbers(x=1, y=2):

    if x != None and y != None:
        print("God is great")
        return x + y

# addition = add_numbers(5, 8)

# print(addition)

# g(x) = x/2 
# [5, 9, 45, 67, 90]


def parent_function():

    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation: ")

    def add_nums(num1, num2):

        return num1 + num2
    
    if operation == "add":
        addition = add_nums(first_number, second_number)
        print(addition)

parent_function()