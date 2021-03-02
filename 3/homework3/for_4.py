# 4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).
natural_num = int(input("Podaj liczbę całkowitą od 0 do 8: "))
if natural_num < 0:
    print("Liczba ujemna! Podaj liczbę między 0 a 8!")
elif natural_num > 8:
    print("Liczba większa niż 8! Podaj liczbę między 0 a 8!")
else:
    num_factorial = 1
    for i in range(1,natural_num + 1):
        num_factorial = num_factorial*i
        print("Silnia ", i,"to: ", num_factorial)