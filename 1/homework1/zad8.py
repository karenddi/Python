# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.
kasa= int(input("Ile złotych chcesz wziąć na wakacje?"))
euro=round(kasa *0.22, 0)
bilon50= euro//50
bilon20=euro//20
bilon10=euro//10
bilon5=euro//5
print("Twój budżet to mniej więcej",bilon50,"x 50 euro.")
print("Twój budżet to mniej więcej",bilon20,"x 20 euro.")
print("Twój budżet to mniej więcej",bilon10,"x 10 euro.")
print("Twój budżet to mniej więcej",bilon5,"x 5 euro.")