#1 Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie
# np. “Mój pies, rasy border collie wabi się Dyzio”.

my_dog = ("pies", "golden", "Serniczek")
zwierze, rasa, imie = my_dog
sentence = f"Mój {zwierze}, rasy {rasa} wabi się {imie}"
print(sentence)