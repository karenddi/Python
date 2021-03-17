#Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi
# na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
# w zależności od otrzymanego parametru.

#BMI = (masa (kg)) / (wzrost (m))²

def BMI():

    weight = int(input("Podaj swoją wagę [kg]:"))
    height = int(input("Podaj swój wzrost [cm]:"))/100
    BMI = (weight / height**2)
    BMI_rounded = round(BMI, 2)
    print("Your BMI is:",BMI_rounded)
    return BMI_rounded



def BMI_interpreter(your_bmi):

    if 17 < your_bmi < 18.49:
        print("niedowaga")
    elif 18.5 < your_bmi < 24.99:
        print("waga prawidłowa")
    elif 25 < your_bmi < 29.99:
        print("nadwaga")
    elif your_bmi > 30:
        print("otyłość")

print("Sprawdź swoje BMI.")
your_bmi = BMI()
print("~~~~~~~~~~~~~~")
BMI_interpreter(your_bmi)