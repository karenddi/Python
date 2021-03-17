# Nie korzystając z funkcji wbudowanej min(),
# napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def minimum_of():
    list_numbers = []
    for i in range(0,3):
        num = int(input("Give me a number: "))
        list_numbers.append(num)

    list_numbers.sort()
    print("Minimum from your list is: ",list_numbers[0])
    return list_numbers

print("Welcome!")
minimum_of()
print("The end!")