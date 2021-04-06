
import BMI_check

def BMI():

    weight = int(input("Provide me your weight [kg]:"))
    height = int(input("Provide me your height [cm]:"))/100
    BMI = (weight / height**2)
    BMI_rounded = round(BMI, 2)
    print("Your BMI is:",BMI_rounded)
    return BMI_rounded

your_BMI = BMI()
BMI_check.BMI_interpreter(your_BMI)

