weight=float(input("Enter your weight(kg)"))
height=float(input("Enter your height(m)"))

BMI=weight/(height*height)

print("BMI=",BMI)

if BMI<18.5:
    print("Underweight")
elif 24.9>=BMI>=18.5:
    print("Normal Weight")
elif 29.9>=BMI>=25.0:
    print("Over Weight")
else:
    print("Obese")
