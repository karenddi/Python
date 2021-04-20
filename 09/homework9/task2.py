my_tuple = (1, 2, 3, 4, 5, "shoes", "top", 2.2, 12.1, "candy")
index = int(input("Choose a number from 1-10:  "))

try:

    for item in my_tuple:
        my_tuple.replace(index, "lola")
        print(my_tuple)

except AttributeError as err:
    print(err, "You cannot replace items in tuple!")