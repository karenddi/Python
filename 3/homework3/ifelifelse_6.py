# 6. Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie
# liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

secret_number = 74
your_number = int(input("Podaj liczbę całkowitą od 1 do 100:  "))
if your_number == secret_number:
    print("gratulacje!")
else:
    print("pudło!")