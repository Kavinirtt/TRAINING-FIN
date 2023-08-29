n=int(input("enter the starting number : "))
m=int(input("enter the number of terms : "))
cd=int(input("enter the difference : "))
sum=n
sum1=0
for i in range(1,m):
    sum=sum+cd
    sum1=sum1+sum
print("the sum of the a.p series is",sum1+1)   

