# Stwórz listę pomysłów na prezent dla swoich bliskich. Kiedy nadarzy się okazja,
# aby dać im prezent (święta, urodziny, rocznicę),
# program losowo wybierze jeden (i być może miejsca, w których możesz go zdobyć).

import random

def gifts():
    gift_ideas = ["tea", "coffee", "book", "flowers", "cosmetics"]
    gift = random.choice(gift_ideas)
    print("You can buy: ", gift)

def where_buy(gift):
    if gift == "tea" or "coffee":
        print("You should go to coffee shop.")
    elif gift == "book":
        print("You should go to bookshop.")
    elif gift == "flowers":
        print("You should go to flower shop.")
    elif gift == "cosmetics":
        print("You should go to beauty supply shop.")


print("If you need to buy a present.")

where_buy(gifts())
