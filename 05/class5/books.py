def get_books():
    counter = int(input("How many books you want to add to collection?"))


    books_collection = []
    for book in range(counter):
        title = input("Book title: ")
        rate = int(input(f"{title} - rate [0-10]:  "))
        books_collection.append([title, rate])


    return books_collection

def show_rate(book_list):
    nr = int(input("Which rate you want to see? Give me a nr: "))
    index = nr - 1

    if nr > len(book_list) or nr <0:
        print("No such book in collection.")
    else:
        print(f"Book{book_list[index][0]} is rated -> {book_list[index][1]}/10")


#---main part---
print("Welcome to Library! :)")
books = get_books()
print("Added!")
print("-------------")
show_rate(books)