# Utwórz klasę Robot każdy robot ma imię i rok produkcji. Utwórz właściwość,
# która zwraca kondycję robota (condition). Kondycja jest liczona jako suma cyfr składających się
# na rok produkcji np. (1973 = 20, 1993 = 22,  2020 = 4 etc).
# Jeśli suma cyfr jest poniżej 5 zwróć tekst ‘seems ok!’, dla wartości 5 - 10 -
# ‘honestly could be better; 10 - 15  ‘bad choice’, 15 w górę ’cheap & weak’.


class Robot:

    def __init__(self, name, production_year):
        self.name = name
        self.production_year = production_year

    @property
    def condition(self):

        numbers = []

        for x in str(self.production_year):
            x = int(x)
            numbers.append(x)

        robot_condition = sum(numbers)

        if robot_condition <= 5:
            return "Seems ok"
        elif 5 < robot_condition <= 10:
            return "Honestly could be better!"
        elif 10 < robot_condition <= 15:
            return "Bad choice!"
        elif robot_condition > 15:
            return "Cheap & weak "




if __name__ == "__main__":

    robot1 = Robot("Wallie", 1999)
    print(robot1.condition)
    print(robot1.name)

    robot2 = Robot("Laila", 2001)
    robot2.condition

#zadanie 6
