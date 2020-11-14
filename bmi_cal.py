print("Enter your height : ")
ft = input("Feet : ")
inch = input("Inches : ")
wt = input("Enter your weight in kgs : ")
ht = (float(ft) * 0.3048) + (float(inch) * 0.0254)
bmi = (float(wt) / ht) / ht
print("Your BMI is ", bmi)
if bmi<18.5:
    print("Under-Weight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
