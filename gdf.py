import random

# this program is used to generate a random number between 0 and 20.
# The user will have 3 tries to guess the write number. If the user does not answer the guess right, the game is over.
# Using the random library.

"""

CODE LOGIC
-----------------

We need the program to generate a random number and then have the user guess it. 
The program will need to check if that guess is equal to the random number and if it is within the 0 to 20 range. 
Program will also need to ensure that the input is a integer and not a string. 

"""

randomNumber = random.randrange(0, 20)
gameRun = True
incorrectGuess = 0
print("Please input a random number between 0 and 20. You only have 3 tries so make it count.")


while gameRun:
    userInput = input(">")
    if int(userInput) <= 20:
        if int(userInput) >= 0:
            if int(userInput) == randomNumber:
                print("Congrats, you guessed right. Game over!")
                break
            else:
                print("Try again. That was incorrect.")
                incorrectGuess = incorrectGuess + 1
    else:
        print("That number is not between the range. Enter a number between 0 and 20.")
        incorrectGuess = incorrectGuess + 1

    if incorrectGuess == 3:
        print("The game is over.")
        print("The random number was "+str(randomNumber)+".")
        break
