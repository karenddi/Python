# 6. Przekopiuj zawartość import this do zmiennej.

import this
text = "The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

#Policz liczbę wystąpień słowa better.

substring = "better"
x_better = text.count(substring)
print(x_better)
print("Słowo better pojawia się w wierszu", x_better, "razy.")

#Usuń z tekstu symbol gwiazdki

text_new = text.strip("*")
print(text_new)

#To nie działa ponieważ pomiędzy gwiazdką a słowem nie ma spacji, dlatego po prostu zamienię

text_new2 = text.replace("*right*", "right")
print(text_new2)

#Zamień jedno wystąpienie explain na understand

text_new3 = text.replace("explain", "understand", 1)
print(text_new3)
#Usuń spacje i połącz wszystkie słowa myślnikiem

text_new4 = text.replace(" ", "-")
print(text_new4)

#Podziel tekst na osobne zdania za pomocą kropki

text_new5 = text.split(".")
print(text_new5)