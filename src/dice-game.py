# main is the default entry point for the dice game.
def main():
    import random

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

# This is the entry point for the script.
main()