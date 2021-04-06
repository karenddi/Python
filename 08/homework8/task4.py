import random

from hangman_details import choosing_category
from hangman_details import random_codeword

print("Welcome in game Wisielec!")

category = choosing_category()
codeword = random_codeword(category)

codeword_len = len(codeword)
table = list(codeword)
chances = 5
print("Codeword has", codeword_len, "letters. You've got", chances,"chances.")


for i in range(codeword_len):
    table[i] = '_'

while chances > 0:

    print(" ".join(table))

    choice = input("Are you guessing whole codeword or just a letter? Type -'codeword' or 'letter':   ")

    if choice == "letter":
        letter = input("Type a letter: ")
    elif choice == "codeword":
        users_codeword = input("Guess the codeword:   ")
    else:
        print("Choose if you want to guess codeword or letter.")

    if choice == "letter" and letter in codeword:
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
    elif choice == "codeword" and users_codeword == codeword:
        print("Congrats!")
        break

    elif choice == "codeword" and users_codeword != codeword:
            print("Try again!")
    else:
        chances = chances - 1
        print("Try again. You've got",chances, "chances.")


else:
    print("You lost this game.")