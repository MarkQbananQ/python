n = None
answer = False

while answer == False:
    n = input("Podaj liczbę całkowitą: ")

    if int(n) % 2 == 0:
        print("Liczba {} jest parzysta".format(str(n)))
        answer = True
    elif int(n) % 2 != 0:
        print("Liczba {} jest nieparzysta".format(str(n)))
        answer = True
    else:
        continue
