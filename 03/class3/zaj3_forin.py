pa = ""
magic = "hokuspokus"
for num in range (2,10,2):
    pa = pa + str(num) + magic[num]
    print(pa)
#Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

items = ["mapa", "czapka", "buty", "kurtka"]
for i in items:
    print("W góry zabieram",i)
print("Great we are ready!")

#5. Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

sum_nr = 0
for i in range(1, 11):
    sum_nr = i + sum_nr
    if i == 10:
        print(sum_nr)
    else:
        print(sum_nr, end = ", ")
