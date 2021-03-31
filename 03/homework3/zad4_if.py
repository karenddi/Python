# 4. Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

word = "Makrama"
if len(word) > 5:
    word.find("a")
    new_word = word.replace("a", "z")
    print(new_word)
else:
    print("Nie wyszło!")
