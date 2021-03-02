# 8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

number1 = int(input("Podaj liczbę 1: "))
number2 = int(input("Podaj liczbę 2: "))
number3 = int(input("Podaj liczbę 3: "))

numbers = [number1, number2, number3]
sorted_numbers = sorted(numbers, reverse=True)

print("Największa liczba to: ",max(numbers))

print("Sortując od największej do najmniejszej to: ",  sorted_numbers)
