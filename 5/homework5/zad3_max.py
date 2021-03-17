#Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def maximum_of():
    list_numbers = []
    for i in range(0,3):
        num = int(input("Give me a number: "))
        list_numbers.append(num)

    list_numbers.sort()
    print("Maximum from your list is: ",list_numbers[2])
    return list_numbers

print("Welcome!")
maximum_of()
print("The end!")