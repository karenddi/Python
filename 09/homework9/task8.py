from random import choice

def whose_conference(who):
    whose = choice(who)
    return whose

def details_conference(more):
    details = choice(more)
    return details

def where_conference(where):
    place = choice(where)
    return place

def show(who, more, where):
    details = more + where
    print("Konferencja",who,more,where)

def opening_files(filename):
    try:

        with open(filename, 'r', encoding="utf8") as fopen:
            lines = fopen.readlines()
            return lines
    except FileNotFoundError as err:
        print(err, "Something went wrong!")







more_con_first = opening_files("more.txt")
more_con = details_conference(more_con_first)

whose_con_first = opening_files("who.txt")
whose_con = whose_conference(whose_con_first)

where_con_first = opening_files("where.txt")
where_con = where_conference(where_con_first)

show(whose_con, more_con, where_con)