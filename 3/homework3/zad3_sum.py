# 3. W podanym przez użytkownika ciągu wejściowym
# policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

sentence = input("Podaj tekst:  ")
count_lower = 0
for i in sentence:
    if i.islower():
        count_lower = count_lower + 1
print("W tekście użytkownika jest",count_lower, "małych liter.")

count_upper = 0
for i in sentence:
    if i.isupper():
        count_upper = count_upper + 1
print("W tekście użytkownika jest",count_upper, "dużych liter.")

count_digits = 0
for i in sentence:
    if i.isdigit():
        count_digits = count_digits + 1
print("W tekście użytkownika jest",count_digits, "cyfr.")

count_others = 0
for i in sentence:
    if i.isdigit() == False and i.isalpha() == False:
        count_others = count_others + 1
print("W tekście użytkownika jest",count_others, "znaków specjalnych.")


