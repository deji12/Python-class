footballers = []

class Footballer:

    def __init__(self):

        print("0. Enter 0 to exit\n1. Add new footballer\n2. View all footballers")
            
        while True:
            operation = int(input("Select an option: "))

            if operation == 1:
                self.basic_data()
            elif operation == 2:
                self.display_players()
            elif operation == 0:
                exit()
            else:
                print("Invalid input")

    def basic_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        self.name = name
        self.age = age

        self.store_basic_data()

    def store_basic_data(self):
        new_player = {
            "name": self.name,
            "age": self.age
        }
        footballers.append(new_player)

    def display_players(self):

        for i in footballers:
            print(f'Name: {i["name"]}, Age: {i["age"]}')
            
football = Footballer()