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


    amount = 10
    tax = 0.06
    total = amount + (amount * tax)
    totalInt = int(total)
    totalFloat = float(totalInt)

    print(total)
    print(totalInt)
    print(totalFloat)

     # Python only has 2 types of numbers: int and float.

    my_int = 42
    my_float = 3.14
    print(my_int)
    print(my_float)
