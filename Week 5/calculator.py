def add(x=0, y=0):
    return x + y

def deduct(x=0, y=0):
    return x - y

def multiply(x=0, y=0):
    return x * y

def divide(x=0, y=0):
    if y != 0:
        return x / y
    else:
        print("Division by 0 is not allowed")

def ask_for_details():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation: ")

    if operation == '+':
        print(add(first_number, second_number))
    elif operation == "-":
        print(deduct(first_number, second_number))
    elif operation == "*":
        print(multiply(first_number, second_number))
    elif operation == "/":
        print(divide(first_number, second_number))
    else:
        print("Invalid operation")

while True:
    ask_for_details()