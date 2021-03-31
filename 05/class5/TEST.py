def get_books():
    counter = int(input("How many books you want to add to collection?"))


    books_collection = []
    for book in range(counter):
        title = input("Book title: ")
        rate = int(input(f"{title} - rate [0-10]:  "))
        books_collection.append([title, rate])


    return books_collection

BOOKS = get_books()