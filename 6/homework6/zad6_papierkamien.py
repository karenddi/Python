# Napisz grę kamień - papier - nożyce tak, aby korzystać z funkcji.

import random

def points(user,comp):
    u_points = 0
    c_points = 0
    if user_choice == comp_choice:
        print("Remis!")
    elif user_choice == "k" and comp_choice == "n":
        u_points = u_points + 1
        c_points = c_points
        print("Wygrałeś!")
    elif user_choice == "n" and comp_choice == "p":
        print("Wygrałeś!")
        u_points = u_points + 1
        c_points = c_points
    elif user_choice == "p" and comp_choice == "k":
        print("Wygrałeś!")
        u_points = u_points + 1
        c_points = c_points
    else:
        print("Wygrywa komputer!")
        u_points = u_points
        c_points = c_points + 1

    if u_points > c_points:
        print("Wygrałeś, zdobyłeś", u_points,", a komputer:", c_points)
    elif c_points > u_points:
        print("Przegrałeś, zdobyłeś", u_points,", a komputer:", c_points)
    else:
        print("Remis, macie po tyle samo punktów.")

    print("Koniec gry!")


possibilities = ["k", "p", "n"]


print("Witaj w  grze.")
rundy = int(input("Podaj ile rund chcesz zagrać:  "))

while rundy > 0:
    rundy = rundy - 1
    user_choice = input("Wybierz  jedno - papier(p), kamień (k) lub nożyce (n) wpisując symbol:  ")
    comp_choice = random.choice(possibilities)

points(user_choice, comp_choice)

