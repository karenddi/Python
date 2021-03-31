l_per_100 = 6.4
road = int(input("Podaj długość trasy w km:"))
fuel_price = float(input("Podaje cenę litra paliwa w PLN:"))
l_per_yours = road * 6.4 / 100
cost = l_per_yours * fuel_price
print("Koszt podróży to", cost,"PLN")