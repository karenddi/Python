import random

food = ["pizza", "spaghetti", "burger", "pasta", "apple", "sandwich", "candy", "cake", "banana", "mango"]
animals = ["horse", "cat", "dog", "bird", "cow", "monkey", "tiger", "chicken", "pig", "whale"]
sports = ["running", "basketball", "volleyball", "skating", "skiing", "swimming", "jogging", "gymnastics", "cycling", "yoga"]


def choosing_category():
    global codeword
    category = input("Choose category: food, animals or sports:  ")
    return category

def random_codeword(category):

    if category == "food":
        codeword = random.choice(food)
    elif category == "animals":
        codeword = random.choice(animals)
    elif category == "sports":
        codeword = random.choice(sports)

    print("Thanks, let the game begin!")

    return codeword



