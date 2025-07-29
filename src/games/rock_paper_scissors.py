"""Import random library."""
import random

def play_game():
    """Play a game of rock, paper, scissors."""
    computer_choice = random.choice(["rock", "paper", "scissors"])
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}.")
    elif (computer_choice == "rock" and user_choice == "scissors"):
        print("You loose! Rock crushes.")
    elif (computer_choice == "rock" and user_choice == "paper"):
        print("You win! Paper covers rock.")
    elif (computer_choice == "paper" and user_choice == "scissors"):
        print("You win! Scissors cuts paper.")
    elif (computer_choice == "paper" and user_choice == "rock"):
        print("You lose! Paper covers rock.")
    elif (computer_choice == "scissors" and user_choice == "rock"):
        print("You win! Rock crushes scissors.")
    elif (computer_choice == "scissors" and user_choice == "paper"):
        print("You lose! Scissors cuts paper.")
    else:
        print("unknown.")
