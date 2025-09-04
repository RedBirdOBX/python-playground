"""Basic casting examples."""

def demo():
    """Basic casting examples."""

    # string casting
    year = 1970
    print("year " + str(year))

    # int casting
    msg = "What is your age? "
    age = int(input(msg))
    print(f"You are {str(age)} years old!")

    # float casting
    dollar = 100
    cents = 0.50
    total = float(dollar) + float(cents)
    print("Total: " + str(total))

    x = str(3)    # x will be '3'
    print(x)
    print(type(x))

    y = int(3)    # y will be 3
    print(y)
    print(type(y))

    z = float(3)  # z will be 3.0
    print(z)
    print(type(z))
