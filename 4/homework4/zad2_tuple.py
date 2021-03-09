#2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

my_hobbies = ("dance", "cooking","cooking", "baking", "dance", "dance", "dance")

for hob in my_hobbies:
    if my_hobbies.count(hob) > 1:
        print("Item", hob, "is REPEATED")

#Zdaję sobie sprawę, że powinno się wyświetlać raz ale nie wiem jak to osiągnąć.