n="ramasamy"
m=n.split('')
s=0
m.forEach((e) => {
    if(e=="y")
        s=1
    })
if(s==1)
    console.log("yes")
else
    console.log("no")
