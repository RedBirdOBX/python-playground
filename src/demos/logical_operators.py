"""logical operators."""
def demo():
    """logical operators."""

    print("\nLogical Operators Demo")

    a = True
    b = False

    print("\nAND Operator")
    print(f"{a} and {a} = {a and a}")
    print(f"{a} and {b} = {a and b}")
    print(f"{b} and {a} = {b and a}")
    print(f"{b} and {b} = {b and b}")

    print("\nOR Operator")
    print(f"{a} or {a} = {a or a}")
    print(f"{a} or {b} = {a or b}")
    print(f"{b} or {a} = {b or a}")
    print(f"{b} or {b} = {b or b}")

    print("\nNOT Operator")
    print(f"not {a} = {not a}")
    print(f"not {b} = {not b}")