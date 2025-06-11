x = "x"
y = "y"
z = "z"

print(f"Hello, {x} {y} {z}!")
print("Values:", x, y, z)  # Printing values with a comma separator


expenses = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  # List of expenses
sum = 0

for expense in expenses:
    sum += expense  # Adding each expense to the sum

print(f"Total expenses : ${sum}")  # Printing the total expenses
print(f"Total expenses $", sum, sep = "")  # Printing the total expenses