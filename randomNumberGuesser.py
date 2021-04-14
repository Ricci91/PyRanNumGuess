#! python3
# Number guesser program

import random
import pyinputplus as pyip

# Generate a number between 1 and 20
randomNumber = random.randint(1, 20)

# Variable that records number of tries
numTries = 1

# ask user to enter a number between 1 and 20
guessPrompt = print("Please guess a number between 1 and 20 \n")

# while loop that keeps the user guessing until he gets it correct
gameRunning = True
while gameRunning == True:
    
    # variable with input from user with prompt asking to guess a number between 1 and 20
    userInput = pyip.inputInt()

    # if too high tell the user to guess lower
    if userInput > randomNumber:
        print("You have guessed too high.\nTry a lower number.")
        
        
    # elif too low tell to guess higher
    elif userInput < randomNumber:
        print("You have guessed too low.\nPlease guess a higher number.")
    
        
    # elif correct tell user that he won the game
    else:
        print(f"YOU WON!!\nYou guessed {str(numTries)} times.")
        gameRunning = False
    # count number of tries    
    numTries += 1