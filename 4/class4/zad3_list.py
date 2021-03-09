#3.  Dla podanej przez użytkownika liście liczb całkowitych
# sprawdź czy pierwszy i ostatni element są takie same.
numbers = (input("Podaj listę liczb całkowitych, rodziel je przecinkami:  "))
print("Lista użytkownika to: ", numbers)
first_num = numbers[0]
last_num = numbers[-1]
if first_num == last_num:
    print("Pierwsza i ostatnia liczba są takie same.")
else:
    print("Pierwsza i ostatnia liczba różnią się!")
