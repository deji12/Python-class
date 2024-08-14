class Customer:

    def __init__(self):
        self.customer_database = "week-8/customers.txt"

    def get_customer_details(self):

        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        number = input("Enter customer number: ")

        self.name = name
        self.email = email
        self.number = number

    def store_customer_details(self):

        self.get_customer_details()
        
        open_customer_database = open(self.customer_database, "a")
        formatted_data = f"Name: {self.name}, Email: {self.email}, Phone: {self.number}\n"
        
        open_customer_database.write(formatted_data)
        open_customer_database.close()

    def display_customers(self):

        open_customer_database = open(self.customer_database, "r")
        print(open_customer_database.read())
        open_customer_database.close()

print("1. Store customer detials\n2. Display customer details\n3. Exit")
customers = Customer()

while True:
    option = input("Select option: ")
    if option == "1":
        customers.store_customer_details()
    elif option == "2":
        customers.display_customers()
    elif option == "3":
        exit()
    else:
        print("Invalid selection")