#3. Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o
#parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.
#Przekształć powstałą listę w set.

mytuple1 = (1,2,3,4)
mytuple2 = (5,6,7,8,8,8)

mylist1 = list(mytuple1[::2])
print(mylist1)

mylist2 = list(mytuple2[1::2])
print(mylist2)
setall = set(mylist1 + mylist2)
print(setall)