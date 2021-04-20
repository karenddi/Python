
def users_input():

    try:

        num = input("Give me a list of numbers seperated by , : ")
        num = list(num.replace(",", ""))
        numbers = []

        for n in num:
            n = int(n)
            numbers.append(n)

        return numbers

    except ValueError as err:
        print("Error")
    except TypeError as er:
        print("Error")

        


def count_mean(numbers):

    try:

        counter = len(numbers)
        users_mean = sum(numbers)/counter
        print("Mean counted from your input is: ",users_mean)
        return users_mean
    except TypeError as er:
        print("Error")



nums = users_input()
count_mean(nums)