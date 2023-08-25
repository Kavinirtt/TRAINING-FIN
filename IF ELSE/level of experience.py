age=int(input("age"))
Experience=int(input("Experience"))
if(age<25 and Experience<1):
    print("entry level")
elif(age>=25 and age<=40) and (Experience>1 and Experience<=5):
    print("junor level")
elif(age>=40 and (Experience>5 and Experience<=10)):
    print("senior level")
else:
    print("expert level")