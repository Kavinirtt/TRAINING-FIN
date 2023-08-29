n=int(input("enter the number : "))
Fact=1
for i in range(n,1,-1):
    Fact=Fact*i
print("factorial of",n,"is",Fact)