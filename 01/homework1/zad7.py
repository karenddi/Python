# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
kasa= int(input("Ile złotych chcesz wziąć na wakacje?"))
euro=round(kasa *0.22, 0)
dolar= round(kasa*0.27, 0)
print("Twój wakacyjny budżet to", euro, "euro.")
print("Twój wakacyjny budżet to", dolar, "dolarów.")
