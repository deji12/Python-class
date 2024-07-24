first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("\nEnter 1 to add\nEnter 2 to subtract\nEnter 3 to multiply\nEnter 4 to divide")

operation = int(input("Enter your choice: "))

if operation == 1:
    print(first_number + second_number)

elif operation == 2:
    print(first_number - second_number)

elif operation == 3:
    print(first_number * second_number)

elif operation == 4:
    if second_number == 0:
        print("You can't divide by zero")
    else:
        print(first_number / second_number)

else:
    print("Invalid operation number")