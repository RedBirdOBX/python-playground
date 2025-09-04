import config

# defined outside of the scope of the function
app_name = "I am Global to this file"

def demo():
    """Demo function to print the current Python version."""

    # Many Values to Multiple Variables
    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)

    # you can assign the same value to multiple variables in one line
    a = b = c = "Red"
    print(a)
    print(b)
    print(c)

    # unpacking a collection
    # If you have a collection of values in a list, tuple etc.
    # Python allows you to extract the values into variables.
    # This is called unpacking.
    fruits = ["apple", "banana", "cherry"]
    fruit1, fruit2, fruit3 = fruits
    print(fruit1)
    print(fruit2)
    print(fruit3)

    # reading a global variable
    local_var = "I am local"
    print(local_var)
    print(app_name)
    print(config.APP_NAME)

