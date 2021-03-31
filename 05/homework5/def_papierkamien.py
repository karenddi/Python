def game_pkn():
    import random

    possibilities = ["k", "p", "n"]
    print("Oto gra kamień, papier nożyce.\nW każdym momencie możesz zakończyc grę wpisując słowo 'koniec' zamiast symbolu.")
    rundy = int(input("Podaj liczbę rund, która chcesz zagrać - musi to być liczba całkowita:  "))

    while rundy > 0:
        user_choice = input("Wybierz  jedno - papier(p), kamień (k) lub nożyce (n) wpisując symbol:  ")
        comp_choice = random.choice(possibilities)
        rundy = rundy - 1

        if user_choice == "koniec":
            break
        if user_choice == comp_choice:
            print("Remis!")
        elif user_choice == "k" and comp_choice == "n":
            print("Wygrałeś!")
        elif user_choice == "n" and comp_choice == "p":
            print("Wygrałeś!")
        elif user_choice == "p" and comp_choice == "k":
            print("Wygrałeś!")
        else:
            print("Wygrywa komputer!")

    print("Koniec gry!")

print("Dobry wieczór.")
game_pkn()
print("Dzięki za grę.")