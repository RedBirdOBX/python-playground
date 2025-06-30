class Animal:
    def __init__(self):
        self.name = ""
        self.IsMammal = True
        self.NumberOfLegs = 0

    def speak(self, sound):
        return f"{self.name} makes a sound of {sound}."


class Dog(Animal):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.name = "Dog"
        self.NumberOfLegs = 4

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


def main():
    # Create an instance of Animal
    animal = Animal()
    animal.name = "Generic Animal"
    print("-------------------")
    print(animal.speak("Roar"))
    print(f"Is {animal.name} a mammal? {animal.IsMammal}")
    print(f"{animal.name} has {animal.NumberOfLegs} legs.")
    print("-------------------")

    # Create an instance of Dog
    dog = Dog()
    print("-------------------")
    print(dog.speak("Woof"))
    print(f"Is {dog.name} a mammal? {dog.IsMammal}")
    print(f"{dog.name} has {dog.NumberOfLegs} legs.")
    print("-------------------")

main()