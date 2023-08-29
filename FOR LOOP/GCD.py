n=int(input("enter the first number : "))
m=int(input("enter the second number : "))
gcd=1
for i in range(1,(min(n,m))+1):
    if(n%i==0 and m%i==0):
        gcd=i
print("Gcd of",n,"and",m,"is",gcd)        