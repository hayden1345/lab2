def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight = " + str(weight))
    print("Height =" ,height)
    print("Weight = " ,weight)


    BMI = weight/(height**2)
    print("BMI =", round(BMI,2))
    print("Weight Classification: ", end="")
    if BMI < 18.5:
        print("Under Weight")
    elif BMI > 25.0:
        print("Overweight")
    else:
        print("Normal Weight")


calculate_bmi(weight=57, height=1.73)
print("===================")

