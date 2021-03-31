# 7. Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

#BMI = (masa (kg)) / (wzrost (m))²
weight = int(input("Podaj swoją wagę [kg]:"))
height = int(input("Podaj swój wzrost [cm]:"))/100
BMI = (weight / height**2)
BMI_rounded = round(BMI, 2)
print("Your BMI is", BMI_rounded)
if 17 < BMI_rounded < 18.49:
    print("niedowaga")
elif 18.5 < BMI_rounded < 24.99:
    print("waga prawidłowa")
elif 25 < BMI_rounded < 29.99:
    print("nadwaga")
elif BMI_rounded > 30:
    print("otyłość")