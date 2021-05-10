# Utwórz dekorator @lowercase_decorator, który przyjmuje dowolną funkcję zwracającą łańcuch znaków
# i zwracający ten sam tekst zmieniony na małe litery.

def lowercase_decorator(func):

    def lowercase_word(word):
        new_word = word.lower()
        print(new_word)
        return func(word)

    return lowercase_word



if __name__ == "__main__":

    @lowercase_decorator

    def sentence_input(sentence):
        return sentence

    sentence_input("KArOLINa")
    sentence_input("LaTO")

