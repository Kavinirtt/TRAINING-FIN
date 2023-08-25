n=int(input("enter the month: "))
if(n>=1 and n<=12):
    if(n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
        print("31 days in",n,"th month")
    elif(n==2):
        print("29 days in",n,"th month")
    else:
        print("30 days in",n,"th month")     