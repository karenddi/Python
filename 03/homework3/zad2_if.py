# 2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
number1 = int(input("Podaj liczbę całkowitą nr 1:  "))
number2 = int(input("Podaj liczbę całkowitą nr 2:  "))
suma = number1 + number2
if suma > 100:
    print(suma)
else:
    print("Koniec")

