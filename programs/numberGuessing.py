import os
import sys
import time
import random

score = 0
inputNumber = None
correctNumber = None

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def guess():
    correctNumber = random.randint(1, 10)

    clearConsole()

    print("Guess a number between 1 and 10.\n\n")
    print("HINT: ")

    if correctNumber % 2 == 0:
        print("The number is even\n")
    elif correctNumber % 2 != 0:
        print("The number is odd\n")
    
    time.sleep(1)

    inputNumber = input("Guess: ")

    if inputNumber == correctNumber:
        print("Correct.\n")
        print("Your score: {}".format(score))
        score = score + 1
    elif inputNumber != correctNumber:
        print("Incorrect.\n")
        print("Your score: {}".format(score))

while True:
    guess()
