dish = "gzik"
if dish == "pyzy":
    reg = "Wielkopolska"
#print(reg) error name

#a id condition else b
# 1. Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest
# podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input("Podaj liczbę całkowitą:  "))
if (number % 3) == 0:
    print("Twoja liczba jest podzielna przez 3.")
else:
    print("Nie jest podzielna przez 3!")

#3. Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
# W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

opinion1 = float(input("Oceń książkę w skali 1-10:  "))
opinion2 = float(input("Oceń książkę w skali 1-10:  "))
opinion3 = float(input("Oceń książkę w skali 1-10:  "))
opinion_average = (opinion1 + opinion2 + opinion3)/3
if opinion_average > 7:
    print("Bardzo dobra!")
elif opinion_average >= 5:
    print("Przeciętna.")
else:
    print("Nie warta uwagi.")