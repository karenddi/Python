

def party_planner(cookies, people):
    try:

        leftovers = None
        num_each = None

        num_each = cookies  // people
        leftovers = cookies % people

        print(num_each, leftovers)

        return (num_each, leftovers)

    except ZeroDivisionError as err:
        print(err, "You cannot divide by 0!")



party_planner(10,8)