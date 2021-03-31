#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

distance = float(input("Podaj dystans w kilometrach:  "))
per_100 = float(input("Podaj spalanie Twojego auta [l/100km]: "))
fuel_price = float(input("Podaj cenę paliwa na litr [zł]:  "))

cost = (distance * per_100) / 100 * fuel_price

print("Koszt Twojej podróży to:", round(cost,2), "PLN.")

