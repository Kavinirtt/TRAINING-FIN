n=["kavin","shanmugam","kiruba","mohan","sathish"]
m=n.reduce((a,b)=>a=a.length<b.length ? b:a)
console.log(m);