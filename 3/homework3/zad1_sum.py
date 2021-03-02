# 1. Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

names = input("Podaj listę imion, rozdzielając je przecinkami:  ")
names_list = names.replace(" ", "").split(",")
print(names_list)
for name in names_list:
   print("Hello", name)

print("Witajcie")