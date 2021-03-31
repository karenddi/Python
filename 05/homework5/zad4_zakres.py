# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def check_in_range(number, users_range1, users_range2):

    if number in range(users_range1, users_range2):
        print("Yes, your number", number, "is in this range.")
    else:
        print("No, your number", number, "is not in this range.")

print("Hi.")
u_range1 = int(input("Check if my number is in range from :  "))
u_range2 = int(input("Check if my number is in range to:  "))
u_num = int(input("Give me a number to check:  "))

check_in_range(u_num, u_range1, u_range2)