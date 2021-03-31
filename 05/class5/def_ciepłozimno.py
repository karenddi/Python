
print("Welcome in Hot and Cold  Game.")
import random
guesses = 5

while guesses > 0:
    secret_number = random.choice(range(0,51))
    guesses = guesses - 1
    users_guess = int(input("Guess the number from 0 to 50:  "))

    how_close_to_answer = secret_number - users_guess

    if users_guess == secret_number:
        print("Congrats, you won!")
    elif how_close_to_answer < 5:
        print("Hot!")
    elif 5 < how_close_to_answer < 10:
        print("Warmer.")
    elif 10 < how_close_to_answer < 15:
        print("Cold!")
    elif how_close_to_answer > 15:
        print("Really cold!")
    else:
        print("You are really far away.")
print("The end!", "The secret number was", secret_number)