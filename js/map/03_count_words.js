n=["kavin","shanmugam","kavin","nivi","nivi","gopal"]

b=n.map((e,i)=>{
    count=0
    a={}

    n.forEach( s => {
        if(s==e)
        count=count+1
        
    })
    a[e]=count
    count=0
    return a
})
console.log(b)
