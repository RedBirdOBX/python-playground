import random

total = 0
expenditures = []

num_expenses = int(input("How many expenses do you have? "))

for i in range(num_expenses):
    x = random.randint(1,100)
    print(f"Expense {i + 1}: ${x}")
    expenditures.append(x)

total = sum(expenditures)
print("You spent $", str(total), sep="")
print("--------------------")