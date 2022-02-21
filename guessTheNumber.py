
# welcome to the guess the number game made on Techopolis.
# import modules for program.
import random
from playsound import playsound
# init the tries
tries = 3
# main loop to check that tries are not 0
while tries > 0:
    computerNumber = random.randint(1, 10)
    userNumber = int(input("Please type your guess between 1-10.")
    # check to see the number is high, low, or correct.)
    if userNumber == computerNumber:
        print("You guessed my number!")
        playsound("correct.mp3")
        break
    elif userNumber > computerNumber:
        print("Your guess is too high!")
        playsound("incorrect.mp3")
        tries -= 1
    elif userNumber < computerNumber:
        print("Your guess is too low!")
        playsound("incorrect.mp3")
        tries -= 1