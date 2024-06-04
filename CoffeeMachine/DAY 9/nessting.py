#NEsting 
capital={
    "France":"Paris",
    "Germany": "berlin",
}

#nesting a list in a dictionary

travel_log={
    "France":["paris","Lille","Dijion" ],
    "Germany":["Berlin", "Hamburg","Stuttgart"],
}

#Nesting dictionary in a dictionary
travel_log={
    "France":{"cities_visted":["paris","Lille","Dijion" ],"total_visted":12} ,
    "Germany":{"cities_visted":["Berlin", "Hamburg","Stuttgart"],"total_vists":5},
}

#nesting a dictionary in a list
travel_log=[
   {
        "country": "France",
        "cities_visted":["paris","Lille","Dijion" ],
        "total_visted":12
    } ,
    {
        "country":"Germany" ,
        "cities_visted":["Berlin", "Hamburg","Stuttgart"],
        "total_vists":5
        },
]