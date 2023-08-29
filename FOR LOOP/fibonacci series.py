n=int(input("Enter the number : "))
a=0
b=1
c=[]
for i in range(1,n+1):
    c.append(a)
    a,b=b,a+b
print(c,end="")   