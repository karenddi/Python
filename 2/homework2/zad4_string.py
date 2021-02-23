#4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

book_title = input("Podaj tytuł książki: ")
book_author = input("Podaj nazwisko autora książki:  ")
book_pages = input("Podaj liczbę stron książki:  ")

#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

print(book_title.isalpha())
#Jeżeli tytuł to jedno słowo, to ten kod działa. Jeśli więcej, to przez spację mamy false!
print(book_author.isalpha())
print(book_pages.isnumeric())

#Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

print("Tytuł książki to", book_title.capitalize())
print("Autor książki to", book_author.capitalize())
#Połącz dane w jeden ciąg book za pomocą spacji
book_info = (book_title.capitalize() + " " + book_author.capitalize() + " " + book_pages)
print(book_info)

#Policz liczbę wszystkich znaków w napisie book
print(len("book"))