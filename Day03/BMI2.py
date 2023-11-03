weight = float(input("enter the weight: "))
height = float(input("enter the height: "))

bmi = round(weight / height**2, 4)

if(bmi < 18):
    print(f"Your BMI is: {bmi}, you are underweight.")
elif(bmi < 25):
    print(f"Your BMI is: {bmi}, you are normal weight.")
elif(bmi < 30):
    print(f"Your BMI is: {bmi}, you are slightly overweight.")
elif(bmi < 35):
    print(f"Your BMI is: {bmi}, you are obese.")
else:
    print(f"Your BMI is: {bmi}, you are clinically obese.")