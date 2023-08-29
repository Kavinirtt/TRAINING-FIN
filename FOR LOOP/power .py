n=int(input("enter the base : "))
m=int(input("enter the exponent : "))
s=1
for i in range(1,m+1):
    s=s*n
print(n,"^",m,"=",s)