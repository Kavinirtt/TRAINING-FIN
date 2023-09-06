n="nivin"
c=0
n=n.split('')
var l=n.length-1
n.forEach((e,i) => {
    if(e==n[l-i])
        c=c+1   
})
if(c==l+1)
    console.log("it is palindrome")
else
    console.log("not a palindrome")