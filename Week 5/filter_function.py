def is_even_number(number):

    return number % 2 == 0

numbers = [5, 7, 8, 10, 11, 13, 15, 16, 17, 19, 20]

even_numbers = filter(is_even_number, numbers)

print(list(even_numbers))

names = ["Ayodeji", "Aaron", "Bill", "Jackson", "Kelley", "Andrew"]

def does_name_start_with_a(name):
    return name.startswith('A')

print(list(filter(does_name_start_with_a, names)))