import math

def demo():
    """Demonstrates numbers and built-in functions in Python."""

    print("\nRounding")
    number1 = 2.9
    print(round(number1))

    print("\nAbsolute Value")
    number2 = -15
    print(abs(number2))

    #using math module
    # https://docs.python.org/3/library/math.html
    print("\nCeiling")
    number3 = 16.5
    print(math.ceil(number3))

    print("\nFloor")
    print(math.floor(number3))

    print("\nTruncating")
    print(math.trunc(number3))
