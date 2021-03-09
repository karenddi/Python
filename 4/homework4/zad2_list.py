#  Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
numbers = (input("Podaj 10 liczb całkowitych oddzielonych przecinkami:  "))
numbers_edit = numbers.replace(",", "")

new_numbers = []
for n in numbers_edit:
    new_numbers.append(int(n))
numbers_edit = new_numbers


for num in new_numbers:
    if (num % 2) != 0:
        print("Nieparzyste liczby:", num)