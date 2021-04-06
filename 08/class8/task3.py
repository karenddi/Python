# Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje
# bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.
import os

def open_and_save(filename):
    try:

    if os.stat(filename).st_size > 0:
        with open(filename, "x+") as fopen:
            content = fopen.read()
            print("It is fine")

open_and_save("less_weight.txt")

#dopisz sobie z gita