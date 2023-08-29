n=int(input("enter the number : "))
k=n-1
s=0
for i in range(1,n+1):
    for j in range(0,k):
        print(end=" ")
    k=k-1    
    for j in range(1,i+1):
        s=s+1
        print(s,end=" ")
    print()