# Stwórz moduł obliczający pola różnych figur. W nowym pliku utwórz skrypt,
# który na podstawie podanych składowych kształtów pomieszczeń oraz
# ich wymiarów zwraca powierzchnię budynku.

import shapes

def what_figure():
    figure = input("Tell me fiugre of your room e.g. 'trapeze': ")
    return figure

def what_formula(figure):
    if figure == "trapeze":
        shapes.trapeze_area()

figure = what_figure()
what_formula(figure)

#dopisz z gita