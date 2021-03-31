# 1▹ Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
from random import choice


def select_quote(quotes):
    quote = choice(quotes)
    return quote

def reformat(quote):
    quote_and_author = quote.split(' - ')
    return quote_and_author

def show(quote):
    print("Quote of the day is:")
    print("*" * 50)
    print(quote[0].center(50))
    print(quote[1].strip().center(50))
    print("*" * 50)

def show_first5():
    for q in quotes[0:5]:
        print(q)


filename = "quotes.txt"

with open(filename, 'r') as fopen:
    lines = fopen.readlines()

quote = select_quote(lines)
quote = reformat(quote)
show(quote)

