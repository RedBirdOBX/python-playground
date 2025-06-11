expenses = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  # List of expenses
total = 0

for expense in expenses:
    total += expense  # Adding each expense to the sum

print(f"Total expenses: {total}")  # Printing the total expenses

# OR
total2 = sum(expenses)
print(total)

