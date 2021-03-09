#Pobierz od użytkownika parzystą listę elementów.
# Sprawdź czy 2 środkowe elementy są takie same.

numbers = (input("Podaj parzystą ilość liczb całkowitych: "))
print("Lista użytkownika to: ", numbers)
new_numbers = numbers.replace(",", "")
lenght = len(new_numbers)
print(lenght)
middle = lenght/2
print(middle)
mid1 = middle - 1
mid2 = middle

# tu niżej w nawiasach musza być liczby
mid1_num = new_numbers[int(mid1)]
mid2_num = new_numbers[int(mid2)]
print(mid1_num)
print(mid2_num)

if mid1_num == mid2_num:
    print("Środkowe liczby są takie same.")
else:
    print("Środkowe liczby nie są takie same.")
