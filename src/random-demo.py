import random


def main():

    # Generate a random integer between 1 and 100
    random_integer = random.randint(1, 100)
    print(f"Random Integer: {random_integer}")

    # Generate a random float between 0 and 1
    random_float = random.random()
    print(f"Random Float: {random_float}")

    # Generate a random choice from a list
    choices = ['apple', 'banana', 'cherry']
    random_choice = random.choice(choices)
    print(f"Random Choice: {random_choice}")

main()