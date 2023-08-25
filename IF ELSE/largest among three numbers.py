First_number=int(input("enter the first_number : "))
Second_number=int(input("enter the second_number : "))
Third_number=int(input("enter the third_number : "))
if(First_number>Second_number and First_number>Third_number):
    print(First_number,"is the largest number")
elif(Second_number>First_number and Second_number>Third_number):
    print(Second_number,"is the largest number")
else:
    print(Third_number,"is the largest number")        