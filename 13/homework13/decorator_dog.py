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



    def can_participate(self):

        if self.age < 10:
            print("Age of your dog allows him to partcipate in championships!")
        else:
            print("We are sorry :( Age of your dog does not allow him to partcipate in championships.")
        if self.speed >= 40:
            print("Your dog's speed is enough to partcipate in championships!")
        else:
            print("We are sorry. Your dog's speed is not enough to partcipate in championships!")

    @classmethod
    def speed_modify(cls, new_speed):

        cls.min_speed = new_speed

if __name__ == "__main__":




    dog1 = Dog("Sernik", 8, 43)
    dog2 = Dog("Figa", 2, 50)

    dog1.can_participate()
    dog1.speed_modify(20)
    print(dog1.min_speed)
    print(dog2.min_speed)








