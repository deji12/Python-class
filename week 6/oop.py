class Animal:

    def walk(self):
        print("I am walking")

    def speak(self):
        print("I am speaking")

    def greet(self, name):
        print(f"Hello, {name}")

animal = Animal()
animal.walk()
animal.speak()
animal.greet("Taiwo")

animal2 = Animal()
animal2.greet("Deji")