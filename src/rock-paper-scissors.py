import random

computerChoice = random.choice(["rock", "paper", "scissors"])
userChoice = input("Enter your choice (rock, paper, scissors): ").lower()

print(f"Computer chose: {computerChoice}")
print(f"You chose: {userChoice}")


if userChoice == computerChoice:
    print(f"It's a tie! You both chose {userChoice}.")
elif (computerChoice == "rock" and userChoice == "scissors"):
    print("You loose! Rock crushes.")
elif (computerChoice == "rock" and userChoice == "paper"):
    print("You win! Paper covers rock.")

elif (computerChoice == "paper" and userChoice == "scissors"):
    print("You win! Scissors cuts paper.")
elif (computerChoice == "paper" and userChoice == "rock"):
    print("You lose! Paper covers rock.")

elif (computerChoice == "scissors" and userChoice == "rock"):
    print("You win! Rock crushes scissors.")
elif (computerChoice == "scissors" and userChoice == "paper"):
    print("You lose! Scissors cuts paper.")

else:
    print("unknown.")



