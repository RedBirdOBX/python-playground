# http://api.open-notify.org/astros.json
import requests

def demo():
    print("\nAPI Demo - People in Space")
    print("--------------------------")

    response = requests.get('http://api.open-notify.org/astros.json')
    json = response.json()

    # print(f"Number of people in space: {json['number']}")
    # print(json)
    people = json['people']
    # print(people)

    print("People currently in space:")
    for person in json['people']:
        print(person['name'])