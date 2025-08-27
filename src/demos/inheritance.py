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


class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("My name is ", self.name, ".", sep="")

    def eat(self):
        print("I am hungry.")

    def walk(self, x):
        self.position[0] += x
        return f"{self.name} walked to position {self.position}."


class RobotDog(Robot):
    def make_noise(self):
            print(f"Woof!")

    # overriding original method in parent class
    def eat(self):

        # get access to the parent class method
        super().eat()
        print(f"{self.name} is eating dog food.")


def demo():
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


    my_robot_dog = RobotDog("RoboBuddy")

    # invoking method of base / parent class
    my_robot_dog.walk(5)

    # invoking method of derived / child class
    my_robot_dog.make_noise()

    my_robot_dog.eat()


