n=int(input("Enter the number : "))
sum=0
sum1=0
for i in range(0,n):
    sum=sum+(10**i)
    sum1=sum1+sum
print("sum of the series is",sum1)