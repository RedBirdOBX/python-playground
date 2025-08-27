class Dog:

    # 'self' is required for a method within a class
    def __init__(self, name_val, breed_val):

        # properties of the class
        self.name = name_val
        self.breed = breed_val

    # A "method" is a member of the class. functions seem to be "stand alone"
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")
my_dog.bark()

