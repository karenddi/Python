# Utwórz klasę Robot każdy robot ma imię i rok produkcji. Utwórz właściwość,
# która zwraca kondycję robota (condition). Kondycja jest liczona jako suma cyfr składających się
# na rok produkcji np. (1973 = 20, 1993 = 22,  2020 = 4 etc).
# Jeśli suma cyfr jest poniżej 5 zwróć tekst ‘seems ok!’, dla wartości 5 - 10 -
# ‘honestly could be better; 10 - 15  ‘bad choice’, 15 w górę ’cheap & weak’.


class Robot:


 def __init__(self, name, production_year):
  self.name = name
  self.production_year = production_year


 def conditon(self, production_year):

  numbers = []

  for x in str(production_year):
   x = int(x)
   numbers.append(x)

  robot_condition = sum(numbers)

  if robot_condition <= 5:
   print("Seems ok")
  elif 5 < robot_condition <= 10:
   print("Honestly could be better!")
  elif 10 < robot_condition <= 15:
   print("Bad choice!")
  elif robot_condition > 15:
   print("Cheap & weak ")

  return robot_condition

if __name__ == "__main__":


 robot1 = Robot("Wallie", 1999)
 robot1.conditon(robot1.production_year)

 robot2 = Robot("Laila", 2001)
 robot1.conditon(robot2.production_year)



