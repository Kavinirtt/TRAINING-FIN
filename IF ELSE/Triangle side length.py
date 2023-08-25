Side_A=int(input("enter the number : "))
Side_B=int(input("enter the number : "))
Side_c=int(input("enter the number : "))
if(Side_A==Side_B==Side_c):
    print("the given triangle is an equalateral triangle")
elif(Side_A!=Side_B!=Side_c):
    print("the given triangle is an scalene triangle")  
else:
    print("the given triangle is an isoscles triangle")     
