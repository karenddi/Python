#5. Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
# natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód,

list3x3 = [
    ["Julia", "Pietrucha", "piosenkarka"],
    ["Anna", "Nowak", "kasjerka"],
    ["Ida", "Kowalska", "poetka"],
    ["Jola", "Kamińska", "tancerka"]
]
counter = len(list3x3)
for index in range(counter):
    print(index + 1, " - ".join(list3x3[index]))