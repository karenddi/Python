#Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.

#Program zacznie ze stworzonym słownikiem o trzech kluczach:
#marka (str)

#model (str)

#rocznik (int)

#Wypisze ten słownik na ekran (bez żadnego formatowania)

#Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
#“Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”

#Jeśli nie spełnia powyższego warunku, wypisze komunikat:
#“Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”

#Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!),
# aby zobaczyć, czy progam również zmienia swoje zachowanie.


def show_is_vintage(age, original):
    if age >= 25 and car_original == True:
        print(f'Gratulacje! Twój samochód {car["brand"]} może być zarejestrowany jako zabytek.')
    elif age >= 25 and car_original == False:
        print("Twój samochód nie ma wystarczająco dużo oryginalnych części.")
    else:
        print(f'Twój samochód {car["brand"]} jest jeszcze zbyt młody na rejestracje jako zabytek.')

car = {
    'brand': 'renault',
    'model': 'megan',
    'year': 1993,
    'if_original': False
}

print(car)

car_age = 2021 - car['year']
car_original = car['if_original']
show_is_vintage(car_age, car_original)

