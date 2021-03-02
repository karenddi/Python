# 2. Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

your_num = int(input("Podaj liczbę całkowitą 0-20:  "))
secret_num = 5
while your_num is not secret_num:
    print("Zgaduj dalej!")
    your_num = int(input("Podaj liczbę całkowitą 0-20:  "))
print("Gratuluję!")
