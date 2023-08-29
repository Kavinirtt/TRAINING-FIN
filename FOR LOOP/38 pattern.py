n=int(input("enter the number : "))
s=0
for i in range(1,n+1):
    for j in range(1,i+1):
        s=s+1
        print(s,end=" ")
    print()