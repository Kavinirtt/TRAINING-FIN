n=int(input("Enter the first number : "))
m=int(input("Enter the second number : "))
for i in range(max(n,m),(n*m)+1):
    if (i%n==0 and i%m==0):
        lcm=i
        break
print("lcm of",n,"and",m,"is",lcm)    
