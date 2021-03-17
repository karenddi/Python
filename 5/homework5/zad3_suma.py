# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sum_numbers():
    lst = []
    number = int(input('How many numbers you want to enter: '))
    for n in range(number):
        numbers = int(input('Enter number: '))
        lst.append(numbers)
    print("Sum of elements in given list is :", sum(lst))

sum_numbers()