#Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def even_number():
    even_numbers = []
    how_manynr = int(input("How many numbers you like to add: "))
    for n in how_manynr:
        number = int(input("Give me a number: "))
        if number % 2 == 0:
            return number
            even_numbers.append(number)
            print(number, "jest parzysta.")
print("Nice!")

even_number()