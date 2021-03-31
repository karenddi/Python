#Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.

import os

filename = "quotes.txt"
filename_info = os.stat(filename)
print(filename_info)