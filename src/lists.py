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


numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adding a number to the list
numbers.insert(3, 10)  # Inserting a number at index 3
numbers.extend([7, 8, 9])  # Extending the list with more numbers
numbers.sort
print(numbers)

if 10 in numbers:  # Checking if a number is in the list
    print("10 is in the list")

num = 7
if num in numbers:  # Checking if a specific number is in the list
    print(f"{num} is in the list")


letters = ['a', 'b', 'c', 'd', 'e']
letters.append('f')
letters.append("g")  # Adding a letter to the list
print(letters)

