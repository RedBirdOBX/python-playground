"""Demo function to loop through a list property within an object."""

def looping_thru_listprop_within_object_demo():
    """Demo function to loop through a list property within an object."""

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
    for person in contacts["persons"]:
        print(f"{person['name']} is {person['age']} years old, lives in {person['city']}, and can be reached at {person['email']}.")

    for person in contacts["persons"]:
        print(person['email'])