x=[
    {name:'tomoto',  category:'vegetable'},
    {name:'apple',   category:'fruit'},
    {name:'orange',  category:'fruit'},
    {name:'beetroot',category:'vegetable'},
    {name:'brinjal', category:'vegetable'}
    ]
    y=x.filter(e=>e.category=='fruit')
    console.log(y,"are the fruits")