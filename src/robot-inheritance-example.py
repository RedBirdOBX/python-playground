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

def main():
    my_robot_dog = RobotDog("RoboBuddy")

    # invoking method of base / parent class
    my_robot_dog.walk(5)

    # invoking method of derived / child class
    my_robot_dog.make_noise()

    my_robot_dog.eat()

main()
