class Human:

    def __init__(self, name, gender, human_birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = human_birth_year

        self.display_human_details()

    def get_human_age(self):
        return 2024 - self.birth_year

    def add_height(self, height):
        self.height = height

    def display_human_details(self):

        full_sentence = f"You name is {self.name}, you are {self.get_human_age()} years old and your gender is {self.gender}"
        print(full_sentence)

human = Human("Deji", "Male", 1980)