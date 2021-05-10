# Utwórz dekorator, który przyjmie funkcję zwracającą wartość liczbową
# BMI i zwraca tę samą wartość z informacją czy BMI jest prawidłowe



def BMI_interpreter(func):

    def BMI_INFO(your_bmi):

        if 17 < your_bmi < 18.49:
            print(your_bmi, "niedowaga")
        elif 18.5 < your_bmi < 24.99:
            print(your_bmi,"waga prawidłowa")
        elif 25 < your_bmi < 29.99:
            print(your_bmi,"nadwaga")
        elif your_bmi > 30:
            print(your_bmi,"otyłość")
        return func(your_bmi)
    return BMI_INFO


@BMI_interpreter

def show_BMI(users_BMI):
    return users_BMI

show_BMI(20)
