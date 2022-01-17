import random
import time
import keyboard
import os
import sys

diceNumber = random.randint(1, 6)
isPlaying = True

print("This is the dice rolling simulator.\n")
time.sleep(1)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def checkKey():
    while True:
        print("If you want to play, press 'q' key, else click 'e' to exit: ")
        keyboard.read_key()

        if keyboard.read_key() == 'q':
            print("\nklawisz q")
            break
        elif keyboard.read_key() == 'e':
            print("\nklawisz e")
            break
        else:
            continue
    clearConsole()

checkKey()

while isPlaying == True:
    print("To roll the dice, press R\n")
    print("If you want to exit, press E\n")

    if keyboard.is_pressed('r'):
        clearConsole()
        print("You rolled number ", diceNumber)
    elif keyboard.is_pressed('e'):
        clearConsole()
        isPlaying = False
        sys.exit(0)