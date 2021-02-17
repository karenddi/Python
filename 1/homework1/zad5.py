# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 
liczba1= int(input("Podaj liczbę 1:"))
liczba2= int(input("Podaj liczbę 2:"))
iloraz = liczba1/liczba2
ile_razy= liczba1 // liczba2
reszta= liczba1 % liczba2
print("Iloraz liczby1 przez liczbę2 to", iloraz)
print("Liczba2 mieści się w liczbie1", ile_razy, "razy")
print ("Resztą dzielenia liczby1 przez liczbę2 jest", reszta)