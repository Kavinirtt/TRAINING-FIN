n=int(input("enter the amount of unit used "))
m=1
m1=0
if(n>250):
    n=n-250
    m=n*1.5
    m1=m1+m
    n=250
    if(n>150 and n<=250):
        n=n-150
        m=n*1.2
        m1=m1+m
        n=150
        if(n>50 and n<=150):
            n=n-50
            m=n*0.75
            m1=m1+m
            n=50
            if(n>0 and n<=50):
                n=n-0
                m=n*0.5
                m1=m1+m
print(m1)


    
