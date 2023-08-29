n=int(input("enter the starting number : "))
m=int(input("enter the number of terms : "))
r=int(input("enter the range : "))
s=n
s1=0
for i in range(1,m):
    s=s*r
    s1=s1+s
print(s1+3)    


