# 4▹ Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki.
# Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.

class Mammals:
    def __init__(self, mammary_gland, homeothermic, hair):
        self.mammary_gland = mammary_gland
        self.homeothermic = homeothermic
        self.hair = hair

    def if_mammal(self):
        if self.mammary_gland == "yes":
            print("Its a mammal.")
        else:
            print("It not a mammal.")

if __name__ == '__main__':

    cat = Mammals(mammary_gland="yes", homeothermic= "yes", hair="yes")
    dog = Mammals(mammary_gland="yes", homeothermic= "yes", hair="yes")
    bird = Mammals(mammary_gland="no", homeothermic= "no", hair="no")


    cat.if_mammal()
    bird.if_mammal()
    dog.if_mammal()