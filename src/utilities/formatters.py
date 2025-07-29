"""Module providing various formatting functions."""

def format_number():
    """Format a number in various ways."""
    number = input("Please provide a number to format:")
    print(f"Formatted number w/ 2 decimals: {number:.2f}")  # Format to 2 decimal places
    print(f"Formatted number w/ 3 decimals: {number:.3f}")  # Format to 3 decimal places
    print(f"Currency: ${number:,.2f}")  # Format as currency with commas and 2 decimal places


def format_string():
    """Format a string in various ways."""
    question = "What is your name? "
    name = input(question)

    print(f"Hello, {name}!")
    print("Hello \n" + name)
