import random
import time
import os
import sys


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

print("This is the dice rolling simulator.\n")
time.sleep(1)

while True:
    check = input("If you want to play, enter Q, else enter E to exit: ")
    if check == 'q':
        break
    elif check == 'e':
        sys.exit()
    else:
        continue
clearConsole()

while True:
    keyCheck = input("To roll the dice, enter R, if you want to exit, enter E: ")

    if keyCheck == 'r':
        clearConsole()
        print("You rolled number ", random.randint(1, 6))
    elif keyCheck == 'e':
        clearConsole()
        sys.exit(0)
    else:
        continue