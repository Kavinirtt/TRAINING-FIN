n=["kavin","shanmugam","kavin","nivi","nivi","gopal"]

b=n.map(e=>{
    count=0
    c={}

    a=e.split('')
    a.forEach(k =>count++)
        
    
        
    
    c[e]=count
    count=0
    return c
})
console.log(b)
