"""import random functions."""
import random

def game():
    """A simple dice game where a player competes against the computer."""
    def roll_dice():
        return random.randint(1, 6)

    def play_game():
        name1 = input("Enter your name: ")
        name2 = "Computer"

        player_score = roll_dice()
        computer_score = roll_dice()

        print(f"{name1} rolled: {player_score}")
        print(f"{name2} rolled: {computer_score}")

        if player_score > computer_score:
            print("You win!")
        elif player_score < computer_score:
            print("Computer wins!")
        else:
            print("It's a tie!")

    play_game()
