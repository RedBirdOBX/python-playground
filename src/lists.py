acronyms = []
acronyms.append("AI")
acronyms.append("ML")
acronyms.append("NLP")
acronyms.append("DL")
acronyms.append("CV")  # Adding acronyms to the list
acronyms.insert(2, "RL")  # Inserting an acronym at index 2
acronyms.extend(["GAN", "RNN"])  # Extending the list with more acronyms
acronyms.remove("NLP")  # Removing an acronym

del acronyms[0]  # Deleting the first acronym

acronyms.sort()  # Sorting the list of acronyms
print(acronyms)

# --------------------

numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adding a number to the list
numbers.insert(3, 10)  # Inserting a number at index 3
numbers.extend([7, 8, 9])  # Extending the list with more numbers
numbers.sort
# print(numbers)

if 10 in numbers:  # Checking if a number is in the list
    print("10 is in the list")

num = 7
if num in numbers:  # Checking if a specific number is in the list
    print(f"{num} is in the list")


# --------------------

# SLICES
# we can also delete a slice of the list
# slicing [start index start BEFORE position: end index - end BEFORE position]
# formula: [first char : last char + 1]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
slice1 = letters[1:]  # Slicing the list from index 1 to end
slice2 = letters[:3]  # Slicing the list from index 0 to 3
slice3 = letters[2:4]  # Slicing the list from index 2 to 4 - "c & d"
print(slice1)  # Output: ['b', 'c', 'd', 'e', 'f', 'g']
print(slice2)  # Output: ['a', 'b', 'c']
print(slice3)  # Output: ['c', 'd']

# Adding and accessing letters in a list
letters.append('h')
letters.append("i")  # Adding a letter to the list
print(letters)

del letters[2:5]  # Deleting a slice of the list
print("**del:  " + str(letters) + " **")  # Output after deletion

print(letters[0])  # Accessing the first letter

# Lists within lists - 2 dimensional lists
letters = [
    ['a', 'b', 'c'],
    ['aa', 'bb', 'cc'],
    ['aaa', 'bbb', 'ccc']
]
print(letters[0])  # Accessing the first list
print(letters[0][1])  # Accessing 'b' from the first list
print(letters[1][2])  # Accessing 'cc' from the second list


# we can also use dictionaries
menus = {
    "Breakfast" : ["Eggs","Bacon","Pancakes"],
    "Lunch" : ["BLT","Club","Salad"],
    "Dinner" : ["Pizza","Subs","Fried Chicken"]
}

print("Breakfast:\t", menus["Breakfast"])  # Accessing the breakfast menu
print("Lunch:\t\t", menus["Lunch"])  # Accessing the second item in the lunch menu
print("Dinner:\t\t", menus["Dinner"])  # Accessing the second item in the dinner menu


# comparing lists = must be in the SAME ORDER
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [4, 5, 6]
list4 = [3, 2, 1]
print(list1 == list2)  # True, because the contents are the same
print(list1 == list3)  # False, because the contents are different
print(list1 == list4)  # False, because the order is different