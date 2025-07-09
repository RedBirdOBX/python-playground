# a function must be defined BEFORE it is invoked
def Greeting(name: str) -> str:
    return f"Hello, {name}!"

print(Greeting("World"))


# things must be defined BEFORE they are used
foo = "bar"
print(foo)

def AddStuff(a, b)-> int:
    return b + a

result = (AddStuff(10,20))
print(result)


def AddStuff2(a, b):
    return b + a

