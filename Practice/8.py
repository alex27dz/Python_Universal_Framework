from tkinter.font import names


class Person:
    def __init__(self, name, age, ocupation):
        self.name = name
        self.age = age
        self.ocupation = ocupation

    def printinfo(self):
        print(f"Name: {self.name}, Age: {self.age}, Occupation: {self.ocupation}")


alex = Person("name is Alex", 33, "senior qa dev")
alex.printinfo()


