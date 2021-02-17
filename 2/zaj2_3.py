#„Honesty is the first chapter in the book of wisdom.”, a następnie:
quote = "Honesty is the first chapter in the book of wisdom."
#Policz wszystkie znaki w napisie
print(len(quote))
#Nie modyfikując zmiennej wyświetl słowo wisdom.
print(quote[-7:-1])
#Wyświetl tylko pierwszą połowę tekstu
middle = len(quote)//2
print(middle)
print(quote[0:middle])
#Wyświetl tylko kropkę
print(quote[-1])
#Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[middle::3])
#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[0::2])
#Wyświetl cały cytat odwrotnie
print(quote[::-1])
#Zamień wisdom na słowo friendship
print(quote.replace("wisdom","friendship"))