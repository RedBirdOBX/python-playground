"""Demonstrate conditionals in Python."""

def demo():
    """Demonstrate conditionals in Python."""
    temperature = 101
    if temperature > 100:
        print("It's hot outside!")
        print("I said it's hot outside!")
    elif temperature < 60:
        print("It's cold outside!")
    else:
        print("It's a nice day outside!")


    # same as a switch case
    command = "start"

    match command:
        case "start":
            print("Starting...")
        case "stop":
            print("Stopping...")
        case _:
            print("Unknown command")


    age = 50
    if age < 18 and age < 100:
        print("You are and adult.")

    name = "Shane"
    if not name == "Shane":
        print("You are not Shane.")
