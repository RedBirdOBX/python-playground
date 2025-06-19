numbers = [1, 2, 3, 4, 5 ]

for number in numbers:  # Looping through the list of numbers
    print(number)  # Printing each number

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
myList = range(5)
for num in myList:
    print(f"b) Number: {num}")

print("--------------------")

# args are start, stop, and step value
myList2 = range(2,10,2)
for num in myList2:
    print(f"c) Number: {num}")

print("--------------------")

total = 0
expenditures = []
for i in range(100):
    expenditures.append(i)
total = sum(expenditures)
print("You spent $", str(total), sep="")
print("--------------------")

