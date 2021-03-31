#Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.

#Co wiemy o tych numerach tych kart?

#All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.

#MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.

#American Express card numbers start with 34 or 37 and have 15 digits.

def users_card(card_num):
    card_num = (input("Give me your card number: "))
    return card_num

def card_nr_length(len_cardnum):
    card_number = users_card(card_number)
    if len(card_number) == 16:
        print("It may be Visa or Mastercard")
    if len(card_number) == 13:
        print("It may be Visa.")
    if len(card_number) == 15:
        print("It may be American Express.")

def if_visa(card_number):
    card_number = users_card(card_number)
    if len(card_number) == (16 or 13) and card_number[0] == 4:
        print("It is VISA.")
    else:
        print("It is NOT a VISA.")

def if_American_Express(card_number):
    card_number = users_card(card_number)
    if len(card_number) == 15 and card_number[0:2] == (34 or 37):
        print("It is American Express.")
    else:
        print("It is not American Express")

card_number = []

if_American_Express(card_number)