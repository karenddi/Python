# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
#w_lod / w_win wysokość lodówki/ windy
w_lod = int(input("Podaj wysokość lodówki [cm]: "))
w_win = 300 #Podane w cm
#s_lod i s_win szerokość lodówki/windy
s_lod = int(input("Podaj szerokość lodówki [cm]: "))
s_win = 250 #Podane w cm
#g_lod o g_win głębokość lodówki i windy
g_lod = int(input("Podaj głębokośc lodówki [cm]: "))
g_win = 250 #Podane wcm
# w_left wysokość, która pozostaje, reszta analogicznie
w_left = w_win - w_lod
s_left = s_win - s_lod
g_left = g_win - g_lod
print("Po wstawieniu lodówki zostaje", w_left,"cm wysokości,", s_left, "cm szerokości oraz", g_left, "cm głębokości.")
