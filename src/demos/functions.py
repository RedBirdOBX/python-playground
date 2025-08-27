# a function must be defined BEFORE it is invoked
# name is the parameter
# "World" is the argument

def greeting(name: str) -> str:
    return f"Hello, {name}!"

def add_stuff(a, b)-> int:
    return b + a

def increment(number, by):
    return number + by

def increment_with_default(number, by=1):
    return number + by

# numbers is a tuple
def add_variable_arguments(*numbers):
    print(numbers)
    return sum(numbers)

def demo():
    print(greeting("World"))

    # things must be defined BEFORE they are used
    foo = "bar"
    print(foo)

    result = (add_stuff(10,20))
    print(result)

    # keyword arguments and labels
    print(increment(number = 10, by = 5))

    # using the default value
    print(increment_with_default(10))

    # NOT using the default value
    print(increment_with_default(10,10))

    print(add_variable_arguments(1,2,3,4,5,6,7,8,9,10))

