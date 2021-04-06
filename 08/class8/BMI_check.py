def BMI_interpreter(your_bmi):

    if 17 < your_bmi < 18.49:
        print("Less weight")
        with open("less_weight.txt", "r") as fopen:
            lines = fopen.read()
            print(lines)

    elif 18.5 < your_bmi < 24.99:
        print("Good weight")
        with open("good_weight.txt", "r") as fopen:
            lines = fopen.read()
            print(lines)
    elif 25 < your_bmi < 29.99:
        print("Overweight")
        with open("overweight.txt", "r") as fopen:
            lines = fopen.read()
            print(lines)
    elif your_bmi > 30:
        print("Obese")
        with open("obese.txt", "r") as fopen:
            lines = fopen.read()
            print(lines)
