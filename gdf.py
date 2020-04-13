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
Need program to send data to a function and then return function value to determine if the attempts have added to 3.
Using a function to ensure I do not have to retype lines of code. 

"""

incorrectGuess = 0
randomNumber = random.randrange(0, 20)
gameRun = True

print("Please input a random number between 0 and 20. You only have 3 tries so make it count.")
print(randomNumber)

while gameRun:
    if incorrectGuess == 3:
        print("Game over you have reached 3 tries")
        break
    elif incorrectGuess < 3:
        userInput = input(">")
        if (int(userInput) <= 20) and (int(userInput) >= 0):
            if int(userInput) == randomNumber:
                print("Congrats, you guessed right. Game over!")
                break
            elif int(userInput) != randomNumber:
                tooLow = randomNumber > int(userInput)
                tooHigh = randomNumber < int(userInput)
                if tooHigh:
                    incorrectGuess += 1
                    if incorrectGuess >= 3:
                        print("Game over you have reached 3 tries")
                        break
                    elif incorrectGuess < 3:
                        print("You guess was too high")

                if tooLow:
                    incorrectGuess += 1
                    if incorrectGuess >= 3:
                        print("Game over you have reached 3 tries")
                        break
                    elif incorrectGuess < 3:
                        print("You guess was too low")

        elif int(userInput) > 20:
            incorrectGuess += 1
            if incorrectGuess == 3:
                print("Game over you have reached 3 tries")
                break
            elif incorrectGuess < 3:
                print("Enter a number between 0 and 20.")




