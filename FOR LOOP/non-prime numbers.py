n=int(input("enter the first number : "))
m=int(input("enter the second number : "))

for i in range(n,m+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                print(i)            
            
            