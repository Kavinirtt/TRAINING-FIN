height=float(input("height"))
weight=float(input("weight"))

BMI=weight/(height**2)

if(BMI<18.5):
    print("under weight")
elif(BMI>=18.5 and BMI<=24.9):
    print("Normal weight")
elif(BMI>=25 and BMI<=29.9):
    print("over weight")
else:
    print("obese")

