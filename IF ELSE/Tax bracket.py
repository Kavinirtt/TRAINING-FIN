income=int(input("Enter the Annual income : "))
if(income>=0 and income<150000):
    print(" no tax bracket")
elif(income>=150000 and income<500000):
    print(" low tax bracket")
elif(income>=500000 and income<1500000):
    print("middle tax bracket")
elif(income>=1500000 and income<15000000):
    print("middle tax bracket")
else:
    print(" very hightax bracket")