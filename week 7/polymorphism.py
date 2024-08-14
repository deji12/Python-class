class Animal:

    def speak(self):
        print("I am speaking")

class Dog(Animal):
    def speak(self):
        print("I am barking")

class Bird(Animal):
    def speak(self):
        print("I am tweeting")

myAnimals = [Dog(), Bird()]
for i in myAnimals:
    i.speak()