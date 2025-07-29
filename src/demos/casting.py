"""Basic casting examples."""

def demo():
    """Basic casting examples."""

    # string casting
    year = 1970
    print("year " + str(year))

    # int casting
    msg = "What is your age? "
    age = int(input(msg))
    print("You are " + str(age) + " years old!")

    # float casting
    dollar = 100
    cents = 0.50
    total = float(dollar) + float(cents)
    print("Total: " + str(total))