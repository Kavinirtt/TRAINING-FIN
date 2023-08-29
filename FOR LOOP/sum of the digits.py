n=int(input("enter the number : "))
s1=0
while(n!=0):
    s=n%10
    s1=s1+s
    n=n//10
print(s1)