# 2. Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

pasta_list = ["makaron", "feta", "szpinak", "czosnek"]
for i in pasta_list:
    if i == "makaron":
        print("Ugotuj makaron")
    if i == "feta":
        print ("Pokrój fetę")
    if i == "szpinak":
        print("Podsmaż szpinak")
    if i == "czosnek":
        print("Przeciśnij czosnek przez praskę")
print("Podawaj na ciepło ze świeżo zmielonym pieprzem")