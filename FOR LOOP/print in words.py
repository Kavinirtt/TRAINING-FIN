n=int(input("enter the number : "))
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
x=
while(n!=0):
    s=n%10
    if(s==1):
        a="one"
        x.append(a)
    elif(s==2):
        b="two"
        x.append(b)
    elif(s==3):
        c="three"
        x.append(c)       
    elif(s==4):
        d="four"
    elif(s==5):
        e="five"
    elif(s==6):
        f="six"
    elif(s==7):
        g="seven"
    elif(s==8):
        h="eight"
    elif(s==9):
        i="nine"
    elif(s==0):
        j="zero"                
    n=n//10
print(x)