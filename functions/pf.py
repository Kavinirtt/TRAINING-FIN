A=float(input("enter the principle amount : "))
r=float(input("enter the rate of interest : "))
n=int(input("enter the number of year : "))
p=A
D=0
for i in range(1,n+1):
    print()
    k=i*A
    print(k,"original value deposited over years")
    print(p,"prinicipal amount in",i,"year")
    c=(p*r)/100
    print(c,"intrest for",i,"year")

    D=p+c


    p=D+A
    #p=((i+1)*A)+D