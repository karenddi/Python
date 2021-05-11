# Utwórz klasę. Każdy pies ma imię, wiek oraz prędkość z jaką biega.
# W klasie psa powinna być dostępna zmienna klasowa min_speed ustawiona na 40. - DONE
# Utwórz metodę, która sprawdza czy dany pies może brać udział w zawodach. - DONE
# Pies musi być młodszy niż 10 lat i biegać z prędkością ponad 40 km/h. - DONE
# Utwórz metodę klasową, która pozwala zmienić warunek prędkości na np. 45. - DEKORATOR, ZRÓB
# * Dodaj metodę statyczną sprawdzającą jaka dzisiaj pogoda ???
# i jeśli temperatura jest powyżej 10 stopni wyświetli “można biegać”.

def speed_changing_decorator(func):

    def speed_changing(name, age, speed):
        new_speed = int(input("Provide speed of your dog in km/h: "))
        speed = new_speed
        return new_speed


    return speed_changing


class Dog:

    min_speed = 40



    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    @speed_changing_decorator

    def can_participate(self, name, age, speed):

        if age < 10:
            print("Age of your dog allows him to partcipate in championships!")
        else:
            print("We are sorry :( Age of your dog does not allow him to partcipate in championships.")
        if speed >= 40:
            print("Your dog's speed is enough to partcipate in championships!")
        else:
            print("We are sorry. Your dog's speed is not enough to partcipate in championships!")



if __name__ == "__main__":




    # dog1 = Dog("Sernik", 8, 43)
    # print(dog1)

    dog = Dog.can_participate("Sernik", 8, 43)








