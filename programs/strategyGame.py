import time
import os
import sys

startControls = None
chooseNation = None

soldiers = {
    "us": 1360000,
    "ch": 1185000,
    "ru": 1000000,
    "tw": 165000,
    "jp": 247000,
    "kr": 555000,
    "ua": 255000,
    "pl": 160000,
    "de": 64000,
    "uk": 200000,
    "fr": 420000
}
tanks = {
    "us": 8750,
    "ch": 9500,
    "ru": 22710,
    "tw": 1160,
    "jp": 189,
    "kr": 2500,
    "ua": 6500,
    "pl": 800,
    "de": 2500,
    "uk": 227,
    "fr": 527
}
ships = {
    "us": 490,
    "ch": 355,
    "ru": 352,
    "tw": 117,
    "jp": 150,
    "kr": 150,
    "ua": 48,
    "pl": 48,
    "de": 65,
    "uk": 87,
    "fr": 180
}
planes = {
    "us": 13133,
    "ch": 2800,
    "ru": 4000,
    "tw": 400,
    "jp": 740,
    "kr": 740,
    "ua": 125,
    "pl": 272,
    "de": 465,
    "uk": 601,
    "fr": 232
}

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

clearConsole()

time.sleep(1)

print("Direct Command\n\n")

time.sleep(2)

while True:
    startControls = input("Enter C to continue. Enter Q to quit: ")

    if startControls == 'c':
        clearConsole()
        break
    elif startControls == 'q':
        clearConsole()
        sys.exit()
    else:
        clearConsole()
        continue

time.sleep(1)

print("Welcome to Direct Command, very realistic military strategy game.\n\n")

time.sleep(1)

print("You can play 3 nations: the United States, People's Republic of China and Russian Federation.\n\n")

time.sleep(1)

while chooseNation == None: # choosing nation
    chooseNation = input("Choose nation: U for the US, C for China and R for Russia: ")
    
    time.sleep(1)

    clearConsole()

    if chooseNation == 'u':

        print("You have chosen the US!\n")
        time.sleep(1)
        print("You love freedom!\n")

    elif chooseNation == 'c':
        print("You have chosen China!\n")
        time.sleep(1)
        print("Let's retain Taiwan, that rebellious province!\n")

    elif chooseNation == 'r':
        print("You have chosen Russia!\n")
        time.sleep(1)
        print("Let's go, comrade!")

    else:
        continue

print("It's time to explain the basics to you.\n\n")

time.sleep(1)

print("")