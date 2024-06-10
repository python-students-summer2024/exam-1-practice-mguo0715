"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_random_int'.  
# This function accepts two arguments: a minimum value and a maximum value.
# The function must return a random integer between these two values, inclusive.
# Use the function random.randint() to generate the pseudo-random number.

def get_random_int(x, y):
    integer = random.randint(x, y)
    return integer


##--------------------- Function #2 ---------------------##
# Define a function named 'get_guess'.
# This function accepts a single argument - an integer that serves as a max value.
# This function asks the user once to guess a random integer between 1 and the max value, inclusive.
# The function calls the function named get_random_int in order to generate the random integer in this range.
# If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
# If the user has guessed the random integer correctly, this function returns a boolean True.
# If the user has guessed incorrectly, this function returns a boolean False.

def get_guess(x):
    random = get_random_int(1, x)
    guess = input("Guess a random number between 1 and {}".format(x))
    if not guess.isdigit() or not (1 <= int(guess) <= x):
        return -1 
    if int(guess) == random:
        return True
    else:
        return False
    


##--------------------- Function #3 ---------------------##
# Define a function named 'play_game'.
# This function does not accept any arguments.
# This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
# Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
# If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
# At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."

def play_game():


    guess_1 = (get_guess(5))
    if guess_1 == -1: 
        print("Invalid response!")
        return
    if guess_1 == True:
        print("Correct!")
        guess_1 = 1
    elif guess_1 == False:
        print("Wrong!")
        guess_1 = 0

    guess_2 = (get_guess(5))
    if guess_2 == -1: 
        print("Invalid response!")
        return
    if guess_2 == True:
        print("Correct!")
        guess_2 = 1
    elif guess_2 == False:
        print("Wrong!")
        guess_2 = 0

    guess_3 = (get_guess(5))
    if guess_3 == -1: 
        print("Invalid response!")
        return
    if guess_3 == True:
        print("Correct!")
        guess_3 = 1
    elif guess_3 == False:
        print("Wrong!")
        guess_3 = 0 

    guess_4 = (get_guess(5))
    if guess_4 == -1: 
        print("Invalid response!")
        return
    if guess_4 == True:
        print("Correct!")
        guess_4 = 1
    elif guess_4 == False:
        print("Wrong!")
        guess_4 = 0
    
    proportion = ((guess_1 + guess_2 + guess_3 + guess_4 ) / 4 ) * 100
    print("You guessed {}% of the random numbers correctly.".format(int(proportion)))





