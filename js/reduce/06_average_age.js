n=[
    {name:"kavin",  age:21},
    {name:"kumar",age:23},
    {name:"sanjai",  age:25},
    {name:"thanishka",  age:27},
    {name:"sajana",   age:29}
]
m=n.reduce((a,b)=>a+b.age,0)
console.log(m/5);
