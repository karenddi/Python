# Wyświetl 3 losowe cytaty

from random import choice

def select_quote(quotes):
    quote = choice(quotes)
    return quote

def show(quote):
    print(quote)


filename = "quotes.txt"

with open(filename, 'r') as fopen:
    lines = fopen.readlines()

for i in range(0,3):
    quote = select_quote(lines)
    show(quote)
