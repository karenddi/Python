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
    print("Konferencja", who, more, where)


filename1 = "who.txt"

with open(filename1, 'r',  encoding="utf8") as fopen:
    lines1 = fopen.readlines()
whose_con = whose_conference(lines1)

filename2 = "more.txt"

with open(filename2, 'r', encoding="utf8") as fopen:
    lines2 = fopen.readlines()

more_con = details_conference(lines2)

filename3 = "where.txt"

with open(filename3, 'r',  encoding="utf8") as fopen:
    lines3 = fopen.readlines()

where_con = where_conference(lines3)

show(whose_con, more_con, where_con)
#rozkmiń jak połączyć żeby wyświetlanie było ładne