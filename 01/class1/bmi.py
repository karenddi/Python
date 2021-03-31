#BMI = (masa (kg)) / (wzrost (m))²
masa = int(input("Podaj swoją wagę [kg]:"))
wzrost = int(input("Podaj swój wzrost [cm]:"))/100
BMI = (masa / wzrost**2)
BMI_rounded = round(BMI, 2)
print("Your BMI is", BMI_rounded)