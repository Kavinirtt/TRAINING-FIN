a=[3,4,5,6,7,8,9,10,11,12]
x=a.length-1
c=[]
a.forEach((e,i)=> 
c.push(a[x-i])    
)
console.log(c)