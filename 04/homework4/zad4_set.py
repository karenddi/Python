# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

#input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

#output:

#[4, 3, 2, 1]
#[14, 13, 12, 11]
#[24, 23, 22, 21]

numlist = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

numlist1 = list(numlist[0:4])
numlist1.reverse()

numlist2 = list(numlist[4:8])
numlist2.reverse()

numlist3 = list(numlist[8:])
numlist3.reverse()

numfinal = [
    numlist1,
    numlist2,
    numlist3
]

for num in numfinal:
    print(num, end ="\n")

