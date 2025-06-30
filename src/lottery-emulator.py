import random
import time

from datetime import date, timedelta

used_numbers = []


def main():

    start_time = time.time()  # Start timer

    print("--------------------------")
    print("Welcome to the Lottery Emulator!")
    print("--------------------------")

    print("\tGetting your numbers:")

    selection1 = get_random_numbers()
    print(f"\tYour first selection of numbers is: {selection1}")

    selection2 = get_random_numbers()
    print(f"\tYour second selection of numbers is: {selection2}")

    selection3 = get_random_numbers()
    print(f"\tYour third selection of numbers is: {selection3}")

    selection4 = get_random_numbers()
    print(f"\tYour fourth selection of numbers is: {selection4}")

    selection5 = get_random_numbers()
    print(f"\tYour fifth selection of numbers is: {selection5}")

    print("--------------------------")

    selections = [selection1, selection2, selection3, selection4, selection5]

    run_emulator(selections)

    end_time = time.time()  # End timer
    elapsed = end_time - start_time
    print(f"\nProgram completed in {elapsed:.2f} seconds.")


def get_random_numbers():

    numbers = []

    number1 = generate_number()
    # print(f"Generated number: {number1}")
    numbers.append(number1)

    number2 = generate_number()
    # print(f"Generated number: {number2}")
    numbers.append(number2)

    number3 = generate_number()
    # print(f"Generated number: {number3}")
    numbers.append(number3)

    number4 = generate_number()
    # print(f"Generated number: {number4}")
    numbers.append(number4)

    number5 = generate_number()
    # print(f"Generated number: {number5}")
    numbers.append(number5)

    number6 = generate_number()
    # print(f"Generated number: {number6}")
    numbers.append(number6)

    numbers.sort()

    used_numbers.clear()

    return numbers


def generate_number():
    number = random.randint(1, 70)

    attempts = 1
    already_used = number in used_numbers
    while already_used:
        attempts += 1
        print(f"\t\tNumber {number} has already been used. Generating a new number. Attempt {attempts}")
        number = random.randint(1, 70)
        already_used = number in used_numbers

    used_numbers.append(number)

    return number


def run_emulator(selections):

    current_date = date.today()
    has_won = False
    circuit_breaker_counter = 1
    selection_counter = 1
    drawing_counter = 1
    max_loops = 1000000
    max_game_date = date(9999, 12, 31)

    print("Starting the lottery emulator:")

    # circut breaker to avoid infinite loop
    while current_date <= max_game_date and has_won is False:

        # time.sleep(1)  # Pauses for 1 second

        # game is only played on Wednesdays and Fridays
        day_of_week = current_date.weekday()
        day_name = current_date.strftime("%A")

        print("\t--------------------------")

        if day_of_week == 2 or day_of_week == 4:

            winning_numbers = get_random_numbers()

            print(f"\tToday is {current_date}, {day_name}. Playing the lottery!")
            print(f"\tWinning numbers are: {winning_numbers}")

            for selection in selections:

                print(f"\t\tPlaying selection {selection_counter}. Checking your selection: {selection}")

                if selection == winning_numbers:
                    has_won = True
                    print(f"\t\tCongratulations! You have won the lottery with the numbers: {selection} on drawing # {drawing_counter}")
                    print(f"\t\tWinning numbers were: {winning_numbers}")
                    break
                else:
                    print(f"\t\tNo winner. Checking next selection.")

                selection_counter += 1


            selection_counter = 1
            drawing_counter += 1

        else:
            print(f"\tToday is {current_date}, {day_name}. Lottery is only drawn on Wednesdays and Fridays. No game played.")

        current_date = current_date + timedelta(days=1)
        circuit_breaker_counter +=1

        if circuit_breaker_counter >= max_loops:
            break

main()