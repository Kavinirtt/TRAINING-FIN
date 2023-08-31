def fibbnoci_series(n):
    a=0
    b=1
    c=[]
    for i in range(1,n+1):
        c.append(a)
        a,b=b,a+b
    return c
user_input=int(input("enter the number : "))
c=fibbnoci_series(user_input)
print(c)