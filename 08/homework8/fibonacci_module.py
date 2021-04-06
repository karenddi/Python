def fibonacci_sequence(n1, n2, count):

    if nterms <= 0:
       print("Please enter a positive integer.")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,"is", n1)

    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           next_value = n1 + n2

           n1 = n2
           n2 = next_value
           count += 1



nterms = int(input("How many terms would you like to try? "))

n1 = 0
n2 = 1
count = 0

fibonacci_sequence(n1,n2, count)
