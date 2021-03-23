# Stwórz grę wisielec “bez wisielca”.
#
# Komputer losuje wyraz z dostępnej w programie listy wyrazów.
#
# Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
#
# Użykownik podaje literę.
#
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.
#
# W przeciwnym wpadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.
#
# Możesz ograniczyć liczbę prób do np. 10.

import random

words = ["pizza", "spaghetti", "burger", "pasta", "apple", "sandwich", "candy", "cake", "banana", "mango"]

print("Welcome in game Wisielec!")

codeword = random.choice(words)


codeword_len = len(codeword)
table = list(codeword)
chances = 10

print("Codeword has", codeword_len, "letters. You've got", chances,"chances.")


for i in range(codeword_len):
    table[i] = '_'

while chances > 0:

    print(" ".join(table))

    letter = input("Give me a letter:   ")


    if letter in codeword:
        for i in range(codeword_len):
            if (codeword[i] == letter):
                    table[i] = letter
        if ''.join(map(str,table)) == codeword:

            print("You've got", chances, " chances left.")
            print(" ")
            print(' '.join(table))
            print(" ")
            print("You won!")
            break
    else:
        chances = chances - 1
        print("Try again. You've got",chances, "chances.")


else:
    print("You lost this game. Codeword was:", codeword)