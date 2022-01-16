agree = None
answer = False

def checkAnswer():
    global answer
    while answer == False:
        agree = input("Do you agree? ")

        if agree == 'y' or agree == 'Y':
            print("Agreed.\n")
            answer = True
        elif agree == 'n' or agree == 'N':
            print("Disagreed.\n")
            answer = True
        else:
            print("Type y, Y for yes or n, N for no.\n")

checkAnswer()
