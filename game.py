# game.py
import random

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
print("The computer chose: 'paper'")
computer_choice = random.choise(list)

print(f"The computer chose: {computer_choice}")

exit()



#determining who won

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")