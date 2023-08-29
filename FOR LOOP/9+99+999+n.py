n=int(input("Enter the number : "))
sum=0
for i in range(1,n+1):
    sum=sum+((10**i)-1)
print("sum of the series is",sum)