"""Module providing random functions."""
import random

def age_calculator():
    """Calculate and display age in decades and years remaining."""
    msg = "What is your age? "

    # Everything from input is a 'string'
    age = input(msg)
    decades = int(age) // 10
    yrs_reamining = int(age) % 10
    respones1 = f"You are {age} years old!"
    response2 = f"You are {decades} decades and {yrs_reamining} old"
    print(respones1)
    print(response2)


def expenses_calculator():
    """Calculate and display total expenses from random values."""
    total = 0
    expenditures = []

    num_expenses = int(input("How many expenses do you have? "))

    for i in range(num_expenses):
        x = random.randint(1,100)
        print(f"Expense {i + 1}: ${x}")
        expenditures.append(x)

    total = sum(expenditures)
    print("You spent $", str(total), sep="")
    print("--------------------")