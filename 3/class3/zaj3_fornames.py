#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
#(np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
#Następnie powitaj każdą osobę na liście.

names = "Ania, Jola, Kasia"
names = names.replace(" ", "").split(",")
for n in names:
    print("Hello", n)