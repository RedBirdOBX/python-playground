"""Various loop demos."""

def demo():
    """main function."""

    print("Demo: Looping through a list property within an object.\n")
    contacts = {
        "number" : 3,
        "persons" :
        [
            {"name": "John Doe","age": 30,"city": "New York","email": "email1"},
            {"name": "Alice Johnson","age": 28,"city": "Chicago","email": "email3"},
            {"name": "Jane Smith","age": 25,"city": "Los Angeles","email": "email2"}
        ]
    }
    print("Contacts:")

    print("FOR LOOPS")

    # looping thru objects
    for person in contacts["persons"]:
        print(f"{person['name']} is {person['age']} years old, lives in {person['city']}, and can be reached at {person['email']}.")

    for person in contacts["persons"]:
        print(person['email'])

    # FOR LOOPS
    numbers = [1, 2, 3, 4, 5 ]
    for number in numbers:  # Looping through the list of numbers
        print(number)  # Printing each number

    # defining start and stops
    start = 1
    end = 10
    for i in range(start, end + 1):  # Looping from start to end
        print(i)  # Printing each number in the range
    print("--------------------")

    # note that loops require a ":"
    for num in numbers:
        print(f"a) Number: {num}")  # Printing each number with a message
    print("--------------------")

    # returns n number of indices starting at 0.  "5" would give you 1 thru 4.
    my_list = range(5)
    for num in my_list:
        print(f"b) Number: {num}")
    print("--------------------")

    # args are start, stop, and step value
    my_list2 = range(2,10,2)
    for num in my_list2:
        print(f"c) Number: {num}")
    print("--------------------")

    total = 0
    expenditures = []
    for i in range(100):
        expenditures.append(i)
    total = sum(expenditures)
    print("You spent $", str(total), sep="")
    print("--------------------")

    # range starts at 0
    for number in range(1, 20):
        print("iteration: ", number + 1, (number + 1) * ".")

    for number in range(1, 20, 2):
        print("iteration: ", number + 1, (number + 1) * "x")

    for number in range(1, 20):
        print("iteration: ", number, number * "-")
        if number == 10:
            print("You have reached the halfway point!")
            break

    for number in range(1, 5):
        print("iteration: ", number, number * "~")
    else:
        print("You have reached the end of the loop!")

    # WHILE LOOPS
    print("WHILE LOOPS")
    # repeat as long as condition is true
    count = 0
    while count < 5:
        print("Count is:", count)
        count += 1  # Incrementing the count by 1

    number = 100
    while number > 0:
        print("Number is:", number)
        # number = number // 2  # Dividing the number by 2 using integer division
        # same as
        number //= 2  # Dividing the number by 2 using integer division


def demo_with_break_and_continue():
    """main function."""

    print("Demo: Looping with break and continue statements.\n")

    print("FOR LOOPS with break and continue")
    numbers = range(1, 10)
    for number in numbers:
        if number == 3:
            print("Skipping number 3")
            continue  # Skip the rest of the loop for this iteration
        if number == 8:
            print("Breaking the loop at number 8")
            break  # Exit the loop entirely
        print(f"Number: {number}")

    print("\nWHILE LOOPS with break and continue")
    count = 0
    while count < 10:
        count += 1
        if count % 2 == 0:
            print(f"Skipping even number: {count}")
            continue  # Skip even numbers
        if count == 7:
            print("Breaking the loop at count 7")
            break  # Exit the loop entirely
        print(f"Count is: {count}")


def demo_sum_expenses():
    """Demo summing expenses using a loop and using sum()."""
    print("Demo: Summing expenses using a loop and using sum().\n")

    expenses = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  # List of expenses
    total = 0

    for expense in expenses:
        total += expense  # Adding each expense to the sum

    print(f"Total expenses using loop: {total}")  # Printing the total expenses

    # OR
    total2 = sum(expenses)
    print(f"Total expenses using sum(): {total2}")  # Printing the total expenses using sum()