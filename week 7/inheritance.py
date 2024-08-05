class Animal:

    def speak(self):
        print("I am speaking")


class Dog(Animal):

    def number_of_legs(self):
        print("I have 4 legs")
    def speak(self):
        print("I am barking")

class GermanShepard(Dog):

    def fur_color(self):
        print("Brown")

class Goat(Animal):

    def speak(self):
        print("I am bleating")

max = Dog()
messi = Goat()

sophie = GermanShepard().speak()
