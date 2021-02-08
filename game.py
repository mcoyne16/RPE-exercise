# game.py
#portions attributed to class 4 lecture video and comments via Slack
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

list = ['rock', 'paper', 'scissors']
if user_choice not in list:
    print("Oops, please choose a valid option and try again")
    exit()
#simulating computer choice

computer_choice = random.choice(list)
print(f"The computer chose: {computer_choice}")
# validate the user selection
#stop the program and not try to determine winner if choice not valid

#determining who won
print("-------------------")
#attributed to classmate Estelle Spanneut in Slack
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