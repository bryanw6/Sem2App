weight = int(input("Please input your weight in kg "))
height = int(input("Please input your height in cm "))

BMI = (weight / height / height) * 10000

print(str(BMI))

if BMI < 18.5:
    print("You are underweight")

elif 18.5 <= BMI <= 24.9:
        print("You have a normal weight")

elif BMI > 24.9:
    print("You are overweight")

else:
    print("Something went wrong, please try again")

    