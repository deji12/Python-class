def square_number(num):

    return num ** 2

my_nums = [2, 3, 6, 7, 9]

m = list(map(square_number, my_nums))

my_new_list = list(m)
print(my_new_list) 