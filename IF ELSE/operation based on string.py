a=int(input("enter the first number : "))
b=int(input("enter the second number : "))
c=input("enter the operation to perform : ")
if(c=="add"):
    print(a,"+", b,"=",a+b)
elif(c=="sub"):
    print(a,"-",b,"=",a-b)
elif(c=="mul"):
    print("a * b =",a*b)
elif(c=="/"):
    print("a / b =",a/b)