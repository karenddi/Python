# 5.Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.


import random
comp_num = (random.randint(1,100))
#print("Losowa liczba to: ",comp_num)
user_num = int(input("Podaj liczbę całkowitą z zakresu 1-100:  "))
if user_num == comp_num:
    print("Brawo!")
