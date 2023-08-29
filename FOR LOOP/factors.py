n=int(input("enter the number : "))
k=[]
for i in range(1,n+1):
    if(n%i==0):
        k.append(i)
print(k,"are the factors for thr given number")        
        
        