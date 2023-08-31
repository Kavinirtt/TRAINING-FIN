def longest_word(a):
    count=0
    max=count
    max1=[]
    for i in a:
        for j in i:
            count=count+1
            
            if(max<count):
                max=count
                max1=i
        count=0
    return max1

a=["kavin","nivi","loahit","shanmugam","kiruba"]
max1=longest_word(a)
print(max1)

