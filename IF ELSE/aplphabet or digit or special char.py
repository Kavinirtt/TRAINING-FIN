n=input("enter the character : ")
if (((ord(n)>=65 and ord(n)<=90)or(ord(n)>=97 and ord(n)<=122))):
    print("it is an aplbhabet")
elif(ord(n)>=48 and ord(n)<=57):
    print("It is an number")
else:
    print("it is an special character")