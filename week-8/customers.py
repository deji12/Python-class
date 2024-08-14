customer_database = "week-8/customers.txt"

def get_customer_details():

    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    number = input("Enter customer number: ")

    return name, email, number

def store_customer_details():

    customer_name, customer_email, customer_number = get_customer_details()
    
    open_customer_database = open(customer_database, "a")
    formatted_data = f"Name: {customer_name}, Email: {customer_email}, Phone: {customer_number}\n"
    
    open_customer_database.write(formatted_data)
    open_customer_database.close()

def display_customers():

    open_customer_database = open(customer_database, "r")
    print(open_customer_database.read())
    open_customer_database.close()

print("1. Store customer detials\n2. Display customer details\n3. Exit")

while True:
    option = input("Select option: ")
    if option == "1":
        store_customer_details()
    elif option == "2":
        display_customers()
    elif option == "3":
        exit()
    else:
        print("Invalid selection")