# game.py
import random
#from random import choice

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
#the comma way: print("You chose: ", x, "another string")
#you could also string concat: print "" + ""
print(f"You chose: {user_choice}")

#simulating computer choice

list = ['rock', 'paper', 'scissors']
computer_choice = random.choice(list)
print(f"The computer chose: {computer_choice}")

#determining who won
print("-------------------")

if computer_choice == "paper" and user_choice == "scissors":
    print("Congrats! You Won!")
elif computer_choice == "scissors" and user_choice == "rock":
    print("Congrats! You Won!")
elif computer_choice == "rock" and user_choice == "paper":
    print("Congrats! You Won!")
elif computer_choice == user_choice:
    print("It's a tie!")
else:
    print("Oh, the computer won. It's ok.")

print("-------------------")
print("Thanks for playing. Please play again!")