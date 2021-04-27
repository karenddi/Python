# Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody.
# Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
# Utwórz kilka storczyków z różnymi parametrami.

class Orchid:
    def __init__(self,kingdom, species, colour, blossom):

        self.kingdom = kingdom
        self.species = species
        self.colour = colour
        self.blossom = blossom


    def show_colour(self):
       return "Your orchid is:", self.colour


    def blossom_time(self):

        return self.species + " "+ "blossom time is" + " " + self.blossom

orchid_1 = Orchid("plants", "Falenopsis", "white", "spring")

orchid_2 = Orchid("plants", "Dendrobium", "yellow", "summer")

orchid_3 = Orchid("plants", "Cymbidium", "blue", "spring")

print(orchid_1.kingdom)

print(orchid_1.blossom_time())




