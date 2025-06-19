acronyms = {
    "LOL" : "Laughing out loud",
    "IDK" : "I don't know",
    "TBH" : "To be honest"
}

# find a value by sending in key
# print(acronyms["IDK"])


# creating a blank dictionary and adding key-value pairs
ships = {}
ships["USS Enterprise"] = "NCC-1701"
ships["USS Enterprise A"] = "NCC-1701"
ships["USS Voyager"] = "NCC-74656"
ships["USS Defiant"] = "NX-74205"
ships["USS Discovery"] = "NCC-1031"

#updating / replacing a value
ships["USS Enterprise A"] = "NCC-1701A"

# deleting a key-value pair - we hated this one
del ships["USS Discovery"]

# error when not found
# print(ships["USS Kelvin"])

# using GET to avoid error
print(ships.get("USS Kelvin", "USS Kelvin: Ship not found"))  # Returns "Ship not found" if key doesn't exist

# None is a Type in Python that represents the absence of a value. Like Null.
kelvin = ships.get("USS Kelvin")
print(kelvin)  # This will print None if "USS Kelvin" is not found

if not kelvin:
    print("USS Kelvin not found in the ships dictionary.")
else:
    print(f"USS Kelvin found: {kelvin}")

# printing the dictionary
print(ships)

# for loop with a dictionary
# skip == "key" and registry == "value"
for ship, registry in ships.items():
    print(f"{ship} has registry number of {registry}")

# use dictionaries to represent objects
person1 = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"}

person2 = {
    "name": "Jane Smith",
    "age": 25,
    "city": "Los Angeles"}

person3 = {
    "name": "Alice Johnson",
    "age": 28,
    "city": "Chicago"}

persons= {}
persons["person1"] = person1
persons["person2"] = person2
persons["person3"] = person3

for key, person in persons.items():
    print(f"{key}: {person['name']} is {person['age']} years old and lives in {person['city']}.")
    