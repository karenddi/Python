# 1. Kopia listy - list.copy
# 2. Sortowanie listy - list.sort
# w danym miejscu robi sort, oryginał jest posorotowany, jeśli zrobimy sorted(list) to oryginał zostaje bez zmian
# a posortowane elementy trzeba przypisać do nowej zmiennej!
# 3. Usunie wszystkie elementy z listy - list.clear()
# 4. Policzy wszystkie wystąpienia elementu x w liście - list.count(x)
# 5. Zsumuje elementy w liście -

lista_num =[6,2,5]
new_list = sorted(lista_num)
print(new_list)
print(lista_num)
print(sum(lista_num))
# deep copy - robi się nowa niezależna od oryginału kopia
# copy - kopia powierzchowna, zachowuje kontakt z oryginałem