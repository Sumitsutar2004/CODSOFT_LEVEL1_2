#Game_project2  Rock,Paper,Scissors
import random

user=input("Enter a choice (rock, paper, scissors): \n")
a = ["rock", "paper", "scissors"]
computer = random.choice(a)
print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer== "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

play_again = input("Play again? (yes/no): ")
if(play_again=='yes'):
    print("Run again and Enjoy the game!!!")
else:
    print("Thank you for playing the game")