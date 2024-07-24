# Keep asking for user input until they type 'exit'
user_input = ""
while user_input != "exit":
    user_input = input("Type 'exit' to stop: ")
    print("You typed:", user_input)

# Print numbers from 1 to 5
number = 1
while number <= 5:
    print(number)
    number += 1